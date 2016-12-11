import network

tree_ip = "10.83.3.160"
network.call(tree_ip)

for X in range(1, 4):
    message = (X, 255, 255, 255)
    message = str(message)
    network.say(message)
