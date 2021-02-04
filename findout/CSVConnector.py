from findout.Connector import Connector
import pandas as pd


class CSVConnector(Connector):

    def __init__(self, access):
        self._start_object = pd.read_csv(access.get('path'), sep=access.get('sep'))
        self._current_object = pd.DataFrame()

    def execute(self, query):
        for edge in query:
            print(edge)
            fun = list(edge.keys())[0]
            args = edge[fun]
            if all(isinstance(arg, str) for arg in args):
                if fun == 'search':
                    self._current_object = self.search(args)
            else:
                for arg in args:
                    if type(arg) == dict:
                        self.execute(arg)
        return self._current_object

    def search(self, args):
        if len(args) == 1:
            sel = self._start_object[args[0]]
            result = sel
        else:
            sel = self._start_object.loc[self._start_object[args[0]] == args[1]]
            result = sel
        return result

    def grater_than(self, col_name, value):
        pass

    # alternative
    def alt(self):
        return

    # conjunction
    def con(self):
        return




