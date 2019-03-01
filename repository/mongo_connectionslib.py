from pymongo import MongoClient
import db_config

class MongoConnections:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection[db_config.database]

    def get_connction(self):
        return self.database


