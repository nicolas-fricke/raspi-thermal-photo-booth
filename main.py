import sys
import os
import time
from escpos.printer import Serial, Dummy

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

d = Dummy()

d.text("This is my image " + image_path + ":\n")
d.image(image_path, impl="bitImageColumn")
d.print_and_feed(5) # Push the paper out

os.makedirs("./tmp", exist_ok=True)
with open("./tmp/output", "wb") as f:
    f.write(d.output)
    print("Dumped output to ./tmp/output")

print("Printing...")

p._raw(d.output)

time.sleep(10) # To ensure the print job is done
