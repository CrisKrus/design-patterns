from abc import abstractmethod
from src.infra.sensor_listener import SensorListener

# subject
class Sensor:
    @abstractmethod
    def subscribe(listener: SensorListener) -> None:
        pass