from findout.Connector import Connector
import sqlite3


class SQLConnector(Connector):

    def __init__(self, access):
        con = sqlite3.connect(access.get('db_name'))
        self.cur = con.cursor()
        self.tab_name = access.get('table_name')

    def execute(self, query):
        fun = list(query[0].keys())[0]
        args = query[0][fun]
        formatted = self.format_query(query)
        if fun == 'col':
            final = self.col(args)
        else:
            final = 'SELECT * FROM ' + self.tab_name + ' WHERE ' + formatted
        print(final)

        self.cur.execute(final)
        rows = self.cur.fetchall()
        for row in rows:
            print(row)

    def format_query(self, query):
        global result
        fun = list(query[0].keys())[0]
        args = query[0][fun]
        if any(type(arg) is dict for arg in args):
            pos = 0
            for arg in args:
                if type(arg) is str:
                    pos += 1
                    continue
                # query must be a list of dicts (arg is dict)
                temp_query = [arg]
                part = self.format_query(temp_query)
                pos = args.index(arg)
                args.pop(pos)
                args.insert(pos, part)
            query[0][fun] = args
            result = self.format_query(query)
        elif all(type(arg) is str for arg in args):
            col = args[0]
            if fun == 'equal':
                result = '"' + col + '"' + '=' + '"' + args[1] + '"'
            elif fun == 'gt':
                result = '"' + col + '"' + '>' + '"' + args[1] + '"'
            elif fun == 'lt':
                result = '"' + col + '"' '<' + '"' + args[1] + '"'
            elif fun == 'goe':
                result = '"' + col + '"' + '>=' + '"' + args[1] + '"'
            elif fun == 'loe':
                result = '"' + col + '"' '<=' + '"' + args[1] + '"'
            elif fun == 'or':
                result = self.alt(args)
            elif fun == 'and':
                result = self.conj(args)
        return result

    def alt(self, args):
        part = ''
        for arg in args:
            part = part + arg + ' OR '
        last_pos = len(part) - 4
        part = part[0: last_pos]
        return part

    def conj(self, args):
        part = ''
        for arg in args:
            part = part + arg + ' AND '
        last_pos = len(part) - 5
        part = part[0: last_pos]
        return part

    def col(self, args):
        sql_query = 'SELECT '
        for arg in args[1:]:
            sql_query += '"' + arg + '", '
        sql_query = sql_query[:len(sql_query)-2]
        sql_query += ' FROM ' + self.tab_name + ' WHERE ' + args[0]
        return sql_query

    def exc(self, args):
        return
