import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class CompoundModelRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.compound_model_collection = self.database['CompoundModel']

    def create(self,compound):
        id=self.get_id()
        insert_compound_model = {"id":id, "compound": compound}
        self.compound_model_collection.insert_one(insert_compound_model)

    def update(self, id,compound):
        update_id = {"id": id}
        update_compound = {"$set": {"compound": compound}}
        self.compound_model_collection.update_many(update_id,update_compound)

    def delete(self, id):
        delete_id = {"id": id}
        self.compound_model_collection.delete_one(delete_id)

    def retrieve_all(self):
        compound_list = []
        compound_data = self.compound_model_collection.find({}, {"_id": 0})
        for compound in compound_data:
            compound_list.append(json.dumps(compound))
        return compound_list


    def retrieve_by_id(self,compound_id):
        compound_list = []
        id = {"id": compound_id}
        compound_data = self.compound_model_collection.find(id, {"_id": 0})
        for compound in compound_data:
            compound_list.append(json.dumps(compound))
        return compound_list

    def get_id(self):
        s = self.compound_model_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.compound_model_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id
