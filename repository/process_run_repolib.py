import json
import pprint

from bson import ObjectId
from pymongo import MongoClient

from repository import mongo_connectionslib, db_config
from repository.mongo_connectionslib import MongoConnections


class ProcessRunsRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['ProcessRunDB']
        self.processruns_collection = self.database['ProcessRuns']

    def create(self, process_id, user_name, process_run):
        try:
            # process_id = self.get_id()
            insert_process = {"id": process_id, "user": user_name, "process_run": json.loads(process_run)}
            self.processruns_collection.insert_one(insert_process)
            return True
        except Exception as e:
            print ("[ERROR] while inserting process run")
            return False

    def update(self, process_id, process):
        try:
            self.processruns_collection.update_one({"id": process_id}, {"$set": {"process": process}})
            return True
        except Exception as e:
            print ("[ERROR] while inserting process run")
            return False

    def delete(self, process_id):
        try:
            self.processruns_collection.delete_one({"id": process_id})
            return True
        except Exception as e:
            print ("[ERROR] while deleting in process run")
            return False

    def retrieve_all(self):
        return json.dumps(self.retrieve(self.processruns_collection.find({}, {"_id": 0})), indent=2)

    def retrieve_by_id(self, process_id):
        return json.dumps(self.retrieve(self.processruns_collection.find({"id": process_id}, {"_id": 0})), indent=2)

    def retrieve_by_name(self, user_name):
        return self.retrieve(self.processruns_collection.find({"user": user_name}, {"_id": 0}))

    def retrieve_by_count(self, froms, to):
        retreive_query = self.retrieve(self.processruns_collection.find({}, {"_id": 0}).skip(froms).limit(to))
        return json.dumps(retreive_query, indent=2)




    def retrieve(self, process_data):
        try:
            process_run_list = []
            for process in process_data:
                process_run_list.append(process)
            return process_run_list
        except Exception as e:
            print("[ERROR] While retrieving forom process id")
            return False

    def ret(self):
        return json.dumps(
            self.retrieve(self.processruns_collection.find({}, {"_id": 0, "process_run.vertices": 1}).skip(1).limit(2)),
            indent=2)
    def retreive_masterids(self):
        pass

    def getid_by_master(self, master_process):
        process_id = []
        master_process = {"master_process": master_process}
        process_data = self.processruns_collection.find(master_process, {"_id": 1})
        for process in process_data:
            process_id.append(process['_id'])
        return process_id

    def get_id(self):
        s = self.processruns_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.processruns_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id

