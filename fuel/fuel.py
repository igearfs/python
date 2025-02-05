def main():
    while True:
        try:
            fuel_gague_input = input("Fraction: ")
            numerator, denominator = fuel_gague_input.split("/")
            numerator = int(numerator)
            denominator = int(denominator)

            #If, though, X or Y is not an integer, X is greater than Y, or Y is 0, i
            good_data = check(numerator, denominator)
            if good_data:
                fuel_gague_input = int(round( ((numerator / denominator) * 100), 0))
                if fuel_gague_input <= 1:
                    print("E")
                elif fuel_gague_input >= 99:
                    print("F")
                else:
                    print(f"{fuel_gague_input}%")
                break
        except (ValueError, NameError, ZeroDivisionError) as e:
            print(e)

def check(numerator, denominator):
    is_denom_good = denominator != 0
    is_num_good = numerator <= denominator
    return is_denom_good and is_num_good

main()