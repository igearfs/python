vowels =  ['a','A', 'e','E', 'i','I', 'o','O', 'u','U']

def main():
    print("Output: " + shorten(input("Input: ").strip()))


def shorten(answer):
    replaced_string = "";
    for letter in answer:
        if letter not in vowels:
            replaced_string += letter
    return replaced_string


if __name__ == "__main__":
    main()