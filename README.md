# Play With Words

This repository provides a comprehensive benchmark suite for evaluating text transformation and manipulation tasks. It is designed to assess and compare the performance of various natural language models on a wide range of linguistic challenges.

---

## Overview

The suite includes:

- **Diverse Tasks:** Over a hundred tasks organized into categories such as:
  - **Artificial Languages:** Tasks like Caesar cipher, mirror language conversion, Pig Latin, leetspeak, etc.
  - **Character Manipulation:** Operations such as removing or replacing characters, swapping cases, etc.
  - **Composite Transformations:** Multi-step operations combining several text transformations.
  - **Language Understanding:** Tasks that test restoration of punctuation, spacing, or dropped vowels.
  - **Letter Analysis:** Counting and extracting letters, identifying unique or repeating characters.
  - **Sentence Manipulation:** Reordering, numbering, or modifying sentences.
  - **Text Analysis & Extraction:** Counting words, sorting, and extracting specific parts of text.
  - **Text Formatting & Word Manipulation:** Converting text formats, applying Markdown styles, and more.

- **Task Definitions & Code:**  
  Each task is defined in JSONL files with clear instructions and Python code snippets that implement the transformation logic.

- **Training Examples:**  
  Sample training data (in both English and Norwegian) are provided to help fine-tune or prompt models on these tasks.

- **Evaluation Results:**  
  The `testresults/` directory contains output logs from various models (e.g., Capybara, Chinchilla, Claude_2_1_Cedar, Gemini-1.5-Pro, etc.) along with status indicators (true/false) showing whether the model output matched the expected result.

---

## Directory Structure

- **`instruction/`**  
  Contains JSONL files with training examples and task instructions (including a Norwegian version).

- **`templates/`**  
  Holds task definitions in JSONL format, including validated samples.

- **`testresults/`**  
  Stores evaluation logs and output results for different language models.

- **Other Scripts & Files:**  
  Additional scripts and resources to generate, test, and evaluate transformations.

---

## Getting Started

### Prerequisites

- Python 3.7 or later
- Required Python packages (see `requirements.txt` if available or install as needed):
  - `re`
  - `string`
  - `nltk` (for sentence tokenization)
  - Other standard libraries

### Installation

Clone the repository:

    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

Install any required dependencies (if provided, otherwise use your own environment setup):

    pip install -r requirements.txt

### Usage

- **Generating Training Examples:**  
  Run the provided scripts in the `instruction/` or `templates/` directories to generate training examples from task definitions.

- **Running Evaluations:**  
  Execute evaluation scripts to run tasks against your chosen language model. Results are saved in the `testresults/` directory.

- **Reviewing Results:**  
  Evaluation output files (in JSONL format) contain the original instructions, expected outputs, model outputs, and status flags indicating success or failure.

---

## Customization

You can add new tasks by editing or adding new JSONL entries in the `templates/` and `instruction/` directories. Contributions that expand the variety of tasks or enhance the evaluation framework are welcome.

---



## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Acknowledgments

This benchmark suite builds upon community efforts to standardize and evaluate text transformation tasks across multiple models and languages. Special thanks to contributors from the NLP community for their ongoing support and inspiration.

---

For any questions or support, please refer to the repository documentation or open an issue on GitHub.
