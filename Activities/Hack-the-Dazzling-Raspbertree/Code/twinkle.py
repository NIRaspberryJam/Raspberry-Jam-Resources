from time import sleep
import network
import random

tree_ip = "1.1.1.1"
network.call(tree_ip)
message = "1,255,255,255"
off = "1,0,0,0"

while True:
    time = random.randint(1, 5)
    network.say(message)
    sleep(0.5)
    network.say(off)
    sleep(time)

