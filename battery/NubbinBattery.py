import py_compile
from battery.Battery import Battery
import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime.date, current_date: datetime.date ):
        self.last_service_date= last_service_date
        self.current_date = current_date
        
        self.SERVICE_THRESHOLD = 4
    
    def need_service(self)->bool:
        if self.current_date.year - self.last_service_date.year >= self.SERVICE_THRESHOLD:
            return True
        else:
            return False