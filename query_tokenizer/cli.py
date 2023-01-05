import argparse
from query_tokenizer.string_tokenizer import tokenize
from pprint import pprint
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("sentence", nargs="+")
    return parser.parse_args()


def main():
    args = parse_args()
    for sentence in args.sentence:
        print(tokenize(sentence))


if __name__ == "__main__":
    main()
