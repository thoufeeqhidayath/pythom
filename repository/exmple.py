from pymongo import MongoClient

client=MongoClient("localHost",27017)
database=client['skan']
collection=database['users']

str=collection.find_and_modify(update={"$inc":{"users_id":1}})


print str['users_id']


