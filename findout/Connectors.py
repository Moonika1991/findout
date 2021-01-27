import regex
import json


class SearchConnector:

    def parse(self, search):
        UNQUOTED_NAME = r'(?:\w[[:alnum:]_]*)'
        QUOTED_NAME = r'(?:\"(?:\\.|[^\"])*\")'

        NAME = r'(?P<name>%s|%s)' % (UNQUOTED_NAME, QUOTED_NAME)
        pattern = r'(?P<fullmatch>%s(?:\((?P<args>(?:[^\(\)]|(?R))*)\))?)' % NAME
        p = regex.compile(pattern)
        result = []
        for m in p.finditer(search):
            tmp = m.groupdict()
            if tmp['args'] and "," in tmp['args']:
                tmp['args'] = self.parse(tmp['args'])
                result.append({tmp["name"] : tmp['args']})
            elif "(" in tmp["fullmatch"]:
                result.append({tmp["name"] : tmp['args']})
            else:
                result.append(tmp['name'])
        return result

    def validate(self, search_tree):
        result = True
        for edge in search_tree:
            if type(edge) == str:
                continue
            fun = list(edge.keys())[0]
            result = self.validate(edge[fun])
            if not result:
                return False
            schema = json.load(open("C:\\Users\\monik\\PycharmProjects\\findout\\etc\\functions\\%s.json"%(fun)))
            if int(schema.get('maxNumberOfArguments')) == -1:
                result = True
            elif int(schema.get('minNumberOfArguments')) <= len(edge[fun]) <= int(schema.get('maxNumberOfArguments')):
                result = True
            else:
                result = False
        return result


