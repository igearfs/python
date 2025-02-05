def main():
    print("snake_case: " + camel_to_snake(input("camelCase: ").strip()))


def camel_to_snake(answer):
    camel_string = "";
    for letter in answer:
        if letter.isupper():
            camel_string += "_"
            camel_string += letter.lower()
        else:
            camel_string += letter
    return camel_string

main()