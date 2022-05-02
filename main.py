from argparse import ArgumentError
import sys
from escpos.printer import Serial

if (len(sys.argv) != 2):
    print("Please provide the path to the image to print")
    sys.exit(1)

image_path = sys.argv[1]
print("Printing " + image_path)

p = Serial(devfile='/dev/cu.usbserial-0001',
           baudrate=9600,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=0.05,
           dsrdtr=False)


p.text("This is my image " + image_path + ":\n")
p.image(image_path, impl="bitImageColumn")
p.text("\n\n\n\n\n") # Push the paper out
