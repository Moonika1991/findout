from dataworkshop.findout.QueryParser import QueryParser
from dataworkshop.findout.connectorFactory.ConnectorFactory import ConnectorFactory


class QueryRunner():
    def __init__(self, query):
        self.parser = QueryParser(query)
        self.source = self.parser.get_source()
        self.connector = ConnectorFactory().create_connector(self.source)
        self.func = self.parser.get_func()

    def get_source(self):
        return self.source

    def run(self):
        result = self.connector.execute(self.func)
        return result
