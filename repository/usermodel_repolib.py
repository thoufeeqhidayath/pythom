import json

from repository import mongo_connectionslib
from repository.mongo_connectionslib import MongoConnections


class UserModelRepo:
    def __init__(self):
        self.db_connection = mongo_connectionslib.MongoConnections().get_connction()
        self.user_models_collection = self.db_connection['UserModels']

    def create(self, user_id,user_model):
        insert_user_model={"user_id":user_id,"user_model":user_model}
        self.user_models_collection.insert(insert_user_model)

    def update(self, user_id, user_model):
        update_id={"user_id":user_id}
        update_user_model={"$set":{"user_model":user_model}}
        self.user_models_collection.update_many(update_user_model)

    def delete(self, user_id):
        delete_id={"user_id":user_id}
        self.user_models_collection.delete_one(delete_id)


    def retrieve_all(self):
        return_user_model={}
        user_models= self.user_models_collection.find()
        for users in user_models:
            return_user_model[users['user_id']] = users['user_model']
        return json.dumps(return_user_model)

    def retrieve_by_id(self, user_id):
        return_user_model = {}
        user_id={"user_id":user_id}
        user_models=self.user_models_collection.find(user_id)
        for users in user_models:
            return_user_model[users['user_id']] = users['user_model']
        return json.dumps(return_user_model)

