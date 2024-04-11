import pandas as pd
import argparse
import os
import glob

def escape_markdown(text, max_length=100):
    """
    Escapes markdown special characters in text to be included in a markdown table.
    Converts line breaks to a visual indicator and truncates long texts.
    """
    markdown_escape_chars = ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '#', '+', '-', '.', '!', '|']
    for char in markdown_escape_chars:
        text = text.replace(char, f"\\{char}")
    
    text = text.replace('\n', ' ↵ ').replace('\r', '')
    if len(text) > max_length:
        text = text[:max_length].rstrip() + '...'
    return text

def format_result(value):
    """
    Returns the result text with markdown characters escaped.
    """
    return escape_markdown(value) if isinstance(value, str) else '-'

def generate_markdown_results(input_json_lines_file, markdown_filename, extended_markdown_filename, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)
    
    # Initialize all potential result columns with 'n/a'
    result_columns = []
    df['output'] = 'n/a'  # Initialize output column

    # Aggregate result columns and populate 'output' from test result files
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        for col in test_df.columns:
            if col.startswith('result_'):
                result_col_name = col.replace('result_', '')
                if result_col_name not in result_columns:
                    result_columns.append(result_col_name)
                    df[result_col_name] = 'n/a'  # Initialize with 'n/a'
            if 'output' in test_df.columns:
                df['output'] = format_result(test_df['output'].iloc[0])  # Assume all outputs are the same and take the first one

    if 'task group' not in df.columns:
        raise ValueError("DataFrame must contain a 'task group' column for sorting.")

    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)
    sorted_df['#'] = sorted_df.groupby('task group').cumcount() + 1

    markdown_cols = ['#', 'instruction', 'output'] + result_columns
    extended_cols = ['#', 'instruction', 'output', 'task', 'code', 'target'] + result_columns

    markdown_string = f"[View extended tasks](./{extended_markdown_filename})\n\n"
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"

    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n" + group[markdown_cols].to_markdown(index=False) + "\n\n"
        extended_markdown_string += f"## {name}\n\n" + group[extended_cols].to_markdown(index=False) + "\n\n"

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
    
    args = parser.parse_args()
    generate_markdown_results(args.input_json_lines_file, 'results.md', 'results_extended.md', args.testresults_dir)

if __name__ == "__main__":
    main()
