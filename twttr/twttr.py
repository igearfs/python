vowels = ["a","e","i","o","u"]

def main():
    print("Output: " + camel_to_snake(input("Input: ").strip()))


def camel_to_snake(answer):
    camel_string = "";
    for letter in answer:
        if letter.lower() not in vowels:
            camel_string += letter
    return camel_string

main()