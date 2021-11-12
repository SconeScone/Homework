import datetime
import time
from special_dots import dots
f = open("input.txt", "r")
r = int(f.readline())
center = list(map(int, f.read().split()))
f.close()
x0 = center[0]
y0 = center[1]
f = open("output.txt", "a")
f.write(str(datetime.datetime.now()) + "\n")
f.write(str(dots(r, x0, y0)) + "\n")
f.write(str(time.clock()))
f.close()
