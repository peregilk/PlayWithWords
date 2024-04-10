import pandas as pd
import argparse
import os
import glob

def format_status(value):
    if value is True:
        return "🟢"
    elif value is False:
        return "🔴"
    else:
        return "-"  # Handles 'n/a' and any other non-boolean value

def generate_markdown_tables(input_json_lines_file, markdown_filename, extended_markdown_filename, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)

    # Initialize all potential status columns with 'n/a' to ensure consistency
    status_columns = []
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        for col in test_df.columns:
            if col.startswith('status_'):
                status_col_name = col.replace('status_', '')
                if status_col_name not in status_columns:
                    status_columns.append(status_col_name)
                    df[status_col_name] = 'n/a'  # Initialize with 'n/a'

    # Merge status from test result files and format values
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        for col in test_df.columns:
            if col.startswith('status_'):
                status_col_name = col.replace('status_', '')
                for index, row in test_df.iterrows():
                    if index < len(df) and col in row:
                        df.at[index, status_col_name] = format_status(row[col])

    # Ensure 'task group' column exists for sorting
    if 'task group' not in df.columns:
        raise ValueError("DataFrame must contain a 'task group' column for sorting.")

    # Sort and reset index
    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)
    sorted_df['#'] = sorted_df.groupby('task group').cumcount() + 1

    # Remove duplicates and select columns for Markdown tables
    markdown_cols = ['#', 'instruction'] + status_columns
    extended_cols = ['#', 'instruction', 'task', 'code', 'target'] + status_columns

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
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_lines_file', type=str, required=True, help='Path to the input JSON Lines file.')
    parser.add_argument('--testresults_dir', type=str, default='testresults/', help='Directory containing test results JSON Lines files.')

    markdown_filename = 'tasks.md'
    extended_markdown_filename = 'tasks_extended.md'

    args = parser.parse_args()
    generate_markdown_tables(args.input_json_lines_file, markdown_filename, extended_markdown_filename, args.testresults_dir)

if __name__ == "__main__":
    main()

