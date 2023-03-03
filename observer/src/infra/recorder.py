from abc import abstractmethod
from src.infra.recorded_image import RecordedImage


class Recorder:
    @abstractmethod
    def store_image(image: RecordedImage)->None:
        pass