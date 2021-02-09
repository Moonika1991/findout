from findout.Connector import Connector
import pandas as pd


class CSVConnector(Connector):

    def __init__(self, access):
        self._start_object = pd.read_csv(access.get('path'), sep=access.get('sep'))

    def execute(self, query):
        fun = list(query[0].keys())[0]
        args = query[0][fun]
        res_args = args
        part_result = query
        if any(type(arg) is dict for arg in args):
            pos = 0
            for arg in args:
                if type(arg) is str:
                    pos += 1
                    continue
                # query must be a list of dicts (arg is dict)
                temp_query = [arg]
                part = self.execute(temp_query)
                if type(arg) is pd.DataFrame:
                    pos += 1
                    continue
                else:
                    res_args.pop(pos)
                    res_args.insert(pos, part)
                    pos += 1
            part_result[0][fun] = res_args
            result = self.execute(part_result)
        elif fun == 'search':
            result = self.search(args)
        elif fun == 'gt':
            result = self.grater_than(args)
        elif fun == 'or':
            result = self.alt(args)
        return result

    def search(self, args):
        if len(args) == 1:
            sel = self._start_object[args[0]]
            result = sel
        else:
            sel = self._start_object.loc[self._start_object[args[0]] == args[1]]
            result = sel
        return result

    def grater_than(self, args):
        col = args[0]
        value = float(args[1])
        result = self._start_object.loc[self._start_object[col] > value]
        return result

    # alternative
    def alt(self, args):
        result = pd.DataFrame()
        for arg in args:
            if type(arg) == str:
                sel = self._start_object[arg]
                result = result.append(sel)
            else:
                result = result.append(arg)
        return result

    # conjunction
    def con(self):
        return




