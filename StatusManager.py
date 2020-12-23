from threading import Thread
from time import sleep
from MockSensor import MockSensor
from State import State
import random

# This doesn't belong in this class but I don't want to give an enum a method
def get_alt_state(state):
    return State.INACTIVE if state == State.ACTIVE else State.ACTIVE

class StatusManager(Thread):

    def __init__(self):
        super(StatusManager, self).__init__()
        super().setDaemon(True)
        self.stop_thread = False
        self.current_state = State.INACTIVE
        self.activity_threshold = 30
        self.timings = {
            State.ACTIVE: 0,
            State.INACTIVE: 0
        }
        self.sensor = MockSensor()

    def get_state(self):
        return {
            "status": self.current_state.value, # A bit gross using enum values directly but works fine here
            "duration": self.timings[self.current_state]
        }

    def run(self):
        while(True):
            if self.stop_thread:
                break
            self.update_state()
            sleep(1)


    def update_state(self):
        sensor_state = self.sensor.get_state()
        alt_state = get_alt_state(self.current_state)
        self.timings[self.current_state] += 1 # Assuming current state continues
        if sensor_state == alt_state:
            self.timings[alt_state] += 1
            if self.timings[alt_state] > self.activity_threshold:
                self.switch_state()
        else:
            self.timings[alt_state] = 0

    def switch_state(self):
        old = self.current_state
        new = get_alt_state(old)
        self.current_state = new
        self.timings[old] = 0

    def stop(self):
        self.stop_thread = True