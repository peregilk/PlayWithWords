import pandas as pd
import argparse

def generate_markdown_tables(input_json_filename, sorted_json_lines_file=None):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_filename, lines=True)

    # Ensure 'code' column is present and correctly referenced
    assert 'code' in df.columns, "DataFrame does not contain a 'code' column."

    # Sort the DataFrame by 'task group' and then by 'task'
    sorted_df = df.sort_values(by=['task group', 'task']).reset_index(drop=True)
    
    # Optionally save the sorted DataFrame back to a JSON Lines file
    if sorted_json_lines_file:
        sorted_df.to_json(sorted_json_lines_file, orient='records', lines=True)
        print(f"Saved sorted JSON Lines to {sorted_json_lines_file}")

    # Generate Markdown tables for each group, including the "code" column
    markdown_string = ""
    for name, group in sorted_df.groupby('task group'):
        markdown_string += f"## {name}\n\n"
        markdown_string += group[['instruction', 'code', 'target']].to_markdown(index=False)
        markdown_string += "\n\n"
    
    return markdown_string

def save_markdown(markdown_string, output_filename='tasks.md'):
    with open(output_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved report to {output_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_filename', type=str, default='templates/samples.jsonl', help='Path to the input JSON Lines file.')
    parser.add_argument('--sorted_json_lines_file', type=str, help='Path to save the sorted JSON Lines file.', default=None)
    
    args = parser.parse_args()
    markdown_string = generate_markdown_tables(args.input_json_filename, args.sorted_json_lines_file)
    save_markdown(markdown_string)

if __name__ == "__main__":
    main()

