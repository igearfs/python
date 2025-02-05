import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
        match exact between the b zero to three numbers

        First 3 numbers followed by a dot repeats {3} times
        \\b(([0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0[0-9][0-9]|0[0-9]|0)\\.{3}\\b

        last 3 numbers no dot
        \\b([0-9]{2}||1[0-9]{2}|2[0-4][0-9]|25[0-5]|0[0-9]{2}|0[0-9]|0)\\b

        001.001.001.001
        01.01.01.01
        0.0.0.0
        255.255.255.255

    """
    valid = False

    if(len(ip.strip().split('.')) == 4):
        compiled_re = re.compile(r"\b(?:(([0-9]{2}|1[0-9]{2}|2[0-4][0-9]|25[0-5]|0[0-9][0-9]|0[0-9]|0)\.)){3}\b\b([0-9]{2}||1[0-9]{2}|2[0-4][0-9]|25[0-5]|0[0-9]{2}|0[0-9]|0)\b")
        valid = compiled_re.search(ip)

    if valid:
        return True
    else:
        return False


if __name__ == "__main__":
    main()