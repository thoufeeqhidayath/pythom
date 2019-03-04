import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class MoleculeModel_RepoLib:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.molecule_collection = self.database['MoleculeModel']


    def create(self, molecule):
        try:
            id = int(self.get_molecule_id())
            user_data = {"id": id, "molecule": molecule}
            self.molecule_collection.insert_one(user_data)
            return True
        except Exception as e:
            print "[ERROR] while inserting Molecule"
            return False


    def update(self, molecule_id, molecule):
        try:
          self.molecule_collection.update_many( {"id": molecule_id}, {"$set": {"molecule": molecule}})
          return True
        except Exception as e:
            print("[ERROR] while updating")
            return False

    def delete(self, molecule_id):
        try:
            self.molecule_collection.delete_many({"id": molecule_id})
            return True
        except Exception as e:
            print ("[ERROR] while deleting from mole`")
            return False




    def retrieve_all(self):
        try:
            molecule_list = []
            molecule_data = self.molecule_collection.find({}, {"_id": 0})
            for molecule in molecule_data:
                molecule_list.append(json.dumps(molecule))
            return molecule_list
        except Exception as e:
            print ("[ERROR] while retrieving data`")
            return False

    def retrieve_by_id(self, molecule_id):
        try:
            molecule_list = []
            molecule_data = self.molecule_collection.find({"id": molecule_id}, {"_id": 0})
            for molecule in molecule_data:
                molecule_list.append(json.dumps(molecule))
            return molecule_list
        except Exception as e:
            print ("[ERROR] while retrieving data`")
            return False

    def get_molecule_id(self):

        s = self.molecule_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.molecule_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id