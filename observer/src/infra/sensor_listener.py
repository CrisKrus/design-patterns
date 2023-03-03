from abc import abstractmethod
from src.infra.recorded_image import RecordedImage


# Observer
class SensorListener():
    @abstractmethod
    def on_recorder_image(image: RecordedImage)->None:
        pass