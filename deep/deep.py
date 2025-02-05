def main():
    print(is_Meaning_Of_Life(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()))


def is_Meaning_Of_Life(answer):
    match answer.lower():
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()