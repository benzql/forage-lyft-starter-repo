import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from car.Car import Car
from engine.CapuletEngine import CapuletEngine as CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine as WilloughbyEngine
from engine.SternmanEngine import SternmanEngine as SternmanEngine
from battery.SpindleBattery import SpindleBattery as SpindleBattery
from battery.NubbinBattery import NubbinBattery as NubbinBattery
from tire.CarriganTires import  CarriganTires 
from tire.OctoprimeTires import OctoprimeTires
from datetime import datetime

class CarFactory:
    def create_calliope(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int, tiresensors:list)->Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        tires = CarriganTires(tiresensors)
        return Car(engine, battery, tires)

    def create_glissade(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int, tiresensors: list)->Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindleBattery(last_service_date, current_date)
        tires = CarriganTires(tiresensors)
        return Car(engine, battery, tires)
    
    def create_palindrome(self, current_date: datetime.date, last_service_date: datetime.date, warning_light_on:bool, tiresensors:list)->Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindleBattery(last_service_date, current_date)
        tires = OctoprimeTires(tiresensors)
        return Car(engine, battery, tires)
    
    def create_rorschach(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int, tiresensors: list)->Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = OctoprimeTires(tiresensors)
        return Car(engine, battery, tires)
    
    def create_thovex(self, current_date: datetime.date, last_service_date: datetime.date, current_mileage:int, last_service_mileage:int, tiresensors: list)->Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(tiresensors)
        return Car(engine, battery, tires)