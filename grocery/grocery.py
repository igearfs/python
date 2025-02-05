grocery_list = {}

def main():
     while True:
        try:
            item = input().strip().upper()
            add_item(item)
        except EOFError:
            sorted_grocery_list = list(grocery_list.keys())
            sorted_grocery_list.sort()
            print()
            for i in sorted_grocery_list:
                print(grocery_list[i], i)
            break


def add_item(item):
    try:
        count = grocery_list[item]
        count = int(count) + 1
        grocery_list[item] = count
    except KeyError:
        grocery_list[item] = 1

main()