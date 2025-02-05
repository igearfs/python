accepted_amounts = [1,5,10,25,50]

def main():
    amount_due = 50

    while amount_due > 0:
        print("Amount Due:", amount_due)
        if(int(amount_due) > 0):
            amount_inserted = input("Insert Coin: ").strip();
            if int(amount_inserted) in accepted_amounts:
                amount_due = calculate_change(amount_inserted, amount_due)

    print("Change Owed:", (amount_due * -1))


def calculate_change(answer, amount_due):
    return amount_due - int(answer)

main()