from findout.QueryParser import QueryParser
from findout.ConnectorFactory import ConnectorFactory

search = 'source("ExampleCSV") col(and(goe("1/27/20", 4), equal("Country/Region", Australia)), "Country/Region", Lat, Long, "1/27/20")'

parser = QueryParser(search)

name = parser.get_source()

connector = ConnectorFactory().create_connector(name)

fun = parser.get_func()

print(connector.execute(fun))
