from findout.QueryParser import QueryParser
from findout.ConnectorFactory import ConnectorFactory

search = 'source("ExampleCSV") or("Country/Region", "Province/State")'

parser = QueryParser(search)

name = parser.get_source()

connector = ConnectorFactory().create_connector(name)

fun = parser.get_func()

print(connector.execute(fun))
