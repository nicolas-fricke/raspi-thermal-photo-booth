import cv2
import sys

if (len(sys.argv) != 2):
    print("Please provide the path to the image to print")
    sys.exit(1)

image_path = sys.argv[1]
print("Resizing " + image_path)


def print_image(image):
    cv2.imshow("whatever", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize(image):
    original_width = image.shape[0]
    original_height = image.shape[1]

    target_width = 383
    target_height = int((original_width / original_height) * target_width)

    print("original_height: " + str(original_height) +
          " original_width: " + str(original_width))
    print("target_height: " + str(target_height) +
          " target_width: " + str(target_width))

    return cv2.resize(image, (target_width, target_height))


def face_detection(image):
    face_cascade = cv2.CascadeClassifier('cascade.xml')
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    return image


image = cv2.imread(image_path)

# print_image(image)
print_image(face_detection(image))
# image_resized = resize(image)
# print_image(image_resized)
