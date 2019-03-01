import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class AtomRepo:

    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['AtomDB']
        self.atom_collection = self.database ['Atom']


    def create(self,atom):
        id = self.get_id()
        atom_data = {"id": id, "atom": atom}
        self.atom_collection.insert(atom_data)


    def delete(self,atom_id):
        atom_delete_id={"id":int(atom_id)}
        self.atom_collection.delete_one(atom_delete_id)

    def update(self,atom_id,atom):
        update_atom_id={"id":atom_id}
        update_data={"$set":{"atom":atom}}
        self.atom_collection.update_many(update_atom_id,update_data)

    def retrieve_by_id(self,atom_id):
        atom_list = []
        retrieve_atom_id={"id":atom_id}
        atom_data=self.atom_collection.find(retrieve_atom_id,{"_id":0})
        for atom in atom_data:
           atom_list.append(atom)
        return  json.dumps(atom_list)

    def retrieve_all(self):
        atom_list = []
        atom_data = self.atom_collection.find({},{"_id": 0})
        for atom in atom_data:
            atom_list.append(atom)
        return json.dumps(atom_list)

    def get_id(self):
        s=self.atom_collection.find_one(sort=[("id", -1)])
        id=s['id']+1
        self.atom_collection.update({"id":id},{"$inc": {"id": 1}})
        return id
