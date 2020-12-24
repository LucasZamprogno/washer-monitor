import unittest
import time
from SW420 import SW420
from State import State, StateUtils

class TestStringMethods(unittest.TestCase):
    '''
    THESE TESTS ARE SEMI-MANUAL
    (stupid real world)
    '''

    def setUp(self):
        print("starting %s" % self._testMethodName)

    def tearDown(self):
        print("ending %s" % self._testMethodName)

    def test_1_stopped(self):
        sw420 = SW420(4)
        sw420.start()
        print("Don't touch! (3s)")
        time.sleep(3)
        self.assertEqual(sw420.get_state(), State.STOPPED)
        sw420.stop()

    def test_2_running(self):
        sw420 = SW420(4)
        sw420.start()
        print("Wiggle! (3s)")
        time.sleep(3)
        self.assertEqual(sw420.get_state(), State.RUNNING)
        sw420.stop()


if __name__ == '__main__':
    unittest.main()