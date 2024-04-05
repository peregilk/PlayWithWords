import sys
import json
import argparse
import jsonlines

def execute_transformation(code: str, corpus_paragraph: str) -> str:
    # Execute the transformation code to generate ModifiedText
    local_vars = {'InputText': corpus_paragraph}
    try:
        exec(code, globals(), local_vars)
        modified_text = local_vars.get('ModifiedText')
        if modified_text is None:
            raise NameError("'ModifiedText' is not defined in the executed code.")
        return modified_text
    except Exception as e:
        # Error handling for any issues during code execution
        raise Exception(f"Error executing transformation code: {e}")

def generate_training_samples(text: str, json_lines_file_path: str, output_file_path: str, verified_json_lines_file_path: str = None) -> None:
    # Conditional opening of the verified jsonlines file before the 'with' statement
    verified_writer = None
    if verified_json_lines_file_path:
        verified_writer = open(verified_json_lines_file_path, mode='w')

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        with open(json_lines_file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    json_line = json.loads(line)
                    try:
                        # Generate the ModifiedText based on the source text and the task's code
                        modified_text = execute_transformation(json_line['code'], text)

                        # Fill in the template with either the original text or the modified text
                        instruction = json_line['instruction'].replace("{InputText}", text).replace("{ModifiedText}", modified_text)

                        # Determine the appropriate output for the training sample based on the task definition
                        output = json_line['target'].replace("{InputText}", text).replace("{ModifiedText}", modified_text)

                        training_sample = {
                            "instruction": instruction,
                            "output": output
                        }

                        # Write the training sample to the output file
                        output_file.write(json.dumps(training_sample) + '\n')

                        # If verified_json_lines_file_path is provided, write the line to the verified JSON-lines file
                        if verified_writer is not None:
                            verified_writer.write(json.dumps(json_line) + '\n')

                        # Print the instruction and output to the console for verification
                        print(f"Instruction: {instruction}\nOutput: {output}\n")
                    except Exception as e:
                        # Print any error messages encountered during the transformation or file operations
                        print(f"Error processing transformation on line {line_number}: {e}")
                except json.JSONDecodeError as e:
                    # Print the error message for the invalid JSON line and continue execution
                    print(f"Error processing JSON line {line_number}: {e}")

    # Properly close the verified_writer if it was opened
    if verified_writer is not None:
        verified_writer.close()



def main():
    parser = argparse.ArgumentParser(description="Generate instruction tuning training examples.")
    parser.add_argument("--input_text", type=str, required=True, help="Input text to transform.")
    parser.add_argument("--json_lines_file", type=str, required=True, help="Path to the json-lines file with transformation templates.")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save the output training examples.")
    parser.add_argument("--verified_json_lines_file", type=str, help="Path to save the verified json-lines file without any processing errors.")

    args = parser.parse_args()

    generate_training_samples(args.input_text, args.json_lines_file, args.output_file, args.verified_json_lines_file)

if __name__ == "__main__":
    main()
