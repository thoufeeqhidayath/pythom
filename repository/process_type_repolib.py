from bson import ObjectId
from pymongo import MongoClient

import db_config


class ProcessTypeRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.process_type_collection = self.database['ProcessType']

    def retrieve_data(self,process_type):
        list_of_ids=[]
        process_ids=self.process_type_collection.find({"type":process_type},{"_id":1})
        if process_ids is  not None:
            for i in process_ids:
                list_of_ids.append(i['_id'])
            return list_of_ids
        else:
            return False


        #process_ids = self.process_type_collection.find({"_id": ObjectId("5c78f3463be990173415d885")})
        #for i in process_ids:
           # print i




