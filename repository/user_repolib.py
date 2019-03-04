import json

from flask import jsonify
from pymongo import MongoClient

from mongo_connectionslib import MongoConnections
from repository import mongo_connectionslib, db_config


class UserRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.users_collection=self.database['Users']


    def create(self,user):
        try:
            user_id = int(self.get_id())
            user_data = {"id": user_id, "user": user}
            self.users_collection.insert(user_data)
        except Exception as e:
            print("[ERROR] while inserting user")




    def update(self,user_id,user):
        try:
           self.users_collection.update_many({"id":user_id},{"$set":{"user":user}})
           return
        except Exception as e:
            print("[ERROR] while updating from user")
            return False


    def delete(self,user_id):
        try:
            delete_id = {"id": user_id}
            self.users_collection.delete_one(delete_id)
        except Exception as e :
            print("[ERROR] while updating from user")
            return False

    def retrieve_all(self):
        return_user_list=[]
        user_data=self.users_collection.find({},{"_id":0})
        for user in user_data:
           return_user_list.append(user)
        return json.dumps(return_user_list)


    def retrieve_by_id(self,user_id):
        return_user_list = []
        user_id={"id":user_id}
        user_data= self.users_collection.find(user_id,{"_id":0})
        for user in user_data:
            return_user_list.append(user)
        return json.dumps(return_user_list)

    def get_id(self):
        s = self.users_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.users_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id






