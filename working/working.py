import re
import sys
time_dict = {
    "1 AM" : "01",
    "2 AM" : "02",
    "3 AM" : "03",
    "4 AM" : "04",
    "5 AM" : "05",
    "6 AM" : "06",
    "7 AM" : "07",
    "8 AM" : "08",
    "9 AM" : "09",
    "10 AM" : "10",
    "11 AM" : "11",
    "12 PM" : "12",
    "1 PM" : "13",
    "2 PM" : "14",
    "3 PM" : "15",
    "4 PM" : "16",
    "5 PM" : "17",
    "6 PM" : "18",
    "7 PM" : "19",
    "8 PM" : "20",
    "9 PM" : "21",
    "10 PM" : "22",
    "11 PM" : "23",
    "12 AM" : "00"
}

def main():
    print(convert(input("Hours: ")))


def convert(s):

    if "to" not in s:
        raise ValueError
    
    start_time = ""
    end_time = ""
    try:
        match = re.search(r"((1[0-2]|0?[1-9]):[0-5][0-9]\s[AP]M)|((1[0-2]|0?[1-9])\s[AP]M)", s, )
        count = 0
        while match:
            if count == 0:
                start_time = fix_time(match.group(0))
                s = s.replace(match.group(0), start_time)
                count += 1
            elif count == 1:
                end_time = fix_time(match.group(0))
                s = s.replace(match.group(0), end_time)
                count += 1
            elif count > 1:
                break;
            match = re.search(r"((1[0-2]|0?[1-9]):[0-5][0-9]\s[AP]M)|((1[0-2]|0?[1-9])\s[AP]M)", s)
        if count < 2:
            raise ValueError

    except KeyError:
        raise ValueError

    if start_time and end_time:
        return s
    else:
        raise ValueError

def fix_time(time):
    if ":" in time:
        number_time, end_time = time.split(":")
        minutes, meridian = end_time.split(" ")
        key = f"{number_time} {meridian}"

        return f"{time_dict[key]}:{minutes}"
    else:
        return f"{time_dict[time]}:00"

if __name__ == "__main__":
    main()