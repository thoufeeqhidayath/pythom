import json
import pprint

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config
from repository.mongo_connectionslib import MongoConnections


class ProcessRunsRepo:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['ProcessRunDB']
        self.processruns_collection = self.database['ProcessRuns']


    def create(self,process):
        process_id=self.get_id()
        insert_process={"id":process_id,"process":process}
        self.processruns_collection.insert_one(insert_process)


    def update(self,process_id,process):
        update_process_id={"id":process_id}
        update_process={"$set":{"process":process}}
        self.processruns_collection.update_one(update_process_id,update_process)


    def delete(self, process_id):
        delete_process_id={"id":process_id}
        self.processruns_collection.delete_one(delete_process_id)


    def retrieve_all(self):
        process_run_list = []
        process_run_data = self.processruns_collection.find({}, {"_id": 0})
        for process_run in process_run_data:
            process_run_list.append(process_run)
        return json.dumps(process_run_list)

    def retrieve_by_id(self, process_id):
        process_run_list = []
        process_id = {"id": process_id}
        process_data = self.processruns_collection.find(process_id, {"_id": 0})
        for process in process_data:
            process_run_list.append(process)
        return json.dumps(process_run_list)

    def get_id(self):
        s = self.processruns_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.processruns_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id


