#prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer
mass = 300000000
def main():
    print(convert(input("Enter mass(in kilograms): ")))

def convert(input):
   return int(input) * mass ** 2

main()