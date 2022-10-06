import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from engine.Engine import Engine

class WilloughbyEngine (Engine):
    def __init__(self, last_service_mileage:int, current_mileage:int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        
        self.SERVICE_THRESHOLD =  60000
    
    def needs_service(self)->bool:
        if self.current_mileage - self.last_service_mileage > self.SERVICE_THRESHOLD:
            return True
        else:
            return False