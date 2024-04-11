import pandas as pd
import argparse
import os
import glob
import re

def escape_markdown(text):
    """
    Escapes markdown special characters in text to be included in a markdown table.
    """
    markdown_escape_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '|']
    for char in markdown_escape_chars:
        text = text.replace(char, f"\\{char}")
    return text

def format_result(value):
    """
    Returns the result text with markdown characters escaped.
    """
    return escape_markdown(value) if isinstance(value, str) else '-'

def generate_markdown_results(input_json_lines_file, markdown_filename, extended_markdown_filename, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)

    # Initialize all potential result columns with 'n/a' to ensure consistency
    result_columns = []
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        for col in test_df.columns:
            if col.startswith('result_'):
                result_col_name = col.replace('result_', '')
                if result_col_name not in result_columns:
                    result_columns.append(result_col_name)
                    df[result_col_name] = 'n/a'  # Initialize with 'n/a'

    # Merge results from test result files and escape markdown special characters
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        for col in test_df.columns:
            if col.startswith('result_'):
                result_col_name = col.replace('result_', '')
                for index, row in test_df.iterrows():
                    if index < len(df) and col in row:
                        df.at[index, result_col_name] = format_result(row[col])

    # Ensure 'task group' column exists for sorting
    if 'task group' not in df.columns:
        raise ValueError("DataFrame must contain a 'task group' column for sorting.")

    # Sort and reset index
    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)
    sorted_df['#'] = sorted_df.groupby('task group').cumcount() + 1

    # Remove duplicates and select columns for Markdown tables
    markdown_cols = ['#', 'instruction'] + result_columns
    extended_cols = ['#', 'instruction', 'task', 'code', 'target'] + result_columns

    markdown_string = f"[View extended tasks](./{extended_markdown_filename})\n\n"
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"

    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n"
        markdown_string += group[markdown_cols].to_markdown(index=False) + "\n\n"
        
        extended_markdown_string += f"## {name}\n\n"
        extended_markdown_string += group[extended_cols].to_markdown(index=False) + "\n\n"

    with open(markdown_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved simplified report to {markdown_filename}")

    with open(extended_markdown_filename, 'w') as file:
        file.write(extended_markdown_string)
    print(f"Saved extended report to {extended_markdown_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown results from JSON Lines tasks.')
    parser.add_argument('--input_json_lines_file', type=str, default='templates/samples.jsonl', help='Path to the input JSON Lines file.')
    parser.add_argument('--testresults_dir', type=str, default='testresults/', help='Directory containing test results JSON Lines files.')

    markdown_filename = 'results.md'
    extended_markdown_filename = 'results_extended.md'

    args = parser.parse_args()
    generate_markdown_results(args.input_json_lines_file, markdown_filename, extended_markdown_filename, args.testresults_dir)

if __name__ == "__main__":
    main()

