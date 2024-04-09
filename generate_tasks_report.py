import pandas as pd
import argparse

def generate_markdown_tables(input_json_filename, markdown_filename, extended_markdown_filename, sorted_json_lines_file=None):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_filename, lines=True)

    # Sort the DataFrame by 'task group' and then by 'task'
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
        markdown_string += group[['task_number', 'instruction', 'target']].to_markdown(index=False)
        markdown_string += "\n\n"
    with open(markdown_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved report to {markdown_filename}")

    # Generate Markdown for tasks_extended.md
    extended_markdown_string = f"[View basic tasks](./{markdown_filename})\n\n"
    for name, group in sorted_df.groupby('task group'):
        extended_markdown_string += f"## {name}\n\n"
        group['code'] = group['code'].apply(lambda x: x.replace('\n', '<br>') if isinstance(x, str) else x)
        extended_markdown_string += group[['task_number', 'task', 'instruction', 'code', 'target']].to_markdown(index=False)
        extended_markdown_string += "\n\n"
    with open(extended_markdown_filename, 'w') as file:
        file.write(extended_markdown_string)
    print(f"Saved extended report to {extended_markdown_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_filename', type=str, default='templates/samples.jsonl', help='Path to the input JSON Lines file.')
    parser.add_argument('--sorted_json_lines_file', type=str, default=None, help='Path to save the sorted JSON Lines file.')
    
    # Filenames for Markdown outputs
    markdown_filename = 'tasks.md'
    extended_markdown_filename = 'tasks_extended.md'
    
    args = parser.parse_args()
    generate_markdown_tables(args.input_json_filename, markdown_filename, extended_markdown_filename, args.sorted_json_lines_file)

if __name__ == "__main__":
    main()
