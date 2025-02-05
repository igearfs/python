def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # Takes care of lenght to start off with
    if len(s) < 2 or len(s) > 7:
        return False

    for letter in s:
        if not letter.isalnum():
            return False
     # no characters that are not alpha/numeric
    if s.isnumeric():
        return False

    if s.isalpha():
        return True

    if s[0].isnumeric() or s[1].isnumeric():
        return False

    # All vanity plates must start with at least two letters
    if s[0].isalpha() and s[1].isalpha():
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

if __name__ == "__main__":
    main()