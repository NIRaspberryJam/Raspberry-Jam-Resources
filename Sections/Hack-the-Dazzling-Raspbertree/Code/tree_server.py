"""
Simple server for the Hack the Dazzling Raspbertree activity from Northern Ireland Raspberry Jam
Written by Andrew Mulholland (@gbaman1)
Written for Python 3

"""

import socket
import sys
import threading
from neopixel import *
from ast import literal_eval as make_tuple
import time

OFFSET = 70 # Pixels in the strip to ignore (if using all the pixels, set to 0)


# LED strip configuration:
LED_COUNT = 400  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)

pixel_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
pixel_strip.begin()
pixel_strip.show()


class NeopixelUpdater(threading.Thread):
    """
    The updater that runs in a background thread, every 0.2 seconds reducing the brightness of every pixel.
    Is included to decrease power usage over time.
    """
    def __init__(self):
        super(NeopixelUpdater, self).__init__()

    def run(self):
        while True:
            for LED in range(0, LED_COUNT):

                p = pixel_strip.getPixelColorRGB(LED + 70)
                r = p.r
                g = p.g
                b = p.b
                if r > 0 or g > 0 or b > 0:
                    r = max(0, r - 3)
                    g = max(0, g - 3)
                    b = max(0, b - 3)
                pixel_strip.setPixelColorRGB(LED + 70, r , g, b)
            pixel_strip.show()
            time.sleep(0.2)


class NeopixelConnection(threading.Thread):
    """
    Thread to handle each connection from a Pi
    """
    conn = None

    def __init__(self, conn):
        super(NeopixelConnection, self).__init__()
        self.conn = conn

    def run(self):
        self.client_thread()

    def client_thread(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            parse_pixel_data(data.decode('ascii'))

        self.conn.close()


def parse_single_pixel(pixel_data):
    try:
        rgb = pixel_data[1:4]
        for colour in rgb:
            colour = int(colour)
            if colour > 256 or colour < 0:
                raise Exception("Colour value {} is greater than 256 or less than 0!".format(colour))
        pixel_strip.setPixelColorRGB(int(pixel_data[0]) + OFFSET, pixel_data[1], pixel_data[2], pixel_data[3])
        pixel_strip.show()
    except:
        print("Message ignored '{}'".format(pixel_data))


def parse_pixel_data(data):
    try:
        data = str(data).strip()
        if data.count("[") > 1:
            split_data = data[1:len(data)].split("][")
            for pixel in split_data:
                pixel = ("[{}]".format(pixel)).replace("]]", "]")
                parse_pixel_data(make_tuple(pixel))
        else:
            parse_single_pixel(make_tuple(data))
    except:
        print("Message ignored '{}'".format(data))


def setup_server():
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = 8888  # Arbitrary non-privileged port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    # Bind socket to local host and port
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print('Socket bind complete')

    # Start listening on socket
    s.listen(10)
    print('Socket now listening')
    worker_threads = []
    updater = NeopixelUpdater()
    updater.daemon = True
    updater.start()

    while 1:
        # wait to accept a connection - blocking call
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        # Start new worker thread
        new_thread = NeopixelConnection(conn)
        new_thread.daemon = True
        new_thread.start()
        worker_threads.append(new_thread)

    s.close()


setup_server()
