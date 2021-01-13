import regex


def parse(search):
    pattern = r'(?P<fullmatch>(?P<name>\w[[:alnum:]]*)(?:\((?P<args>(?:[^\(\)]|(?R))*)\))?)'
    p = regex.compile(pattern)
    result = []
    for m in p.finditer(search):
        tmp = m.groupdict()
        if tmp['args'] and "," in tmp['args']:
            tmp['args'] = parse(tmp['args'])
            result.append({tmp["name"] : tmp['args']})
        elif "(" in tmp["fullmatch"]:
            result.append({tmp["name"] : tmp['args']})
        else:
            result.append(tmp['name'])
    return result


print(parse('or(search(a,”example”),search(b(),”another example”))  search(c,"code") '))