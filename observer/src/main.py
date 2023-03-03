from src.controller import Controller
from src.infra.recorder import Recorder
from src.infra.sensor import Sensor


sensor = Sensor()
recorder = Recorder()


controller = Controller.start(recorder, sensor)