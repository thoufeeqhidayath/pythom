import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config
from repository.mongo_connectionslib import MongoConnections


class ProcessModelRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.process_models_collection = self.database['ProcessModel']

    def create(self,user_id,process_model):
        id=self.get_id()
        insert_process_model={"id":id,"user_id":user_id,"process_model":process_model}
        self.process_models_collection.insert_one(insert_process_model)


    def update(self,id,process_model):
        update_id={"id":id}
        update_user_model={"$set":{"process_model":process_model}}
        self.process_models_collection.update_many(update_id,update_user_model)

    def delete(self, id):
        delete_id={"id":id}
        self.process_models_collection.delete_one(delete_id)


    def retrieve_all(self):
        process_model_list = []
        process_model_data = self.process_models_collection.find({}, {"_id": 0})
        for user in process_model_data:
            process_model_list.append(user)
        return json.dumps(process_model_list)



    def retrieve_by_id(self, user_id):
        process_model_list = []
        user_id = {"id": user_id}
        user_data = self.process_models_collection.find(user_id, {"_id": 0})
        for user in user_data:
            process_model_list.append(user)
        return json.dumps(process_model_list)

    def get_id(self):
        s = self.process_models_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.process_models_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id




