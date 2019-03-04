import json

from bson import ObjectId
from pymongo import MongoClient

import db_config


class ProcessModelRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.process_models_collection = self.database['ProcessModel']

    def create(self,user_id,process_model):
        try:
            id = self.get_id()
            insert_process_model = {"id": id, "user_id": user_id, "process_model": process_model}
            self.process_models_collection.insert_one(insert_process_model)
            return True
        except Exception as e:
            print("[ERROR] while inserting into process model")
            return False


    def update(self,id,process_model):
        try:
            update_id = {"id": id}
            update_user_model = {"$set": {"process_model": process_model}}
            self.process_models_collection.update_many(update_id, update_user_model)
        except Exception as e:
            print("[ERROR] while updating  process model")
            return False

    def delete(self, id):
        try:
            self.process_models_collection.delete_one({"id":id})
        except Exception as e:
            print("[ERROR] while delting process model")
            return False


    def retrieve_all(self):
        try:
            process_model_list = []
            process_model_data = self.process_models_collection.find({}, {"_id": 0})
            for user in process_model_data:
                process_model_list.append(user)
            return json.dumps(process_model_list)
        except Exception as e:
            print "[ERROR] while retrieving from process model"
            return False




    def retrieve_by_id(self, user_id):
        try:
            process_model_list = []
            user_id = {"id": user_id}
            user_data = self.process_models_collection.find(user_id, {"_id": 0})
            for user in user_data:
                process_model_list.append(user)
            return json.dumps(process_model_list)
        except Exception as e:
            print "[ERROR] "
            return  False


    def retrievegojs_by_processtype(self,id):
        gojs_data=[]
        query={"process_type":str(id)}
        data=self.process_models_collection.find(query,{"_id":0,"gojs":1})
        for gojs in data:
            gojs_data.append(gojs)
        return gojs_data


    def get_id(self):
        s = self.process_models_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.process_models_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id




