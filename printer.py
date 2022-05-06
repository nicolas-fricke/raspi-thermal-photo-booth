import time
from escpos.printer import Serial


def print_image(image_path, device_path):
    p = Serial(devfile=device_path,
               baudrate=9600,
               bytesize=8,
               parity='N',
               stopbits=1,
               timeout=0.05,
               dsrdtr=False)

    p.image(image_path, impl="bitImageColumn")
    # p._raw(d.output)
    time.sleep(1)  # To ensure the print job is done before quitting
    p.print_and_feed(3)  # Push the paper out
    time.sleep(1)  # To ensure the print job is done before quitting
    p.close()
