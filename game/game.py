import inflect
import random
import sys

inflect_engine = inflect.engine()

name_list = []


def main():
    item = 0

    while item <= 0:
        try:
            item = int(input("Level: ").strip())
        except ValueError:
            pass

    if item > 0:
        answer = random.randrange(item)
        if int(answer) == 0:
            answer = 1

        while True:
            try:
                guess = int(input("Guess: ").strip())
                if guess == answer:
                    print("Just Right!")
                    sys.exit(0)
                elif guess > answer:
                    print("Too large!")
                else:
                    print("Too small!")

            except ValueError:
                pass


main()
