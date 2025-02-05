from datetime import date
import inflect
import sys

p = inflect.engine()

def main():
    birth_entered = input("Date of Birth: ")
    print(calculate_days(birth_entered))

def calculate_days(birth_entered):
    try:
        if "-" in birth_entered and len(birth_entered.split("-")) == 3:
            birth_year, birth_month, birth_day = birth_entered.split("-")
            today_date = date.today()
            birth_date = date(int(birth_year), int(birth_month), int(birth_day))
            daysDiff = today_date - birth_date
            diffMinutes = daysDiff.days * 24 * 60
            return p.number_to_words(diffMinutes, andword="").capitalize() + " minutes"

        else:
            sys.exit(1)
    except ValueError:
        sys.exit(1)
        
if __name__ == "__main__":
    main()