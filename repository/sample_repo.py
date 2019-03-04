import datetime

from pymongo import MongoClient

from repository import db_config


class SampleRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['ex']
        self.atom_collection = self.database['ji']

    def create(self, atom):

        try:

            self.atom_collection.insert({"atom": atom,"date":datetime.datetime.utcnow()})
            print "[INFO]inserted succesfully -ATOM"
            return True
        except Exception as e:
            print e
            return False


