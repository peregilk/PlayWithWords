import argparse
import json
import os
import random
import re
import string
import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def load_tasks(json_lines_file_path: str) -> pd.DataFrame:
    """
    Load tasks from a JSON lines file into a DataFrame.
    """
    try:
        df = pd.read_json(json_lines_file_path, lines=True)
        # Filter out validation tasks and ensure we have exactly 100 tasks
        df = df[df['task_number'] != 11]
        assert len(df) == 100, f"Expected 100 tasks, got {len(df)}"
        return df
    except Exception as e:
        raise Exception(f"Error loading tasks from {json_lines_file_path}: {e}")

def execute_transformation(code: str, corpus_paragraph: str, char1: str, char2: str, char3: str) -> str:
    """
    Execute the transformation code on the input paragraph.
    """
    try:
        exec(f"""
def transform(InputText, Char1, Char2, Char3):
    {code}
    return ModifiedText
""")
        # Call the now-defined transform function
        modified_text = transform(corpus_paragraph, char1, char2, char3)
        return modified_text
    except Exception as e:
        raise Exception(f"Error executing transformation code: {e}")

def create_sample(task_id: int, language: str, df: pd.DataFrame) -> None:
    """
    Create a sample by executing a transformation code snippet.
    """
    try:
        task = df[df['task_number'] == task_id].iloc[0]
        input_text = "Sample text to transform using the provided code snippet."
        modified_text = execute_transformation(task['code'], input_text, *random.sample(string.ascii_lowercase + 'æøå' if language == 'no' else string.ascii_lowercase, 3))
        print(f"Task: {task['task']}\nInput: {input_text}\nOutput: {modified_text}\n")
    except Exception as e:
        raise Exception(f"Error creating sample for task {task_id}: {e}")

def main():
    """
    Main function to generate instruction tuning training examples.
    """
    try:
        parser = argparse.ArgumentParser(description="Generate instruction tuning training examples.")
        parser.add_argument("--json_lines_file_en", type=str, default="templates/samples_en.jsonl", help="Path to the English json-lines file with transformation templates.")
        parser.add_argument("--json_lines_file_no", type=str, default="templates/samples_no.jsonl", help="Path to the Norwegian json-lines file with transformation templates.")

        args = parser.parse_args()

        df_en = load_tasks(args.json_lines_file_en)
        df_no = load_tasks(args.json_lines_file_no)

        print("Random samples for English:")
        for _ in range(10):
            create_sample(random.randint(1, 10), 'en', df_en)

        print("Random samples for Norwegian:")
        for _ in range(10):
            create_sample(random.randint(1, 10), 'no', df_no)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

