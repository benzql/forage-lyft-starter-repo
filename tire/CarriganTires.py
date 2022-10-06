import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Tires import Tires as Tires

class CarriganTires(Tires):
    def __init__(self, sensors):
        self.sensors = sensors
        self.TIRE_WORN_THRESHOLD = 0.9
        
    def needs_service(self)->bool:
        
        for s in self.sensors:
            if s >= self.TIRE_WORN_THRESHOLD:
                return True
        return False