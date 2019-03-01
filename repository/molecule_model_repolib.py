import json

from pymongo import MongoClient

from repository import mongo_connectionslib, db_config


class MoleculeModel_RepoLib:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection['SkanDB']
        self.molecule_collection = self.database['MoleculeModel']


    def create(self, molecule):
        id = int(self.get_molecule_id())
        user_data = {"id": id, "molecule": molecule}
        self.molecule_collection.insert_one(user_data)

    def update(self, molecule_id, molecule):
        update_id = {"id": molecule_id}
        update_molecule = {"$set": {"molecule": molecule}}
        self.molecule_collection.update_many(update_id, update_molecule)

    def delete(self, molecule_id):
        delete_id = {"id": molecule_id}
        self.molecule_collection.delete_many(delete_id)

    def retrieve_all(self):
        molecule_list = []
        molecule_data = self.molecule_collection.find({}, {"_id": 0})
        for molecule in molecule_data:
            molecule_list.append(json.dumps(molecule))
        return molecule_list

    def retrieve_by_id(self, molecule_id):
        molecule_list = []
        molecule_id = {"id": molecule_id}
        molecule_data = self.molecule_collection.find(molecule_id, {"_id": 0})
        for molecule in molecule_data:
            molecule_list.append(json.dumps(molecule))
        return molecule_list

    def get_molecule_id(self):
        #s = self.molecule_collection.find_one(sort=[("id", -1)])
        #id = s['id'] + 1
        #atom_data = self.molecule_collection.find_and_modify(update={"$inc": {"id": 1}})
        #return id
        s = self.molecule_collection.find_one(sort=[("id", -1)])
        id = s['id'] + 1
        self.molecule_collection.update({"id": id}, {"$inc": {"id": 1}})
        return id