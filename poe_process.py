import os
import jsonlines
import argparse
from poe_api_wrapper import PoeApi
import re

# Reading environment variables
b_token = os.getenv('B_TOKEN')
lat_token = os.getenv('LAT_TOKEN')

tokens = {
    'b': b_token,
    'lat': lat_token
}

def standardize_spacing(text):
    """
    Ensures there is exactly one space before and no unnecessary spaces after certain punctuation marks in the given text.
    This targets ., !, and ? specifically, which are common in test comparisons.
    """
    text = re.sub(r'\s*([.!?])', r' \1', text)  # Put exactly one space before punctuation
    text = re.sub(r'([.!?])\s+', r'\1 ', text)  # Remove multiple spaces after punctuation, leave one
    return text.strip()  # Strip whitespace from the ends for a clean comparison



def process_examples(client, training_examples, bot, prefix, start_from):
    # Format the bot name for filename compatibility and define the output file path
    bot_formatted = bot.replace(" ", "_").replace("-", "_").lower()
    output_file = f"testresults/{bot_formatted}.jsonl"

    mode = 'a' if start_from > 0 else 'w'  # Append if starting from a position other than 0
    with jsonlines.open(output_file, mode=mode) as writer:
        for example in training_examples[start_from:]:
            instruction = example['instruction']
            expected_output = example.get('output', '')
            message = f"{prefix}\n\n{instruction}"
            
            # Initialize response aggregation variable
            response = ""
            chat_code = None
            for chunk in client.send_message(bot=bot, message=message):
                response += chunk["response"]
                # Assuming chatCode can be found in the first chunk
                if not chat_code:
                    chat_code = chunk.get("chatCode")

            result = {
                'input': example,
                'result_' + bot: response,
                'status_' + bot: standardize_spacing(response.strip()) == standardize_spacing(expected_output.strip())
            }
            writer.write(result)
            print(f"Processed example: {instruction}")
            print(f"({standardize_spacing(response.strip()) == standardize_spacing(expected_output.strip())})  Expected:\"{standardize_spacing(expected_output.strip())}\" - Result:\"{standardize_spacing(response.strip())}\" \n")

            # After processing each example, delete the chat thread if a chat code was captured
            if chat_code:
                client.delete_chat(bot, chatCode=chat_code)
                print(f"Deleted chat thread for example: {instruction}")


def main(training_file, bot, prefix):
    client = PoeApi(cookie=tokens)

    # Ensure the testresults directory exists
    os.makedirs("testresults", exist_ok=True)

    # Determine how many examples have already been processed
    bot_formatted = bot.replace(" ", "_").replace("-", "_").lower()
    output_file = f"testresults/{bot_formatted}.jsonl"
    processed_count = 0
    if os.path.exists(output_file):
        with jsonlines.open(output_file) as reader:
            processed_count = len(list(reader))
        print(f"Found interrupted output file with {processed_count} lines. Continuing processing from line {processed_count + 1}...")
    else:
        print("Output file does not exist. Starting processing from the beginning...")

    with jsonlines.open(training_file) as reader:
        training_examples = list(reader)

    if processed_count < len(training_examples):
        process_examples(client, training_examples, bot, prefix, processed_count)
    else:
        print("Output file is already completed. Nothing to be done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process training examples using Poe API')
    parser.add_argument('--training_file', type=str, default='instruction/training_examples.jsonl', help='Path to the training examples file (jsonlines)')
    parser.add_argument('--bot', type=str, default='gpt3_5', help='Name of the bot to use')
    parser.add_argument('--prefix', type=str, default='Please answer the following question as short as possible. Just answer the question. No extra explanations or comments.', help='Prefix to add before the instruction')

    args = parser.parse_args()

    main(args.training_file, args.bot, args.prefix)

