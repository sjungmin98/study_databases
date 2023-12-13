from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
collection.insert_one({"name": "키위", 
                       "color": "갈색", 
                       "origin": "뉴질랜드"})
dict_fruits = {{"name" : "오렌지", "color" : "주황색", "origin" : "미국"}}
collection.insert_one(dict_fruits)

pass