import unittest

from script import SensorProcessor


class TestSensorProcessor(unittest.TestCase):

    def test_empty_input(self):
        empty_input = ""
        sp = SensorProcessor(empty_input)
        self.assertEqual(sp.process(), None)

    # def test_wrong_number_of_sensors(self):
    #     inp = """
    #     3 9
    #     45 46 47 48 52 60
    #     S1 34 45 18 20 35 40 50 65 75
    #     S2 87 89 80 78 90 38 32 45 58
    #     """
    #     sp = SensorProcessor(inp)
    #     with self.assertRaises(ValueError):
    #         sp.execute()

    # def test_wrong_number_of_measurements(self):
    #     inp = """
    #     2 9
    #     45 46 47 48 52 60
    #     S1 34 45 18 20 35 40 50 65 75
    #     S2 87 89 80 78 90 38 32 45 58 89 90
    #     """
    #     sp = SensorProcessor(inp)
    #     with self.assertRaises(ValueError):
    #         sp.execute()

    def test_correct_output(self):
        inp = """
        2 9
        45 46 47 48 52 60
        S1 34 45 18 20 35 40 50 65 75
        S2 87 89 80 78 90 38 32 45 58
        """
        sp = SensorProcessor(text_inp=inp)
        outliers = sp.execute()
        self.assertListEqual(outliers, [[3, 3, 3, 3, 2, 2], [6, 6, 6, 6, 6, 5]])


# python -m unittest tests.test_script

if __name__ == "__main__":
    unittest.main()
