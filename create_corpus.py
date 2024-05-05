import sys
import json
import argparse
import jsonlines
import random
import string
import os
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
import logging
from tqdm import tqdm

# Disable verbose downloader
nltk.download('punkt', quiet=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def load_tasks(json_lines_file_path: str) -> pd.DataFrame:
    """
    Load tasks from a JSON lines file into a DataFrame.
    """
    try:
        df = pd.read_json(json_lines_file_path, lines=True)
        return df[df['task_number'] != 11]
    except Exception as e:
        logging.error(f"Error loading tasks from {json_lines_file_path}: {str(e)}")
        sys.exit(1)

def execute_transformation(code: str, corpus_paragraph: str, char1: str, char2: str, char3: str) -> str:
    """
    Execute the transformation code on the input paragraph.
    """
    try:
        local_vars = {
            'InputText': corpus_paragraph,
            'Char1': char1,
            'Char2': char2,
            'Char3': char3,
            'string': string,
            'nltk': nltk,
            'sent_tokenize': sent_tokenize
        }
        exec(f"""
def transform(InputText, Char1, Char2, Char3):
    import re
    try:
        {code}
    except Exception as e:
        return 'Error in transformation code: ' + str(e)
    return ModifiedText
""", globals(), local_vars)
        return local_vars['transform'](corpus_paragraph, char1, char2, char3)
    except Exception as e:
        logging.error(f"Error executing transformation code: {str(e)}")
        sys.exit(1)

def read_template(filename: str) -> str:
    """
    Read template from the file.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        logging.error(f"Template file {filename} not found.")
        sys.exit(1)

def format_template(template: str, system_prompt: str, instructions: str, modified_text: str) -> str:
    """
    Format the dialogue template with given parameters and escape necessary characters.
    """
    formatted_template = template.replace("{{ system_prompt }}", system_prompt)
    formatted_template = formatted_template.replace("{{ user_msg_1 }}", instructions)
    return formatted_template.replace("{{ model_answer_1 }}", modified_text).replace('\n', '\\n').replace('"', '\\"')

def process_input_file(input_file: str, df_no: pd.DataFrame, df_en: pd.DataFrame, output_file: jsonlines.Writer, chat_template: str):
    """
    Process each line in the input JSONL file based on language and generate output with a progress bar.
    """
    with jsonlines.open(input_file) as reader:
        for item in tqdm(reader, desc="Processing input file"):
            if item['lang_fasttext'] in ['no', 'en']:
                df = df_no if item['lang_fasttext'] == 'no' else df_en
                input_text = item['text']
                sample_id = item['id']
                chars = random.sample(string.ascii_lowercase + 'æøå' if item['lang_fasttext'] == 'no' else string.ascii_lowercase, 3)
                try:
                    task = df.sample(1).iloc[0]  # Random task from the dataframe
                    modified_text = execute_transformation(task['code'], input_text, chars[0], chars[1], chars[2])
                    instruction = task['instruction'].replace("{InputText}", input_text).replace("{ModifiedText}", modified_text)
                    formatted_template = format_template(chat_template, "I am a helpful chat bot.", instruction, modified_text)
                    output_file.write({"id": sample_id, "text": formatted_template})
                except Exception as e:
                    logging.error(f"Error processing input line {sample_id}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Process input data to generate training examples.")
    parser.add_argument("--input_file", type=str, required=True, help="Path to the input jsonlines file.")
    parser.add_argument("--json_lines_file_no", type=str, default="templates/samples_no.jsonl", help="Path to the Norwegian transformation template file.")
    parser.add_argument("--json_lines_file_en", type=str, default="templates/samples_en.jsonl", help="Path to the English transformation template file.")
    parser.add_argument("--chat_template_file", type=str, default="chat_template.txt", help="Path to the chat dialogue template file.")
    parser.add_argument("--output_file", type=str, default="output.jsonl", help="Path to output the jsonlines results.")
    args = parser.parse_args()

    # Download necessary NLTK packages only once
    # nltk.download('punkt')

    df_no = load_tasks(args.json_lines_file_no)
    df_en = load_tasks(args.json_lines_file_en)
    chat_template = read_template(args.chat_template_file)

    with jsonlines.open(args.output_file, mode='w') as output_file:
        process_input_file(args.input_file, df_no, df_en, output_file, chat_template)

if __name__ == "__main__":
    main()

