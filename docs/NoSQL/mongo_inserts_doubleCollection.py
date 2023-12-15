from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']
# insert 작업 진행
collection.insert_one({"name": "오렌지", 
                       "color": "주황색", 
                       "origin": "미국"})
# dict_fruits = {{"name" : "오렌지", "color" : "주황색", "origin" : "미국"}}
# collection.insert_one(dict_fruits)

# 분리 입력 (fruits, fruits_colors)
# insert fruits 작업 진행
mixed_fruits = {"name": "오렌지", 
                "color": ["주황색", '갈색', '노란색'],
                "origin": "미국"}
result = collection.insert_one(mixed_fruits)
pass
dict_fruit = {"name":"오렌지", 
               "origin":"미국"}
result = collection.insert_one(dict_fruit)
# insertedId("657bf1c1edcd8ea4232048cd")
print("result.inserted_id : {}".format(result.inserted_id))
inserted_id = result.inserted_id

#insert fruits_colors 작업 진행
# [{"fruits_id": ObjectId("657bf1c1edcd8ea4232048cd"), "color": "주황색"} 
# , {"fruits_id": ObjectId("657bf1c1edcd8ea4232048cd"), "color": '갈색'}, 
# , {"fruits_id": ObjectId("657bf1c1edcd8ea4232048cd"), "color": '노란색'}]

fruits_colors = [{"color": "주황색"}
                , {"color": '갈색'}
                , {"color": '노란색'}]

list_fruits_colors = list()
for dict_color in fruits_colors:
    dict_color["fruits_id"] = inserted_id
    list_fruits_colors.append(dict_color)
    pass

# collection fruits_colors
collection_fruits_colors = database["fruits_colors"]

collection_fruits_colors.insert_many(list_fruits_colors)

#find from fruits_colors
documents = collection_fruits_colors.find( {"fruits_id": {"$eq" : inserted_id}} )

pass