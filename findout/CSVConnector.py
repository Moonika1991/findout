from findout.Connector import Connector
import pandas as pd


class CSVConnector(Connector):

    def __init__(self, access):
        self._current_object = pd.read_csv(access.get('path'), sep=access.get('sep'))
        self._col = self._current_object.columns

    def search(self, *args):
        result = []
        if len(args) == 1:
            sel = self._current_object[args[0]]
            result = sel.to_json()
        else:
            sel = self._current_object.loc[self._current_object[args[0]] == args[1]]
            result = sel.to_json()
        return result

    # altarnative
    def alt(self):
        return

    # conjunction
    def con(self):
        return




