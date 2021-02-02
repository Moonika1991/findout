from abc import ABC, abstractmethod


class Connector(ABC):
    # Factory method  product

    @abstractmethod
    def search(self, *args) -> dict:
        pass

    @abstractmethod
    def grater_than(self, col_name, value) -> dict:
        pass

    # alternative
    @abstractmethod
    def alt(self) -> list:
        pass

    # conjunction
    @abstractmethod
    def con(self) -> list:
        pass
