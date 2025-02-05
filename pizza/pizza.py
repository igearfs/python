import sys
import csv
import tabulate

def main():
    check_valid_sys_args(sys.argv)
    print_menu(sys.argv[1])

def check_valid_sys_args(argsv):
    command_length = len(argsv)

    if command_length < 2:
        sys.exit("Too few command-line arguments")

    elif command_length > 2:
        sys.exit("Too many command-line arguments")

    elif not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a Python file")

def print_menu(file_name):

    try:
        with open(file_name, 'r', encoding='utf-8') as pyfile:
            reader = csv.reader(pyfile)
            headers = next(reader)
            print(tabulate.tabulate(reader, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()