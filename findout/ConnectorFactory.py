from abc import ABC, abstractmethod
from pathlib import Path
import json
from findout.CSVConnector import CSVConnector
from findout.SQLConnector import SQLConnector
from findout.Connector import Connector


class ConnectorFactory(ABC):

    def create_connector(self, filename) -> Connector:
        # finding path by given filename
        path = Path(__file__).resolve().parents[1]
        for name in filename:
            connector = json.load(open("%s\\etc\\connectors\\%s.json" % (path, name)))
            targetclass = connector.get('type').upper() + 'Connector'

        return globals()[targetclass](connector)

