import RPi.GPIO as GPIO
from SensorInterface import SensorInterface
from threading import Thread
from time import sleep
from State import State

class SW420(Thread, SensorInterface):

    def __init__(self, channel):
        super(SW420, self).__init__()
        super().setDaemon(True)
        self.stop_thread = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.IN)
        home = self # Is this necessary in python vs JS?
        def callback(channel):
            home.next_state = State.RUNNING

        GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=200)
        GPIO.add_event_callback(channel, callback)

        self.state = State.STOPPED
        self.next_state = State.STOPPED

    def run(self):
        while True:
            # Essentially a 1 second buffer on callback inputs
            if self.stop_thread:
                break
            self.state = self.next_state
            self.next_state = State.STOPPED
            sleep(1)

    def get_state(self):
        return self.state

    def stop(self):
        self.stop_thread = True