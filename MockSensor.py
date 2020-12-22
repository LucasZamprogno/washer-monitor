from SensorInterface import SensorInterface
from State import State
import random

class MockSensor(SensorInterface):
    def __init__(self):
        self.state = State.INACTIVE

    def get_state(self):
        print('Polled, responding %s' % self.state)
        return self.state

    def force_state(self, state):
        print('Forced to %s' % state)
        self.state = state