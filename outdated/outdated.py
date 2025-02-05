months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:

            item = input("Enter date: ").strip()
            if "/" in item:
                month, day, year = item.split("/")
                if check_data(int(month), int(day)):
                    print(f"{int(year)}-{int(month):02}-{int(day):02}")
                    break
            elif "," in item:
                item = item.replace(",","")
                month, day, year = item.split(" ")
                month_as_number = months.index(month.title()) + 1
                if check_data(int(month_as_number), int(day)):
                    print(f"{int(year)}-{month_as_number:02}-{int(day):02}")
                    break
            else:
                pass

        except ValueError:
            pass



def check_data(month, day):
    if month < 13 and month > 0 and day < 32:
        return True
    return False

main()