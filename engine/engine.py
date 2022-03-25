from abc import abc

class Engine(ABC):
    def needs_service(self):
        pass