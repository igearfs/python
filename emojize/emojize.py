import emoji

input = input("Input: ").strip()

print("Output: " + emoji.emojize(input, language='alias'))
