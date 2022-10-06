from Car import Car
from engine.CapuletEngine import CapuletEngine as CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine as WilloughbyEngine
from engine.SternmanEngine import SternmanEngine as SternmanEngine
from battery.SpindleBattery import SpindleBattery as SpindleBattery
from battery.NubbinBattery import NubbinBattery as NubbinBattery
import datetime

class CarFactory:
    def create_calliope(current_date: datetime, last_service_date: datetime, current_mileage:int, last_service_mileage:int)->Car:
        engine = engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(current_date: datetime, last_service_date: datetime, current_mileage:int, last_service_mileage:int)->Car:
        engine = engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_palindrome(current_date: datetime, last_service_date: datetime, warning_light_on:bool)->Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_rorschach(current_date: datetime, last_service_date: datetime, current_mileage:int, last_service_mileage:int)->Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)
    
    def create_thovex(current_date: datetime, last_service_date: datetime, current_mileage:int, last_service_mileage:int)->Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine, battery)