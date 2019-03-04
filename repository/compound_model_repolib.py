import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class CompoundModelRepo:

    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.compound_model_collection = self.database['CompoundModel']

    def create(self,compound):
        try:
            id = self.get_id()
            self.compound_model_collection.insert_one({"id": id, "compound": compound})
            print("[INFO] inserted succesfuly")
            return True
        except Exception as e:
            print("[ERROR] Error while inserting datain comound model")
            return False


    def update(self, id,compound):
        try:
            self.compound_model_collection.update_many({"id": id}, {"$set": {"compound": compound}})
            return True
        except Exception as e:
            print ("[ERROR] while updating compund model")
            return  False

    def delete(self, id):
        try:
            self.compound_model_collection.delete_one({"id": id})
            return True
        except Exception as e:
            print ("[ERROR] while deleting compund model")
            return False


    def retrieve_all(self):
        try:
            compound_list = []
            compound_data = self.compound_model_collection.find({}, {"_id": 0})
            for compound in compound_data:
                compound_list.append(json.dumps(compound))
            return compound_list
        except Exception as e:
            print ("[ERROR] while retriving compund model")
            return False




    def retrieve_by_id(self,compound_id):
        try:
            compound_list = []
            compound_data = self.compound_model_collection.find({"id": compound_id}, {"_id": 0})
            for compound in compound_data:
                compound_list.append(json.dumps(compound))
            return compound_list
        except Exception as e:
            print ("[ERROR] while retriving compund model")
            return False

    def get_id(self):
        s = self.compound_model_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.compound_model_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id
