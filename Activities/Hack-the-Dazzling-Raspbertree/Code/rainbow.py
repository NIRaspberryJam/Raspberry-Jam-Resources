import colorsys
from time import sleep
import network

led = 8
tree_ip = "10.83.3.129"
network.call(tree_ip)

while True:
    for x in range(0, 100):
        r, g, b = colorsys.hsv_to_rgb(x / 100.0, 1.0, 1.0)
        r = int(r * 100)
        g = int(g * 100)
        b = int(b * 100)
        message = (led, r, g, b)
        message = str(message)
        network.say(message)
        print(message)
        sleep(0.05)
