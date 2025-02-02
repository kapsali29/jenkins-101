import unittest
from unittest.mock import patch

from script import SensorProcessor


def set_static_input():
    test_inp = """
    2 9
    45 46 47 48 52 60
    S1 34 45 18 20 35 40 50 65 75
    S2 87 89 80 78 90 38 32 45 58
    """
    return [record for record in test_inp.strip().split('\n') if record], False


class TestMockScript(unittest.TestCase):

    @patch.object(SensorProcessor, 'set_raw_data', return_value=set_static_input())
    def test_mock_input(self, mock_set_raw_data):
        sp = SensorProcessor("path", None)
        outliers = sp.execute()
        self.assertListEqual(outliers, [[3, 3, 3, 3, 2, 2], [6, 6, 6, 6, 6, 5]])
        mock_set_raw_data.assert_called_once_with("path", None)  # Verify call


if __name__ == '__main__':
    unittest.main()

# python -m unittest tests.test_mock_script.TestMockScript
