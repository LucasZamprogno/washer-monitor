from enum import Enum

class State(Enum):
    RUNNING = "Running"
    STOPPED = "Stopped"

class StateUtils:
    @staticmethod
    def get_alt_state(state):
        return State.STOPPED if state == State.RUNNING else State.RUNNING