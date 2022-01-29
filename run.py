import argparse
from validator.validator import Validator


def run():
    """
    Run the validator pipeline based on command line parameters.
    """
    parser = argparse.ArgumentParser(description='Run the validator pipeline')
    parser.add_argument('--file', dest='file', help='The CSV file to validate')
    args = parser.parse_args()
    validator = Validator()
    validator.load(args.file)
    validator.validate()

if __name__ == "__main__":
    run()
