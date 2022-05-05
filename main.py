from camera import take_picture
from image import load_resize_and_save
from printer import print_image
from gpiozero import Button
from signal import pause


def take_and_print_a_picture():
    print("Taking a picture...")
    image_path = take_picture()
    print("Done, saved as " + image_path)

    print("Resizing " + image_path)
    resized_image_path = load_resize_and_save(image_path)
    print("Saved resized image to " + resized_image_path)

    print("Printing " + resized_image_path)

    print_image(resized_image_path, "/dev/serial0")

    print("Done. Wanna go again? Press the button...")


if __name__ == '__main__':
    print("The photo booth is ready!")
    print("Press the button when you're, too...")

    shutter_button = Button(18)
    shutter_button.when_pressed = take_and_print_a_picture

    # Using signal's pause method to put the script in a
    # waiting loop handling button presses whenever they
    # come:
    pause()
