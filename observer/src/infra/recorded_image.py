from datetime import datetime


class RecordedImage:
    time_stamp: datetime

    def __init__(self, time_stamp) -> None:
        self.time_stamp = time_stamp

    @staticmethod
    def snapshot():
        return RecordedImage(datetime.now())
    
    def __eq__(self, __o: object) -> bool:
        return self.time_stamp == __o.time_stamp
