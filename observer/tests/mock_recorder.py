from src.infra.recorded_image import RecordedImage
from src.infra.recorder import Recorder


class MockRecorder(Recorder):
    recorded_image: RecordedImage
    
    def assertThatStoreImageWasCalledWith(self, image: RecordedImage):
        assert self.recorded_image == image

    def store_image(self, image: RecordedImage) -> None:
        self.recorded_image = image