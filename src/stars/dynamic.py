import time
import read
import write

stream = read("master")
notes = write("conditional")

while True:
    line = next(stream)
    notes += line
    if notes["break"] == True:
        break
    else:
        interval = notes["sleep"]
        time.sleep(interval)

[see dynamic @ dynamic.py]
