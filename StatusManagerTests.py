import unittest
import time
from StatusManager import StatusManager, get_alt_state
from State import State

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print("starting %s" % self._testMethodName)

    def tearDown(self):
        print("ending %s" % self._testMethodName)

    def test_get_alt_state(self):
        self.assertEqual(get_alt_state(State.ACTIVE), State.INACTIVE)
        self.assertEqual(get_alt_state(State.INACTIVE), State.ACTIVE)

    def test_sm_default_state(self):
        sm = StatusManager()
        self.assertEqual(sm.get_state(), State.INACTIVE)

    def test_state_switch_i_to_a(self):
        sm = StatusManager()
        sm.activity_threshold = 5
        sm.sensor.force_state(State.ACTIVE)
        sm.start()
        time.sleep(6)
        sm.stop()
        self.assertEqual(sm.get_state(), State.ACTIVE)

    def test_state_switch_a_to_i(self):
        sm = StatusManager()
        sm.activity_threshold = 5
        sm.current_state = State.ACTIVE
        sm.sensor.force_state(State.INACTIVE)
        sm.start()
        time.sleep(6)
        sm.stop()
        self.assertEqual(sm.get_state(), State.INACTIVE)


if __name__ == '__main__':
    unittest.main()