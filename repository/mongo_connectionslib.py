from pymongo import MongoClient
import db_config

class MongoConnections:
    def __init__(self):
        self.db_connection = MongoClient(db_config.host, db_config.server)
        self.database = self.db_connection[db_config.database]

    def get_atom_connection(self):
        database = self.db_connection[db_config.atom_db]
        collection=database['Atom']
        return collection


    def molecule_connection(self):
        database = self.db_connection[db_config.skan_db]
        collection = database['MoleculeModel']
        return collection

    def get_process_run_connection(self):
        database = self.db_connection[db_config.process_run_db]
        collection = database['ProcessRuns']
        return collection

    def get_process_model_connection(self):
        database = self.db_connection[db_config.skan_db]
        collection = database['ProcessModel']
        return collection

    def get_compound_connection(self):
        database = self.db_connection[db_config.skan_db]
        collection = database['CompoundModel']
        return collection

    def user_connection(self):
        database = self.db_connection[db_config.skan_db]
        collection = database['Users']
        return collection



