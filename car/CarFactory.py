from car.Car import Car
from engine.CapuletEngine import CapuletEngine as CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine as WilloughbyEngine
from engine.SternmanEngine import SternmanEngine as SternmanEngine
from battery.SpindleBattery import SpindleBattery as SpindleBattery
from battery.NubbinBattery import NubbinBattery as NubbinBattery
from datetime import datetime

class CarFactory:
    def create_calliope(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int)->Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int)->Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(self, current_date: datetime.date, last_service_date: datetime.date, warning_light_on:bool)->Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int)->Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int)->Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)