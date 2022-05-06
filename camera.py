import time
import os
from picamera import PiCamera, mmal
import ctypes

# The camera used here turns out to be the NoIR camera. This one
# has a very pink-ish tint during daytime. There's a new "greyworld"
# auto-white-balance mode in the camera's firmware to correct for
# this, but it's not yet supported by the picamera library. Therefore,
# extend the library to add this AWB mode. For more info see:
# https://github.com/raspberrypi/firmware/issues/1167#issuecomment-511798033
class PiCamera2(PiCamera):
    AWB_MODES = {
        'off':           mmal.MMAL_PARAM_AWBMODE_OFF,
        'auto':          mmal.MMAL_PARAM_AWBMODE_AUTO,
        'sunlight':      mmal.MMAL_PARAM_AWBMODE_SUNLIGHT,
        'cloudy':        mmal.MMAL_PARAM_AWBMODE_CLOUDY,
        'shade':         mmal.MMAL_PARAM_AWBMODE_SHADE,
        'tungsten':      mmal.MMAL_PARAM_AWBMODE_TUNGSTEN,
        'fluorescent':   mmal.MMAL_PARAM_AWBMODE_FLUORESCENT,
        'incandescent':  mmal.MMAL_PARAM_AWBMODE_INCANDESCENT,
        'flash':         mmal.MMAL_PARAM_AWBMODE_FLASH,
        'horizon':       mmal.MMAL_PARAM_AWBMODE_HORIZON,
        'greyworld':     ctypes.c_uint32(10)
        }

camera = PiCamera2()
camera.resolution = (1640, 1232)
camera.framerate = 10
camera.contrast = 80
camera.brightness = 70
camera.awb_mode = "greyworld"

def take_picture():
    # To ensure the camera has enough time to adjust
    # to brightness - and give the user a moment to
    # prepare for the picture to be taken :)
    time.sleep(2)

    os.makedirs("./tmp", exist_ok=True)
    file_path = "./tmp/photo.png"

    camera.capture(file_path)
    return file_path


if __name__ == '__main__':
    print("Taking a picture...")
    picture_path = take_picture()
    print("Picture taken! Saved as " + picture_path)

    # print("Taking a second picture...")
    # picture_path = take_picture()
    # print("Picture taken again! Saved as " + picture_path)
