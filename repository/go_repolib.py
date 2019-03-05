import json

from bson import ObjectId
from pymongo import MongoClient

import db_config
from repository.user_repolib import UserRepo


class GoRepoLib:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['GoDB']
        self.go_collection = self.database['Go']

    def create(self,go_id,Go):
        try:
            # id = int(self.get_molecule_id())
            user_data = {"id": go_id, "go": json.loads(Go)}
            self.go_collection.insert_one(user_data)
            return True
        except Exception as e:
            print ("[ERROR] while inserting Go")
            return False

    def update(self, go_id, go):
        try:
            self.go_collection.update_many({"id": go_id}, {"$set": {"go": go}})
            return True
        except Exception as e:
            print("[ERROR] while updating Go")
            return False

    def delete(self, go_id):
        try:
            self.go_collection.delete_many({"id": go_id})
            return True
        except Exception as e:
            print ("[ERROR] while deleting from Go`")
            return False

    def retrieve_all(self):
        try:
            go_list = []
            go_data = self.go_collection.find({}, {"_id": 0})
            for go in go_data:
                go_list.append(json.dumps(go))
            return go_list
        except Exception as e:
            print ("[ERROR] while retrieving data from Go`")
            return False

    def retrieve_by_id(self, go_id):
        try:
            molecule_list = []
            molecule_data = self.go_collection.find({"id": go_id}, {"_id": 0})
            for molecule in molecule_data:
                molecule_list.append(json.dumps(molecule))
            return molecule_list
        except Exception as e:
            print ("[ERROR] while retrieving data`")
            return False

    def getgo_by_processrun(self,process_run):
        userRepo=UserRepo()
        go_query={process_run:ObjectId(process_run)}
        godata=self.go_collection.find({})
        for instance in godata:
          if instance is not None:
              up_list = []
              up_list.append({"name": userRepo.getname_by_id(instance['user_id'])})
              up_list.append({"go": instance['go']})
              return json.dumps(up_list, indent=2)
          else:
              return False



        
        
    


