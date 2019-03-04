import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class AtomRepo:

    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['AtomDB']
        self.atom_collection = self.database ['Atom']


    def create(self,atom):

        try:
            id = self.get_id()
            self.atom_collection.insert({"id": id, "atom": atom})
            print "[INFO]inserted succesfully -ATOM"
            return True

        except Exception as e:
            print "[ERROR] error when inserting"
            return False



    def delete(self,atom_id):
        try:
            self.atom_collection.delete_one({"id": int(atom_id)})
            return  True
        except Exception as e:
            print"[ERROR] when deleting from atom"
            return False




    def update(self,atom_id,atom):
        try:
            self.atom_collection.update_many({"id": atom_id}, {"$set": {"atom": atom}})
            return True
        except Exception as e:
            print"[ERROR] when deleting from atom"
            return False

    def retrieve_by_id(self,atom_id):
        try:
            atom_list = []
            atom_data = self.atom_collection.find({"id": atom_id}, {"_id": 0})
            for atom in atom_data:
                atom_list.append(atom)
            return  json.dumps(atom_list)
        except Exception as e:
            print ("[ERROR] when reading data")
            return False

    def retrieve_all(self):
        try:
            atom_list = []
            atom_data = self.atom_collection.find({}, {"_id": 0})
            for atom in atom_data:
                atom_list.append(atom)
            return json.dumps(atom_list)
        except Exception as e:
            print ("[ERROR] when inserting data")
            return False

    def get_id(self):
        s=self.atom_collection.find_one(sort=[("id", -1)])
        id=s['id']+1
        self.atom_collection.update({"id":id},{"$inc": {"id": 1}})
        return id
