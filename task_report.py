import pandas as pd
import argparse
import os
import glob

def generate_markdown_tables(input_json_lines_file, markdown_filename, extended_markdown_filename, testresults_dir='testresults/'):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_lines_file, lines=True)

    # Load and merge status from test result files in testresults_dir
    for testresult_file in glob.glob(os.path.join(testresults_dir, '*.jsonl')):
        test_df = pd.read_json(testresult_file, lines=True)
        
        # For each status_ column in the file, update the corresponding status in the main DataFrame
        status_columns = [col for col in test_df.columns if col.startswith('status_')]
        for col in status_columns:
            bot_name = col.replace('status_', '')  # Remove the prefix to shorten the column name
            if bot_name not in df.columns:
                df[bot_name] = 'n/a'  # Initialize the column with 'n/a'
            # Update status information based on index as the files have the same order
            for index, row in test_df.iterrows():
                if index < len(df):
                    df.at[index, bot_name] = row[col]

    # Sort the DataFrame by 'task group' and 'task'
    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)

    # Add a new column '#' that resets for each task group
    sorted_df['#'] = sorted_df.groupby('task group').cumcount() + 1

    # Generate Markdown for tasks.md (simplified view)
    markdown_string = f"[View extended tasks](./{extended_markdown_filename})\n\n"
    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n"
        # Selecting columns for the simplified view, excluding 'task group' and 'target'
        simplified_columns = ['#', 'instruction'] + [col for col in group.columns if col not in ['task group', 'target', 'task_number', 'code']]
        markdown_string += group[simplified_columns].rename(columns={'#': '#'}).to_markdown(index=False)
        markdown_string += "\n\n"
    with open(markdown_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved report to {markdown_filename}")

    # Generate Markdown for tasks_extended.md
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"
    for name, group in sorted_df.groupby('task group'):
        extended_markdown_string += f"## {name}\n\n"
        group['code'] = group['code'].apply(lambda x: x.replace('\n', '<br>') if isinstance(x, str) else x)
        # Include all columns for the extended view and ensure '#' is the first column
        extended_columns = ['#'] + [col for col in group.columns if col != '#']
        extended_markdown_string += group[extended_columns].rename(columns={'#': '#'}).to_markdown(index=False)
        extended_markdown_string += "\n\n"
    with open(extended_markdown_filename, 'w') as file:
        file.write(extended_markdown_string)
    print(f"Saved extended report to {extended_markdown_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_lines_file', type=str, required=True, help='Path to the input JSON Lines file.')
    parser.add_argument('--testresults_dir', type=str, default='testresults/', help='Directory containing test results JSON Lines files.')

    # Filenames for Markdown outputs
    markdown_filename = 'tasks.md'
    extended_markdown_filename = 'tasks_extended.md'

    args = parser.parse_args()
    generate_markdown_tables(args.input_json_lines_file, markdown_filename, extended_markdown_filename, args.testresults_dir)

if __name__ == "__main__":
    main()

