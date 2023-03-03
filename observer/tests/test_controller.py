from src.controller import Controller
from src.infra.recorded_image import RecordedImage
from tests.mock_recorder import MockRecorder
from tests.mock_sensor import MockSensor


class TestController:
    def test_something(self):
        recorder = MockRecorder();
        sensor = MockSensor();
        controller = Controller.start(recorder, sensor);
        recorded_image = RecordedImage.snapshot();
        sensor.simulate_event_with(recorded_image);

        recorder.assertThatStoreImageWasCalledWith(recorded_image);