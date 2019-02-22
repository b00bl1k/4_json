import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding="utf8") as file_handler:
        return json.load(file_handler)


def pretty_print_json(obj):
    print(json.dumps(obj, indent=4))


def main():
    try:
        path = sys.argv[1]
        pretty_print_json(load_data(path))
    except FileNotFoundError:
        sys.exit("File '{}' not found".format(path))
    except json.JSONDecodeError:
        sys.exit("Invalid file '{}'".format(path))
    except IndexError:
        sys.exit("Invalid command line arguments")


if __name__ == '__main__':
    main()
