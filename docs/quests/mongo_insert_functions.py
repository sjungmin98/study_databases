# fruit_info_list = [
#     {"name": "Apple", "color": "Red", "origin": "Asia"},
#     {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
#     {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
#     {"name": "Grapes", "color": "Purple", "origin": "Europe"}]

# Connect to MongoDB
def connect_mongo(link, database_name, collection_name): 
    from pymongo import MongoClient
    mongoclient = MongoClient(link)
    database = mongoclient[database_name]  # 로컬로 연결한거 변수로 받음
    return database[collection_name]  # 로컬안에 있는 fruit docutment 변수로 받음

def insert_fruit(fruit):
    collection.insert_one(fruit)

# 과일 리스트
fruit_info_list = [
    {"name": "Apple", "color": "Red", "origin": "Asia"},
    {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
    {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
    {"name": "Grapes", "color": "Purple", "origin": "Europe"}]

collection = connect_mongo("mongodb://localhost:27017", "local", "fruits")

# 각각의 정보를 mongoDB로 insert
for fruit in [0, 1, 2, 3]:
    fruit_list = fruit_info_list[fruit]
    insert_fruit(fruit_list)
pass