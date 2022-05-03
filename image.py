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

  print("original_height: " + str(original_height) + " original_width: " + str(original_width))
  print("target_height: " + str(target_height) + " target_width: " + str(target_width))

  return cv2.resize(image, (target_width, target_height))


image = cv2.imread(image_path)

print_image(image)
image_resized = resize(image)
print_image(image_resized)
