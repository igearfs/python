# Prompts the user for a level,. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number),
#     the program should output EEE and prompt the user again,
#     allowing the user up to three tries in total for that problem.
#     If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.

import random


def main():
    answered_correctly = 0
    level = get_level()
    question_count = 0
    while question_count < 10:
        x = generate_integer(level)
        y = generate_integer(level)

        answer_count = 0
        answer = x + y
        while answer_count < 3:
            print(f"{x} + {y} = ", end = "")
            p = int(input())
            if p == answer:
                answered_correctly += 1
                break
            else:
                answer_count = answer_count + 1
                print("EEE")

        if answer_count == 3:
            print(f"{x} + {y} = {answer}")

        question_count = question_count + 1
        
    print(f"Score: {answered_correctly}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass

def generate_integer(level):

    lower_limit = 0
    upper_limit = 9

    if level == 2:
        lower_limit = 10
        upper_limit = 99
    elif level == 3:
        lower_limit = 100
        upper_limit = 999

    return random.randint(lower_limit, upper_limit)

if __name__ == "__main__":
    main()