from battery.Battery import Battery
from datetime import datetime
from datetime import  timedelta

class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date = datetime.today().date() ):
        self.last_service_date= last_service_date
        self.current_date = current_date
        
        self.SERVICE_THRESHOLD = timedelta(days=4*365)
    
    def needs_service(self)->bool:
        if self.current_date -  self.last_service_date > self.SERVICE_THRESHOLD:
            return True
        else:
            return False