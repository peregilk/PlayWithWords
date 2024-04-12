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
    return escape_markdown(value) if isinstance(value, str) else value

def format_status(value):
    if value is True:
        return "🟢"
    elif value is False:
        return "🔴"
    else:
        return value  # Handles 'n/a' and any other non-boolean value


def generate_markdown_results(input_json_lines_file, markdown_filename, extended_markdown_filename, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)
    
    # Initialize 'output' column
    df['output'] = None
    
    # Process each test result file
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        
        for index, row in test_df.iterrows():
            if 'input' in row and 'output' in row['input']:
                # Update the 'output' for the corresponding row in the main DataFrame
                if index < len(df):
                    df.at[index, 'output'] = format_result(row['input']['output'])
    
            for col in test_df.columns:
                if col.startswith('result_'):
                    status_col = col.replace('result_', 'status_')
                    if col not in df.columns:
                        df[col] = 'n/a'  # Initialize column if not present
                    
                    # Check if index is within the bounds of df
                    if index < len(df):
                        result_value = test_df.at[index, col] if col in test_df.columns else 'n/a'
                        status_value = test_df.at[index, status_col] if status_col in test_df.columns else 'n/a'
                        df.at[index, col] = f"{format_status(status_value)} {format_result(result_value)}"


    if 'task group' not in df.columns:
        raise ValueError("DataFrame must contain a 'task group' column for sorting.")

    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)
    sorted_df['#'] = sorted_df.groupby('task group').cumcount() + 1

    markdown_cols = ['#', 'instruction', 'output'] + [col for col in sorted_df.columns if col.startswith('result_')]
    extended_cols = ['#', 'target','instruction', 'output', 'task', 'code', 'output'] + [col for col in sorted_df.columns if col.startswith('result_')]

    markdown_string = f"[View extended tasks](./{extended_markdown_filename})\n\n"
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"

    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n" + group[markdown_cols].to_markdown(index=False) + "\n\n"
        extended_markdown_string += f"## {name}\n\n" + group[extended_cols].to_markdown(index=False) + "\n\n"

    # Save Markdown files
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

