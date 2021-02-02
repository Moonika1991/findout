from abc import ABC, abstractmethod
from pathlib import Path
import json
from findout.CSVConnector import CSVConnector
from findout.SQLConnector import SQLConnector



class ConnectorFactory(ABC):

    def create_connector(self, filename):
        path = Path(__file__).resolve().parents[1]
        connector = json.load(open("%s\\etc\\connectors\\%s.json" % (path, filename)))
        targetclass = connector.get('type').upper() + 'Connector'

        return globals()[targetclass](connector)
