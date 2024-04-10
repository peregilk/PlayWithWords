import os
from poe_api_wrapper import AsyncPoeApi
import asyncio
import jsonlines
import argparse

# Reading environment variables
b_token = os.getenv('B_TOKEN')
lat_token = os.getenv('LAT_TOKEN')

tokens = {
    'b': b_token,
    'lat': lat_token
}

async def process_examples(client, training_examples, bot, output_file, prefix):
    with jsonlines.open(output_file, mode='w') as writer:
        for example in training_examples:
            instruction = example['instruction']
            expected_output = example.get('output', '')
            message = f"{prefix}\n\n{instruction}"
            response = ''
            async for chunk in client.send_message(bot=bot, message=message):
                response += chunk["response"]
            result = {
                'input': example,
                'result_' + bot: response,
                'status_' + bot: response.strip() == expected_output.strip()
            }
            writer.write(result)
            print(f"Processed example: {instruction}")

async def main(training_file, bot, output_file, prefix):
    client = await AsyncPoeApi(cookie=tokens).create()
    with jsonlines.open(training_file) as reader:
        training_examples = list(reader)
    await process_examples(client, training_examples, bot, output_file, prefix)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process training examples using Poe API')
    parser.add_argument('--training_file', type=str, required=True, help='Path to the training examples file (jsonlines)')
    parser.add_argument('--bot', type=str, default='gpt3_5', help='Name of the bot to use')
    parser.add_argument('--output_file', type=str, required=True, help='Path to the output file (jsonlines)')
    parser.add_argument('--prefix', type=str, default='Please answer the following question as short as possible. Just answer the question. No extra explanations or comments.', help='Prefix to add before the instruction')

    args = parser.parse_args()

    asyncio.run(main(args.training_file, args.bot, args.output_file, args.prefix))
