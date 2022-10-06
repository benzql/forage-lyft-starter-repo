from abc import ABC, abstractmethod

class Engine:    
    @abstractmethod
    def need_service(self) ->bool:
        pass