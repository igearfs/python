import sys
from PIL import Image
from PIL import ImageOps

def main():
    check_valid_sys_args(sys.argv)
    overlay_image(sys.argv[1], sys.argv[2])

def check_valid_sys_args(argsv):
    command_length = len(argsv)

    if command_length < 3:
        sys.exit("Too few command-line arguments")

    elif command_length > 3:
        sys.exit("Too many command-line arguments")

    elif not (sys.argv[1].endswith(".jpg")):
        sys.exit("Invalid output")

    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")

def overlay_image(in_file, out_file):

    try:
        input_shirt = Image.open(in_file)

        overlay_image = Image.open("shirt.png")

        size = overlay_image.size

        input_shirt = ImageOps.fit(input_shirt, size)
        input_shirt.paste(overlay_image, overlay_image)

        input_shirt.save(out_file)

    except FileNotFoundError:
        sys.exit(f"Could not read {in_file}")


if __name__ == "__main__":
    main()