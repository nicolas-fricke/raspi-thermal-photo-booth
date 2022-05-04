import time
from escpos.printer import Serial, Dummy


def print_image(image_path, device_path):
    p = Serial(devfile=device_path,
               baudrate=9600,
               bytesize=8,
               parity='N',
               stopbits=1,
               timeout=0.05,
               dsrdtr=False)

    # The documentation recommended to first output the image to a
    # dummy printer to improve print speed & quality and then feed
    # the raw data to the serial printer port
    d = Dummy()

    d.image(image_path, impl="bitImageColumn")
    d.print_and_feed(5)  # Push the paper out

    p._raw(d.output)
    time.sleep(10)  # To ensure the print job is done before quitting
    p.close()
