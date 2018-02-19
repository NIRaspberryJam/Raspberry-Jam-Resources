import serial
import scratch

scr = scratch.Scratch()
## THE NEXT LINE MIGHT NEED TO BE CHANGED - TYPE ls /dev/ttyA* into the terminal to see which port is needed.
PORT = "/dev/tty.usbmodem1412"
##
BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
    data = s.readline().decode('UTF-8')
    data_list = data.rstrip().split(' ')
    try:
        x, y, z, a, b = data_list
        scr.sensorupdate({'x' : x})
        scr.sensorupdate({'y' : y})
        scr.sensorupdate({'z' : z})
        scr.sensorupdate({'a' : a})
        scr.sensorupdate({'b' : b})

    except:
        pass

s.close()