from SensorInterface import SensorInterface
from State import State
import random

class MockSensor(SensorInterface):
    def __init__(self):
        self.state = State.STOPPED

    def get_state(self):
        return self.state

    def force_state(self, state):
        print('Forced to %s' % state)
        self.state = state