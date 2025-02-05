import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    compiled_re = re.compile(r"(https*:\/\/w*w*w*\.*youtube\.com\/embed\/[a-zA-Z0-9]*)")
    full_url = compiled_re.search(s)
    if full_url and "iframe" in s.lower():
        compiled_re = re.compile(r"(https*:\/\/w*w*w*\.*youtube\.com\/embed\/*)")
        up_to_embed_url = compiled_re.search(full_url[0])
        embed = full_url[0][up_to_embed_url.span()[1]::]
        return f"https://youtu.be/{embed}"
    else:
        return "None"
...


if __name__ == "__main__":
    main()