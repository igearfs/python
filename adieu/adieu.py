import inflect

inflect_engine = inflect.engine()

name_list = []

def main():
     while True:
        try:
            item = input("Name: ").strip()
            name_list.append(item)
        except EOFError:
            print()
            print("Adieu, adieu, to " + inflect_engine.join(name_list))
            break

main()