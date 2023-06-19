# ai-generate-unittest 
# Pytest Unit Test Generator

This command-line tool generates Pytest unit tests for Python functions. It uses OpenAI's GPT-3 to generate high-quality test cases that verify the behavior of the function for a wide range of possible inputs and edge cases.

## Requirements

- Python 3.6 or higher
- Pytest
- OpenAI API credentials

## Installation

1. Clone this repository: `git clone https://github.com/your-username/pytest-unit-test-generator.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up your OpenAI API credentials by following the instructions [here](https://beta.openai.com/docs/authentication).
4. Configure the tool's settings by editing the `config.py` file.

## Usage

python main.py function_name --pytest_path=path/to/pytest/files --auto_accept

- `function_name`: the name of the Python function to generate a unit test for.
- `--pytest_path`: the path to the Pytest files. Defaults to `tests/`.
-