def main():
    answer = input("Expression: ").strip()
    answer = calculate(answer)
    print("{:.1f}".format(answer))


def calculate(answer):
    return eval(answer)

main()
