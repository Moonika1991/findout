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
            # query must be a list of dicts (arg is dict)
            pos = 0
            for arg in args:
                if type(arg) is str:
                    pos += 1
                    continue
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
        elif all(type(arg) is str for arg in args):
            col = args[0]
            if args[1].isdigit():
                val = float(args[1])
            else:
                val = args[1]
            if fun == 'equal':
                result = self._start_object.loc[self._start_object[col] == val]
            elif fun == 'gt':
                result = self._start_object.loc[self._start_object[col] > val]
            elif fun == 'lt':
                result = self._start_object.loc[self._start_object[col] < val]
            elif fun == 'goe':
                result = self._start_object.loc[self._start_object[col] >= val]
            elif fun == 'loe':
                result = self._start_object.loc[self._start_object[col] <= val]
        elif fun == 'or':
            result = self.alt(args)
        return result

    def alt(self, args):
        result = pd.DataFrame()
        for arg in args:
            result = pd.concat([result, arg]).drop_duplicates()
            result = result.sort_index()
        return result




