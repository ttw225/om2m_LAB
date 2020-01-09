#!/usr/bin/python

import os
import time
import requests
import logging
import json
from dotenv import load_dotenv
import RPi.GPIO as GPIO


load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] - %(asctime)s\n%(message)s\n' + ('-' * 70),
    datefmt='%Y-%m-%dT%H:%M:%S',
)


class MotionDetect():
    def __init__(self, pir, light):
        self.pir = pir
        self.light = light
        self.mode = 'default'
        self.action = {
            'class_over': self.class_over_mode,
            'in_class': self.in_class_mode,
            'movie_time': self.movie_time_mode,
        }
        self.lock_header = {
            'Authorization': os.environ.get('KEY'),
            'Content-Type': 'application/json'
        }
        self.lock_target = os.environ.get('URL')
        self.lock_map = {
            True: 'lock',
            False: 'unlock'
        }
        self.light_header = {
            'Content-Type': 'application/json'
        }
        self.light_target = os.environ.get('LIGHT_URL')
        self.light_map = {
            True: 'true',
            False: 'false'
        }
        self.detect()

    def detect(self):
        # Calculate numbers of motion
        counter_motion = 0
        counter_nobody = 0
        try:
            while True:
                # Detected if pir is high
                if GPIO.input(self.pir) == True:
                    logging.info("Motion Detected!")
                    counter_motion += 1
                    counter_nobody = 0
                else:
                    logging.info("Nobody...")
                    counter_motion = 0
                    counter_nobody += 1
                logging.info(f"Detect count: {counter_motion}\nNobody count: {counter_nobody}")

                if counter_motion >= 2:
                    # In Class mode
                    if self.mode != 'in_class':
                        self.mode = 'in_class'
                        self.action[self.mode]()
                    # Reset Counter
                    counter_motion = 0
                    counter_nobody = 0

                elif counter_nobody >= 10:
                    # Class Over mode
                    if self.mode != 'class_over':
                        self.mode = 'class_over'
                        self.action[self.mode]()
                    # Reset Counter
                    counter_motion = 0
                    counter_nobody = 0

                if GPIO.input(self.light) == True:
                    # Movie mode
                    if self.mode != 'movie_time':
                        self.mode = 'movie_time'
                        self.action[self.mode]()

                time.sleep(1)

        except KeyboardInterrupt:
            pass

        finally:
            GPIO.cleanup() #reset all GPIO
            logging.info("Program ended")

    def in_class_mode(self):
        logging.info("In Class Mode")
        self.light_control(True)
        self.lock_control(False)

    def class_over_mode(self):
        logging.info("Class Over Mode")
        self.light_control(False)
        self.lock_control(True)

    def movie_time_mode(self):
        logging.info("Movie Time Mode")
        self.light_control(False)

    def light_control(self, signal):
        logging.info(f"Light Control: {signal}")
        message = f'{{\"on\":{self.light_map[signal]}}}'
        res = requests.request("PUT", self.light_target, headers=self.light_header, data=message)
        logging.info(f" - Light Control Response: {res.text}")

    def lock_control(self, signal):
        logging.info(f"Lock Control: {signal}")
        message = f'{{\"command\":\"{self.lock_map[signal]}\"}}'
        res = requests.request("POST", self.lock_target, headers=self.lock_header, data=message)
        logging.info(f" - Lock Control Response: {res.text}")


def main():
    # Assign pins
    pir = int(os.environ.get('PIR_PIN', '8'))
    light = int(os.environ.get('LIGHT_PIN', '7'))
    # Set GPIO to pin numbering
    GPIO.setmode(GPIO.BOARD)
    # Setup GPIO pin PIR as input
    GPIO.setup(pir, GPIO.IN)
    GPIO.setup(light, GPIO.IN)
    logging.info(f"PIR Sensor initializing on pin {pir}")
    logging.info(f"Light Sensor initializing on pin {light}")
    # Start up sensor
    time.sleep(2)
    logging.info("Active")
    logging.info("Press Ctrl+c to end program")
    MotionDetect(pir, light)


if __name__ == "__main__":
    main()
