import pandas as pd
import argparse
import os
import glob

def generate_markdown_tables(input_json_lines_file, markdown_filename, extended_markdown_filename, sorted_json_lines_file=None, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)

    # Initialize columns for status from each bot as 'n/a' by default
    # Identify all possible bots by examining filenames in the testresults_dir
    test_results_files = glob.glob(os.path.join(testresults_dir, '*.jsonl'))
    bots = [os.path.basename(file).split('.')[0] for file in test_results_files]
    for bot in bots:
        df[f'status_{bot}'] = 'n/a'

    # Load and merge status from test result files in testresults_dir
    for testresult_file in test_results_files:
        test_df = pd.read_json(testresult_file, lines=True)
        bot_name = os.path.basename(testresult_file).split('.')[0]
        status_col_name = f'status_{bot_name}'

        # Update status information based on index as the files have the same order
        for index, row in test_df.iterrows():
            if index < len(df) and 'status_' + bot_name in row:
                df.at[index, status_col_name] = row['status_' + bot_name]

    # Sort the DataFrame by 'task group' and 'task'
    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)

    # Add a new column 'task_number' that resets for each task group
    sorted_df['task_number'] = sorted_df.groupby('task group').cumcount() + 1

    # Optionally save the sorted DataFrame back to a JSON Lines file
    if sorted_json_lines_file:
        sorted_df.to_json(sorted_json_lines_file, orient='records', lines=True)
        print(f"Saved sorted JSON Lines to {sorted_json_lines_file}")

    # Generate Markdown for tasks.md
    markdown_string = f"[View extended tasks](./{extended_markdown_filename})\n\n"
    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n"
        # Include all columns except 'code' for the basic tasks view
        markdown_cols = [col for col in group.columns if col != 'code']
        markdown_string += group[markdown_cols].to_markdown(index=False)
        markdown_string += "\n\n"
    with open(markdown_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved report to {markdown_filename}")

    # Generate Markdown for tasks_extended.md
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"
    for name, group in sorted_df.groupby('task group'):
        extended_markdown_string += f"## {name}\n\n"
        group['code'] = group['code'].apply(lambda x: x.replace('\n', '<br>') if isinstance(x, str) else x)
        extended_markdown_string += group.to_markdown(index=False)
        extended_markdown_string += "\n\n"
    with open(extended_markdown_filename, 'w') as file:
        file.write(extended_markdown_string)
    print(f"Saved extended report to {extended_markdown_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_lines_file', type=str, required=True, help='Path to the input JSON Lines file.')
    parser.add_argument('--sorted_json_lines_file', type=str, default=None, help='Path to save the sorted JSON Lines file.')
    parser.add_argument('--testresults_dir', type=str, default='testresults/', help='Directory containing test results JSON Lines files.')

    # Filenames for Markdown outputs
    markdown_filename = 'tasks.md'
    extended_markdown_filename = 'tasks_extended.md'

    args = parser.parse_args()
    generate_markdown_tables(args.input_json_lines_file, markdown_filename, extended_markdown_filename, args.sorted_json_lines_file, args.testresults_dir)

if __name__ == "__main__":
    main()

