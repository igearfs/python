def main():
    while True:
        try:
            fuel_gague_input = input("Fraction: ")

        except (ValueError, NameError, ZeroDivisionError) as e:
            print(e)

def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    check(numerator, denominator)
    fuel_gague_input = int(round( ((numerator / denominator) * 100), 0))
    return fuel_gague_input

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return "{0}%".format(percentage)

def check(numerator, denominator):
    if denominator == 0:
        raise ZeroDivisionError
    if numerator > denominator:
        raise ValueError

if __name__ == "__main__":
    main()