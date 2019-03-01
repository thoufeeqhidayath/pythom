import json

from repository import mongo_connectionslib


class CompoundModelRepo:
    def __init__(self):
        self.db_connection = mongo_connectionslib.MongoConnections().get_connction()
        self.compound_model_collection = self.db_connection['CompoundModel']

    def create(self, compound):
        insert_compound_model = {"id":id, "compound": compound}
        self.compound_model_collection.insert(insert_compound_model)

    def update(self, id,compound):
        update_id = {"id": id}
        update_compound = {"$set": {"compound": compound}}
        self.compound_model_collection.update_many(update_compound)

    def delete(self, id):
        delete_id = {"id": id}
        self.compound_model_collection.delete_one(delete_id)

    def retrieve_all(self):
        compound_list = []
        compound_data = self.compound_model_collection.find({}, {"_id": 0})
        for compound in compound_data:
            compound_list.append(json.dumps(compound))
        return compound_list


    def retrieve_by_id(self, compound_id):
        compound_list = []
        id = {"id": compound_id}
        compound_data = self.compound_model_collection.find({compound_id}, {"_id": 0})
        for compound in compound_data:
            compound_list.append(json.dumps(compound))
        return compound_list

