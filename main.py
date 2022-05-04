import sys
from image import load_resize_and_save
from printer import print_image


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Please provide the path to the image to print")
        sys.exit(1)

    image_path = sys.argv[1]

    print("Resizing " + image_path)
    resized_image_path = load_resize_and_save(image_path)
    print("Saved resized image to " + resized_image_path)

    print("Printing " + resized_image_path)

    print_image(resized_image_path, "/dev/cu.usbserial-0001")

    print("Done.")
