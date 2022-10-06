import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from Tires import Tires as Tires

class  OctoprimeTires (Tires):
    def __init__(self, sensors):
        self.sensors = sensors
        self.TIRE_WORN_THRESHOLD = 3
        
    def needs_service(self)->bool:
        return True if sum(self.sensors) >= self.TIRE_WORN_THRESHOLD else False