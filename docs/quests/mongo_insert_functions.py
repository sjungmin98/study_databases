# fruit_info_list = [
#     {"name": "Apple", "color": "Red", "origin": "Asia"},
#     {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
#     {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
#     {"name": "Grapes", "color": "Purple", "origin": "Europe"}]

from pymongo import MongoClient

# Connect to MongoDB
mongoclient = MongoClient("mongodb://localhost:27017/")
database = mongoclient["local"]  # 로컬로 연결한거 변수로 받음
collection = database["fruits"]  # 로컬안에 있는 fruit docutment 변수로 받음

def insert_fruit(fruit):
    collection.insert_one(fruit)

# 과일 리스트
fruit_info_list = [
    {"name": "Apple", "color": "Red", "origin": "Asia"},
    {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
    {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
    {"name": "Grapes", "color": "Purple", "origin": "Europe"}]


# 각각의 정보를 mongoDB로 insert
for fruit in fruit_info_list:
    insert_fruit(fruit)
pass
    