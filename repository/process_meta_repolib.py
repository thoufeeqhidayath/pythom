from repository import mongo_connectionslib


class ProcessMetaRepo:
    def __init__(self):
        self.db_connection = mongo_connectionslib.MongoConnections().get_connction()
        self.process_meta_collection = self.db_connection['skan']


    def create(self,process_meta):
        self.process_meta_collection.insert_one()

    def delete(self):
        self.process_meta_collection.delete_many()

    def update(self):
        pass

    def retrieve_all(self):
        pass


