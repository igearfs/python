import requests
import sys as System

def main():
    argv_len = len(System.argv)
    if(argv_len == 1):
        print("Missing command-line argument")

    try:
        argument = float(System.argv[1])
        current_price = float(requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()['bpi']['USD']['rate'].replace(",",""))
        amount = argument * current_price

        print(f"${amount:,.4f}")
    except ValueError:
        print("Command-line argument is not a number")
        System.exit(1)
if __name__ == "__main__":
    main()