import regex
import json
from pathlib import Path


class QueryParser:

    def __init__(self, search):
        self.parsed = self.__parse(search)
        self.source = self.parsed[0]
        self.functions = self.parsed[1]

    def get_source(self):
        return self.source

    def get_func(self):
        return self.functions

    def __parse(self, search):
        UNQUOTED_NAME = r'(?:\w[[:alnum:]_]*)'
        QUOTED_NAME = r'(?:\"(?:\\.|[^\"])*\")'

        NAME = r'(?P<name>%s|%s)' % (UNQUOTED_NAME, QUOTED_NAME)
        pattern = r'(?P<fullmatch>%s(?:\((?P<args>(?:[^\(\)]|(?R))*)\))?)' % NAME
        p = regex.compile(pattern)
        result = []
        source = ''
        for m in p.finditer(search):
            tmp = m.groupdict()
            if tmp['name'] == 'source':
                source = tmp['args']
            elif tmp['args'] and "," in tmp['args']:
                tmp['args'] = self.__parse(tmp['args'])
                result.append({tmp["name"] : tmp['args']})
            elif "(" in tmp["fullmatch"]:
                result.append({tmp["name"] : tmp['args']})
            else:
                result.append(tmp['name'])
        return source, result

    def __validate(self, search_tree):
        path = Path(__file__).resolve().parents[1]
        result = True
        for edge in search_tree:
            if type(edge) == str:
                continue
            fun = list(edge.keys())[0]
            result = self.__validate(edge[fun])
            if not result:
                return False
            schema = json.load(open("%s\\etc\\functions\\%s.json" % (path, fun)))
            if int(schema.get('maxNumberOfArguments')) == -1:
                result = True
            elif int(schema.get('minNumberOfArguments')) <= len(edge[fun]) <= int(schema.get('maxNumberOfArguments')):
                result = True
            else:
                result = False
        return result

