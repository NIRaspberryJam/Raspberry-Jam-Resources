from twython import Twython
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
# Imports keys from auth.py
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Says to use the keys with Twython and refer to it as "twitter"
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

# Sets Pin number, GPIO mode and set as input
PIR = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR, GPIO.IN)

# sets message as what is in "Brackets"
message = "Hello world!"

# makes camera refer to PiCamera()
camera = PiCamera()

# Constant Loop
while True:
    # When Movement is sensed
    if GPIO.input(PIR):
        # Set timestamp to be current time
        timestamp = datetime.now().isoformat()
        # Sets path for photo to be saves to and sets the file name to the timestamp
        photo_path = '/home/pi/tweeter/%s.jpg' % timestamp
        sleep(3)
        # Take a picture to the path previously specified
        camera.capture(photo_path)

        # Then start the next part with Photo referring to the picture just taken
        with open(photo_path, 'rb') as photo:
            # makes response mean upload the picture taken
            response = twitter.upload_media(media=photo)
            # Sends tweet to twitter with image
            twitter.update_status(status=message, media_ids=[response['media_id']])
            # Print that the image is tweeted
            print("just tweeted", message, "with the image", photo_path)
            # exits script
            exit()
