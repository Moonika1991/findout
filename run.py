from findout.QueryParser import QueryParser

search = 'source("osdfosfn", "osdfjerjnfg") or(search(a,"example"),search(b,"another example"))  search(c,"code") '

sc = QueryParser(search)
print(QueryParser.get_source(sc))


