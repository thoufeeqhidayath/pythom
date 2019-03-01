from repository.mongo_connectionslib import MongoConnections


class ActivityRepo:
    def __init__(self):
        self.db_connection = MongoConnections.get_connction()
        self.activity_collection = self.db_connection['skan.ProcessRuns']

    def create(self,activity):
        activity_id=self.get_activity_id()
        insert_user_data={"activity_id":activity_id,"activity":activity}
        self.activity_collection.insert(insert_user_data)

    def update(self,activity_id, activity):
        update_id={"activity_id":activity_id}
        update_activity={"$set":{"activity":activity}}
        self.activity_collection.update_many(update_id,update_activity)

    def delete(self,activity_id):
        delete_id={"activity_id":activity_id}
        self.activity_collection.delete_many(delete_id)

    def retrieve_all(self):
        return self.activity_collection.find()

    def retrieve_by_id(self, activity_id):
        retrieve_id={"activity_id":activity_id}
        return self.activity_collection.find_one(retrieve_id)

    def get_activity_id(self):
        user_data = self.activity_collection.find_and_modify(update={"$inc": {"activity_id": 1}})
        return user_data['activity_id'] + 1