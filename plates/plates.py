def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
#        vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
def is_valid(s):

    # Takes care of lenght to start off with
    if len(s) < 2 or len(s) > 7:
        return False

     # no characters that are not alpha/numeric
    if not s.isalnum():
        return False

    # All vanity plates must start with at least two letters
    elif s[0].isalpha() and s[1].isalpha():
        first_number_found = False

        # now check every letter
        for letter in s:
            if letter.isnumeric() and not first_number_found:
                first_number_found = True
                if int(letter) == 0:
                    return False
            #If we find a numeric and the last letter is not numeric then not valid
            elif letter.isnumeric() and s[len(s)-1].isalpha():
                return False
            # if a number was found then no alphas can be after it
            if first_number_found and letter.isalpha():
                return False
    # We made it past all checks good to go
    return True

main()