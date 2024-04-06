import pandas as pd
import argparse

def generate_markdown_tables(input_json_filename):
    # Read JSON Lines file directly into a Pandas DataFrame
    df = pd.read_json(input_json_filename, lines=True)

    # Adjusting to avoid potential future deprecation issues
    # Group by 'task group', sort within each group by 'task', and reset index without the deprecation warning concern
    grouped = df.groupby('task group', as_index=False, group_keys=False).apply(lambda x: x.sort_values('task')).reset_index(drop=True)

    # Generate Markdown tables for each group
    markdown_string = ""
    for name, group in grouped.groupby('task group'):
        markdown_string += f"## {name}\n\n"
        markdown_string += group[['instruction', 'target']].to_markdown(index=False)
        markdown_string += "\n\n"
    
    return markdown_string

def save_markdown(markdown_string, output_filename='tasks.md'):
    with open(output_filename, 'w') as file:
        file.write(markdown_string)
    print(f"Saved report to {output_filename}")

def main():
    parser = argparse.ArgumentParser(description='Generate Markdown tables from JSON Lines tasks.')
    parser.add_argument('--input_json_filename', type=str, default='templates/sample.jsonl', help='Path to the input JSON Lines file.')
    
    args = parser.parse_args()
    markdown_string = generate_markdown_tables(args.input_json_filename)
    save_markdown(markdown_string)

if __name__ == "__main__":
    main()

