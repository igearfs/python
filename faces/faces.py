smile_image = "🙂"
frown_image = "🙁"

smile = ":)"
frown = ":("

def main():
    print(convert(input("Enter Data:")))

def convert(input):
    input = input.replace(smile, smile_image)
    input = input.replace(frown, frown_image)
    return input

main()