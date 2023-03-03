from observer.src.infra.sensor_listener import SensorListener
from src.infra.recorded_image import RecordedImage
from src.infra.recorder import Recorder
from src.infra.sensor import Sensor

# controller/observer
class Controller(SensorListener):
    recorder: Recorder
    sensor: Sensor

    def __init__(self, recorder: Recorder, sensor: Sensor) -> None:
        self.recorder = recorder
        self.sensor = sensor

    @staticmethod
    def start(recorder: Recorder, sensor: Sensor):
        controller = Controller(recorder, sensor)
        controller._subscribe_to_events()
        return controller

    def _subscribe_to_events(self)-> None:
        self.sensor.subscribe(self)

    def on_recorded_image(self, image: RecordedImage) -> None:
        self.recorder.store_image(image)