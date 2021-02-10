from abc import ABC, abstractmethod


class Connector(ABC):
    # Factory method  product

    @abstractmethod
    def execute(self, function):
        pass

    @abstractmethod
    def alt(self, args):
        pass