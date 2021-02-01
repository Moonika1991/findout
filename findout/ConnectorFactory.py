from abc import ABC, abstractmethod


class ConnectorFactory(ABC):

    @abstractmethod
    def connector_creator(self):
        pass