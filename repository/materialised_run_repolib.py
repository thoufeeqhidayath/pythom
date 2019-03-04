import json

from pymongo import MongoClient

import db_config


class MaterialisedRunRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['MaterialisedRunDB']
        self.go_collection = self.database['MaterialisedRun']

    def create(self, run_id, materialised_run):
        try:
            # id = int(self.get_molecule_id())
            user_data = {"id": run_id, "materialised_run": json.loads(materialised_run)}
            self.go_collection.insert_one(user_data)
            return True
        except Exception as e:
            print ("[ERROR] while inserting materialised Run")
            return False

    def update(self, run_id, materialised_run):
        try:
            self.go_collection.update_many({"id": run_id}, {"$set": {"materialised_run": materialised_run}})
            return True
        except Exception as e:
            print("[ERROR] while updating Go")
            return False

    def delete(self, run_id):
        try:
            self.go_collection.delete_many({"id": run_id})
            return True
        except Exception as e:
            print ("[ERROR] while deleting from Go`")
            return False

    def retrieve_all(self):
        try:
            run_list = []
            run_data = self.go_collection.find({}, {"_id": 0})
            for run in run_data:
                run_list.append(json.dumps(run))
            return run_list
        except Exception as e:
            print ("[ERROR] while retrieving data from Go`")
            return False

    def retrieve_by_id(self, go_id):
        try:
            run_list = []
            run_data = self.go_collection.find({"id": go_id}, {"_id": 0})
            for run in run_data:
                run_list.append(json.dumps(run_data))
            return run_list
        except Exception as e:
            print ("[ERROR] while retrieving data`")
            return False
