class SensorInterface:
    def get_state(self):
        """
        Was the sensor in motion in the last second
        """
        raise NotImplementedError