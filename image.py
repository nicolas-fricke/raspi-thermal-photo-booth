import cv2
import sys
import os


def load_image(image_path):
    return cv2.imread(image_path)


def print_image(image):
    cv2.imshow("whatever", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(image):
    original_width = image.shape[0]
    original_height = image.shape[1]

    target_width = 383
    target_height = int((original_width / original_height) * target_width)

    return cv2.resize(image, (target_width, target_height))


def save_image(image):
    os.makedirs("./tmp", exist_ok=True)
    file_path = "./tmp/image.png"
    cv2.imwrite(file_path, image)

    return file_path


if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Please provide the path to the image to print")
        sys.exit(1)

    image_path = sys.argv[1]
    print("Resizing " + image_path)

    image = load_image(image_path)

    print_image(image)
    image_resized = resize(image)
    print_image(image_resized)
    print("Resized image saved to: " + save_image(image_resized))
