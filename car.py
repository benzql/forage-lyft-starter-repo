from abc import ABC, abstractmethod
from engine import Engine
import battery.Battery as Battery  

class Car():
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.engine.need_service() or self.battery.need_service():
            return True
        else:
            return False
