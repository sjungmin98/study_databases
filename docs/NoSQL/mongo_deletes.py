from pymongo import MongoClient

# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert many 작업 진행
list_fruits = [
    {"name": "Apple", "color": "Red", "origin": "Asia"},
    {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
    {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
    {"name": "Grapes", "color": "Purple", "origin": "Europe"}
]
inserted_result = collection.insert_many(list_fruits)

list_inserted_ids = inserted_result.inserted_ids

# delete inserted records by _ids
delete_result = collection.delete_many({"_id": {list_inserted_ids[0]}})
pass
