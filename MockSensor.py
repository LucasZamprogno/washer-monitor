from SensorInterface import SensorInterface
from threading import Thread
from State import State
from time import sleep
import random

class MockSensor(Thread, SensorInterface):
    def __init__(self):
        super(MockSensor, self).__init__()
        super().setDaemon(True)
        self.state = State.STOPPED
        self.stop_thread = False

    def run(self):
        while True:
            if self.stop:
                break
            sleep(60)

    def stop(self):
        self.stop_thread = True

    def get_state(self):
        return self.state

    def force_state(self, state):
        print('Forced to %s' % state)
        self.state = state