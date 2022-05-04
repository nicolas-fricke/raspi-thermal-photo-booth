from picamera import PiCamera
import time
import os


def take_picture():
    camera = PiCamera()
    camera.resolution = (1280, 720)
    camera.vflip = True
    camera.contrast = 10
    time.sleep(2)

    os.makedirs("./tmp", exist_ok=True)
    file_path = "./tmp/photo.png"

    camera.capture(file_path)
    return file_path


if __name__ == '__main__':
    print("Taking a picture...")
    picture_path = take_picture()
    print("Picture taken! Saved as " + picture_path)
