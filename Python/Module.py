import time
from time import sleep
import sys

print(time.asctime())
print(time.timezone)
sleep(3)
print(time.asctime())


for path in sys.path:
    print(path)


