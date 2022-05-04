from camera import take_picture
from image import load_resize_and_save
from printer import print_image


if __name__ == '__main__':
    print("Taking a picture...")
    image_path = take_picture()
    print("Done, saved as " + image_path)

    print("Resizing " + image_path)
    resized_image_path = load_resize_and_save(image_path)
    print("Saved resized image to " + resized_image_path)

    print("Printing " + resized_image_path)

    print_image(resized_image_path, "/dev/serial0")

    print("Done.")
