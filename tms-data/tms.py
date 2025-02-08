from dataclasses import dataclass, field
from typing import List
import json

from datetime import date, datetime


@dataclass
class TimeSeries:
    time: date
    value: float
    

@dataclass
class Point:
    point_id: int
    tms: List[TimeSeries]


@dataclass
class Storage:
    points: List[Point] = field(default_factory=list) 


class Executor(object):
    """Execution class of the TMS

    Attributes:
        storage (Storage): keeps a list of points
    """
    def __init__(self):
        self.storage = Storage()
    
    @staticmethod
    def tms_set(raw_data, date_format="%Y-%m-%dT%H:%M:%SZ"):
        """process the raw data point and constructs a Timeseries object

        Args:
            raw_data (str): JSON that includes time and value
            date_format (str, optional): date format to be used. Defaults to "%Y-%m-%dT%H:%M:%SZ".

        Returns:
            Timeseries: returns the Timeseries object from the raw data.
        """
        tms_data = json.loads(raw_data.replace("\'", "\""))
        return TimeSeries(
            time=datetime.strptime(tms_data["time"], date_format),
            value=float(tms_data["value"])
        )

    def update_point_tms(self, idx, data_point):
        """Updates an existing Point object

        Args:
            idx (int): position of the for loop
            data_point (str): raw data point
        """
        current_point_tms = self.storage.points[idx].tms[-1]
        new_tms = self.tms_set(data_point["point"])
        if current_point_tms.value == new_tms.value:
            pass
        else:
            self.storage.points[idx].tms.append(new_tms)

    def construct_point(self, data_point):
        """Main logic

        Args:
            data_point (str): raw data point
        """
        point_id = int(data_point["id"])
        len_of_points = len(self.storage.points)
        found = 0
        for idx in range(0, len_of_points):
            if point_id == self.storage.points[idx].point_id:
                found = 1
                self.update_point_tms(idx, data_point)
                break   
        if not found:
            tms_obj = self.tms_set(data_point["point"])
            self.storage.points.append(Point(point_id=point_id, tms=[tms_obj]))
            
            
if __name__ == "__main__":
    exec = Executor()           
    exec.construct_point({"id": 1,"point": "{'time': '2024-01-01T05:00:00Z', 'value': 4}"})
    exec.construct_point({"id": 1,"point": "{'time': '2024-01-01T06:00:00Z', 'value': 5}"})
    exec.construct_point({"id": 1,"point": "{'time': '2024-01-01T07:00:00Z', 'value': 6}"})
    exec.construct_point({"id": 1,"point": "{'time': '2024-01-01T07:00:00Z', 'value': 6}"})
    # from pdb import set_trace as bp

    print(exec.storage)
    # bp()
