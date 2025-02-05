from validator_collection import checkers

def main():
    print(check_email(input("What's your email address? ").strip()))

def check_email(email):
    is_email_valid = checkers.is_email(email)

    if is_email_valid:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()