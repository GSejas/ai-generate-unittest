import argparse
import os
from generate import unit_test_from_function

# TODO: import any other necessary modules

# parse command-line arguments
parser = argparse.ArgumentParser(description='Generate Pytest unit tests from Python functions.')
parser.add_argument('function', type=str, help='The Python function to generate unit tests for.')
parser.add_argument('--pytest_path', type=str, default='tests/', help='The path to the Pytest files.')
parser.add_argument('--auto_accept', action='store_true', help='Automatically generate and accept the unit test.')

args = parser.parse_args()

# load configuration from config.py
# TODO: implement this

# check if Pytest path exists
if not os.path.exists(args.pytest_path):
    print(f"Error: Path to Pytest files {args.pytest_path} does not exist.")
    exit()

# generate unit test
unit_test = unit_test_from_function(args.function)

# prompt user to accept or reject the unit test
if not args.auto_accept:
    print("Generated unit test:")
    print(unit_test)
    user_input = input("Accept generated unit test? (y/n): ")
    if user_input.lower() != 'y':
        exit()

# write the unit test to file
filename = args.function.replace('.', '_') + '_test.py'
filepath = os.path.join(args.pytest_path, filename)
with open(filepath, 'w') as f:
    f.write(unit_test)

print(f"Unit test written to {filepath}.")