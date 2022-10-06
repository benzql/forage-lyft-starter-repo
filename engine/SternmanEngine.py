import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from engine.Engine import Engine

class SternmanEngine (Engine):
    def __init__(self, warning_light_on:bool):
        self.warning_light_on = warning_light_on
    
    def needs_service(self)->bool:
        if self.warning_light_on:
            return True
        else:
            return False