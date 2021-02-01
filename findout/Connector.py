from abc import ABC, abstractmethod


class Connector(ABC):
    # Factory method  product

    @abstractmethod
    def search(self) -> list:
        pass

    #altarnative
    @abstractmethod
    def alt(self) -> list:
        pass

    #conjunction
    @abstractmethod
    def con(self) -> list:
        pass
