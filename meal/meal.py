def main():
    time = convert(input("What time is it? ").strip())

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")

def convert(time):
    hour, min = time.split(":")

    minute_as_decimal = float("{:.2f}".format((int(min)/60)))
    return float(hour) + minute_as_decimal


if __name__ == "__main__":
    main()