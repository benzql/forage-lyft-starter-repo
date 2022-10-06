import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from car.CarFactory import CarFactory
from engine.CapuletEngine import CapuletEngine as CapuletEngine
from engine.WilloughbyEngine import WilloughbyEngine as WilloughbyEngine
from engine.SternmanEngine import SternmanEngine as SternmanEngine
from battery.SpindleBattery import SpindleBattery as SpindleBattery
from battery.NubbinBattery import NubbinBattery as NubbinBattery

    
class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.96]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())
        
    def test_tires_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.89]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
        
    def test_battery_should_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_glissade(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.96]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())
        
    def test_tires_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.89]


class TestPalindrome(unittest.TestCase):
        
    def test_battery_should_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        tiresensors=[0,0,0,0]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        tiresensors=[0,0,0,0]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        warning_light_is_on = True
        tiresensors=[0,0,0,0]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        warning_light_is_on = False
        tiresensors=[0,0,0,0]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertFalse(car.needs_service())
        
    def test_tires_should_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        warning_light_is_on = False
        tiresensors=[1,1,1,1]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertTrue(car.needs_service())

    def test_tires_should_not_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        warning_light_is_on = False
        tiresensors=[0,0,0,0]

        car = car_factory.create_palindrome(today, last_service_date, warning_light_is_on, tiresensors)
        self.assertFalse(car.needs_service())

class TestRorschach(unittest.TestCase):
   
    def test_battery_should_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_rorschach(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())
    
    def test_tires_should_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0.95,0.95,0.95,0.96]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())
        
    def test_tires_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.89]
        
        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())



class TestThovex(unittest.TestCase):
        
    def test_battery_should_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car_factory =CarFactory()
        today=last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        tiresensors=[0,0,0,0]

        car = car_factory.create_thovex(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())
        
    def test_tires_should_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.96]

        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertTrue(car.needs_service())
        
    def test_tires_should_not_be_serviced(self):
        car_factory =CarFactory()
        today = last_service_date = datetime.today().date()
        current_mileage = 0
        last_service_mileage = 0
        tiresensors=[0,0,0,0.89]
        
        car = car_factory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, tiresensors)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()

