from src.infra.recorded_image import RecordedImage
from src.infra.sensor import Sensor
from src.infra.sensor_listener import SensorListener


class MockSensor(Sensor):
    listener: SensorListener

    def subscribe(self, listener: SensorListener) -> None:
        self.listener = listener

    def simulate_event_with(self, image: RecordedImage)->None:
        self.listener.on_recorded_image(image)