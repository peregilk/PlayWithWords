import sys
import json
import argparse
import jsonlines
import random
import string

# Define the letters of the English alphabet
alphabet = list(string.ascii_lowercase)

# Randomly draw a letter for each variable
Char1, Char2, Char3 = random.sample(alphabet, 3)

# Map the letters to their position in the alphabet (A=1, B=2, ..., Z=26)
Char1_pos = alphabet.index(Char1) + 1
Char2_pos = alphabet.index(Char2) + 1
Char3_pos = alphabet.index(Char3) + 1

def execute_transformation(code: str, corpus_paragraph: str, char1: str, char2: str, char3: str) -> str:
    # Wrapper code to define a function that will be executed by exec.
    # This function includes the transformation logic and returns ModifiedText.
    wrapper_code = f"""
def transform(InputText, Char1, Char2, Char3):
    {code}
    return ModifiedText
"""
    local_vars = {
        'InputText': corpus_paragraph,
        'Char1': char1,
        'Char2': char2,
        'Char3': char3
    }
    # Execute the wrapper code to define the transform function.
    exec(wrapper_code, globals(), local_vars)
    
    try:
        # Call the now-defined transform function with necessary arguments.
        modified_text = local_vars['transform'](corpus_paragraph, char1, char2, char3)
        return modified_text
    except Exception as e:
        # Error handling for any issues during code execution.
        raise Exception(f"Error executing transformation code: {e}")


def generate_training_samples(text: str, json_lines_file_path: str, output_file_path: str, char1: str, char2: str, char3: str, verified_json_lines_file_path: str = None) -> None:
    verified_file = jsonlines.open(verified_json_lines_file_path, mode='w') if verified_json_lines_file_path else None

    with jsonlines.open(output_file_path, mode='w') as output_writer:
        with open(json_lines_file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    json_line = json.loads(line)
                    try:
                        modified_text = execute_transformation(json_line['code'], text, char1, char2, char3)
                        instruction = json_line['instruction'].replace("{InputText}", text).replace("{ModifiedText}", modified_text).replace("{Char1}", char1).replace("{Char2}", char2).replace("{Char3}", char3)
                        output = json_line['target'].replace("{InputText}", text).replace("{ModifiedText}", modified_text).replace("{Char1}", char1).replace("{Char2}", char2).replace("{Char3}", char3)

                        training_sample = {
                            "instruction": instruction,
                            "output": output
                        }

                        output_writer.write(training_sample)

                        if verified_file:
                            verified_file.write(json_line)

                        print(f"Instruction: {instruction}\nOutput: {output}\n")
                    except Exception as e:
                        print(f"Error processing transformation on line {line_number}: {e}")
                except json.JSONDecodeError as e:
                    print(f"Error processing JSON line {line_number}: {e}")

    if verified_file:
        verified_file.close()

def main():
    parser = argparse.ArgumentParser(description="Generate instruction tuning training examples.")
    parser.add_argument("--input_text", type=str, required=True, help="Input text to transform.")
    parser.add_argument("--json_lines_file", type=str, required=True, help="Path to the json-lines file with transformation templates.")
    parser.add_argument("--output_file", type=str, required=True, help="Path to save the output training examples in jsonlines format.")
    parser.add_argument("--verified_json_lines_file", type=str, help="Path to save the verified json-lines file without any processing errors.")

    args = parser.parse_args()

    generate_training_samples(args.input_text, args.json_lines_file, args.output_file, Char1, Char2, Char3, args.verified_json_lines_file)

    print(f"Char1: {Char1} (Position: {Char1_pos}), Char2: {Char2} (Position: {Char2_pos}), Char3: {Char3} (Position: {Char3_pos})")

if __name__ == "__main__":
    main()

