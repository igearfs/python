def main():
    print(process_Greeting(input("Greeting: ").strip().lower()))


def process_Greeting(answer):
    answer = answer.replace(",", "")
    if answer.split(" ")[0] == "hello":
        return "$0"
    elif answer[0] == "h":
        return "$20"
    else:
        return "$100"


main()