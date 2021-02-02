from findout.QueryParser import QueryParser
from findout.ConnectorFactory import ConnectorFactory

search = 'source("osdfosfn", "osdfjerjnfg") or(search(a, b),search(b,"another example"))  search(c,"code") '

connector_factory = ConnectorFactory()

connector = connector_factory.create_connector('ExampleCSV')

print(connector.search("Country/Region", "Australia"))


