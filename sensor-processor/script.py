from typing import Tuple, List, Union, Optional


class SensorProcessor(object):
    """Represents a routine responsible to extract and check threashold from Sensor measurements

    Attributes:
    ----------
        raw_data (List[str]): list of strings.
        is_file (bool): If the object was activated by text or file
    """

    def __init__(self, text_inp: Optional[str] = None, file_inp: Optional[str] = None):
        """Initializes the object attributes

        Args:
        ---
            text_inp (Optional[str], None): text input
            file_inp (Optional[str], None): file path to be provided
        """
        self.raw_data, self.is_file = self.set_raw_data(text_inp, file_inp)

    @staticmethod
    def set_raw_data(
            text_inp: Optional[str] = None,
            file_inp: Optional[str] = None
    ) -> Tuple[List[str], bool]:
        """Reads the selected data source

        Args:
            text_inp: text input
            file_inp: file path to be provided

        Returns:
            List[str]: list of strings that represent sensor details
            bool: True if the input was a file False eitherwise
        """
        if text_inp:
            return [record for record in text_inp.strip().split('\n') if record], False
        if file_inp:
            with open(file_inp, "r") as file:
                return file.read().splitlines(), True

    def tame_raw_sensor_measurements(self, raw_mes: str) -> List[int]:
        ''' Method to process raw sensor measurements

        Args:
            raw_mes: raw measurement in string format

        Returns:
            List[int]: processed measurements
        '''
        if self.is_file:
            return [int(x) for x in raw_mes.split(",") if x.isdigit()]
        else:
            return [int(x) for x in raw_mes.split(" ") if x.isdigit()]

    @staticmethod
    def count_outliers(threashold: int, measurements: List[int]) -> int:
        ''' Counts  the outliers for the declared threasholds

        Args:
            threashold: provided threashold
            measurements: measurements

        Returns:
            int: number of measurements above the declared threashold
        '''
        return sum(measurement > threashold for measurement in measurements)

    @staticmethod
    def pretty_print(outliers: List[List[int]]) -> None:
        ''' Pretty prints the output outliers

        Args:
            outliers: sensors' outliers
        '''
        str_msg = []
        for idx in range(0, len(outliers)):
            outliers_msg = " ".join(list(map(lambda x: str(x), outliers[idx])))
            str_msg.append(
                f"S{idx} {outliers_msg}"
            )
        print("\n".join(str_msg))

    @staticmethod
    def validate_data(num_of_sensors: int, num_of_measurements: int, sensor_measurements):
        ''' Method used for data validation

        Args:
            num_of_sensors: number of sensors
            num_of_measurements: number of measurements per sensor
            sensor_measurements: list of sensor measurements
        '''
        if num_of_sensors == len(sensor_measurements):
            if num_of_measurements == len(sensor_measurements[0]) and num_of_measurements == len(
                    sensor_measurements[1]):
                pass
            else:
                raise ValueError(
                    f"Number of Measurements ({num_of_measurements}) in line #1 not correspoing with sensor measurements {len(sensor_measurements[0])}-{len(sensor_measurements[1])}")
        else:
            raise ValueError(
                f"Number of Sensors ({num_of_sensors}) in line #1 not correspoing with sensor listings {len(sensor_measurements)}")

    def process(self) -> Union[None, Tuple[int, int, List[int], List[List[int]]]]:
        ''' Process provided data

        Returns:
            Union[None, Tuple[int, int, List[int], List[List[int]]]]:
              - None: in the case where raw data are empty
              - Tuple: In the case of existing data
                - int: number of sensors
                - int: number of measurements
                - List[int]: threashold values
                - List[List[int]]]: sensors' measurements
        '''
        if self.raw_data:
            sensor_meta = self.raw_data[0].split(" ")
            num_of_sensors = int(sensor_meta[0])
            num_of_measurements = int(sensor_meta[1])
            threashold_values = [int(val) for val in self.raw_data[1].strip().split(" ")]
            sensor_measurements = list(map(self.tame_raw_sensor_measurements, self.raw_data[-num_of_sensors:]))
            return num_of_sensors, num_of_measurements, threashold_values, sensor_measurements
        else:
            return None

    def calculate_outliers(self, threashold_values: List[int], sensor_measurements: List[List[int]]) -> List[List[int]]:
        ''' Outlier calculation

        Args:
            threashold_values: threashold values after processing
            sensor_measurements: processed sensors' measurements

        Returns:
            List[List[int]: the outliers per sensor
        '''
        outliers = []
        for measurement_list in sensor_measurements:
            outliers.append([self.count_outliers(threashold, measurement_list) for threashold in threashold_values])
        return outliers

    def execute(self) -> Union[None, List[List[int]]]:
        ''' Method to assemble the class logic

        Returns:
            Union[None, List[List[int]]:
             - None: In the case of invalid input
             - List[List[int]]: The actual outliers
        '''
        result = self.process()
        if result:
            num_of_sensors, num_of_measurements, threashold_values, sensor_measurements = result
            # self.validate_data(num_of_sensors, num_of_measurements, sensor_measurements)
            outliers = self.calculate_outliers(threashold_values, sensor_measurements)
            self.pretty_print(outliers)
            return outliers
        else:
            return None
