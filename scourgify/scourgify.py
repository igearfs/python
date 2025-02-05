import sys
import csv
import tabulate

def main():
    check_valid_sys_args(sys.argv)
    print_menu(sys.argv[1], sys.argv[2])

def check_valid_sys_args(argsv):
    command_length = len(argsv)

    if command_length < 3:
        sys.exit("Too few command-line arguments")

    elif command_length > 3:
        sys.exit("Too many command-line arguments")

    elif not (sys.argv[1].endswith(".csv")):
        sys.exit("Not a CSV file")

def print_menu(in_file, out_file):

    try:
        with open(in_file, 'r', encoding='utf-8') as input:
            reader = csv.DictReader(input)
            dict_list = []
            for x in reader:
                lName, fName  = x['name'].split(",")
                dict_list.append({"first" : fName.strip(), "last" : lName.strip(), "house" : x['house']})
        with open(out_file, 'w', encoding='utf-8') as output:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            for d in dict_list:
                writer.writerow(d)

    except FileNotFoundError:
        sys.exit(f"Could not read {in_file}")


if __name__ == "__main__":
    main()