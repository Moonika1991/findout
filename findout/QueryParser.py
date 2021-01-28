import regex
import json
from pathlib import Path


class QueryParser:

    def __init__(self, search):
        self.parsed = self.__parse(search)
        self.__validate(self.parsed)
        self.functions = self.parsed

    def get_source(self):
        return self.source

    def get_func(self):
        return self.functions

    # syntactic analysis of query
    def __parse(self, search):
        UNQUOTED_NAME = r'(?:\w[[:alnum:]_]*)'
        QUOTED_NAME = r'(?:\"(?:\\.|[^\"])*\")'

        NAME = r'(?P<name>%s|%s)' % (UNQUOTED_NAME, QUOTED_NAME)
        pattern = r'(?P<fullmatch>%s?(?:\((?P<args>(?:[^\(\)]|(?R))*)\))?)' % NAME
        p = regex.compile(pattern)
        match = regex.search(pattern, search)
        if match.group('name') is None:
            raise Exception('Incorrect query! Syntactic analysis failed!')
        result = []
        self.source = ''
        for m in p.finditer(search):
            tmp = m.groupdict()
            # to avoid adding empty matches to result array
            if tmp['fullmatch'] == '':
                continue
            elif tmp['name'] == 'source':
                self.source = tmp['args']
                continue
            elif tmp['args'] and "," in tmp['args']:
                tmp['args'] = self.__parse(tmp['args'])
                result.append({tmp['name']: tmp['args']})
            elif "(" in tmp['fullmatch']:
                result.append({tmp['name']: tmp['args']})
            else:
                result.append(tmp['name'])
        return result

    # semantic analysis of search tree
    def __validate(self, search_tree):
        path = Path(__file__).resolve().parents[1]
        result = True
        for edge in search_tree:
            if type(edge) == str:
                continue
            fun = list(edge.keys())[0]
            result = self.__validate(edge[fun])
            if not result:
                raise Exception('Incorrect query! Semantic analysis failed!')
            schema = json.load(open("%s\\etc\\functions\\%s.json" % (path, fun)))
            if int(schema.get('maxNumberOfArguments')) == -1:
                result = True
            elif int(schema.get('minNumberOfArguments')) <= len(edge[fun]) <= int(schema.get('maxNumberOfArguments')):
                result = True
            else:
                raise Exception('Incorrect query! Semantic analysis failed!')
        return result
