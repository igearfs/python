import sys

def main():
    check_valid_sys_args(sys.argv)
    print(count_lines(sys.argv[1]))

def check_valid_sys_args(argsv):
    command_length = len(argsv)

    if command_length < 2:
        sys.exit("Too few command-line arguments")

    elif command_length > 2:
        sys.exit("Too many command-line arguments")

    elif not (sys.argv[1].endswith(".py")):
        sys.exit("Not a Python file")

def count_lines(file_name):
    count = 0
    try:
        with open(file_name, 'r', encoding='utf-8') as pyfile:
            for line in pyfile:
                line = line.strip()
                if line.startswith('#') or len(line.strip()) == 0:
                    pass
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    return count


if __name__ == "__main__":
    main()