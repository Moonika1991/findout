from abc import ABC, abstractmethod


class Connector(ABC):
    # Factory method  product

    @abstractmethod
    def execute(self, function):
        pass

    @abstractmethod
    def search(self, *args):
        pass

    @abstractmethod
    def grater_than(self, col_name, value):
        pass

    # alternative
    @abstractmethod
    def alt(self):
        pass

    # conjunction
    @abstractmethod
    def con(self):
        pass
