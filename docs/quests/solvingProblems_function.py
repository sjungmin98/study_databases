# fruit_info_list = [
#     {"name": "Apple", "color": "Red", "origin": "Asia"},
#     {"name": "Banana", "color": "Yellow", "origin": "Southeast Asia"},
#     {"name": "Orange", "color": "Orange", "origin": "Southeast Asia"},
#     {"name": "Grapes", "color": "Purple", "origin": "Europe"}]

# Connect to MongoDB
def connect_mongo(link, database_name, collection_name): 
    from pymongo import MongoClient
    mongoclient = MongoClient(link)
    database = mongoclient[database_name]  
    return database[collection_name]  

def input_quiz(quiz):
    collection.insert_one(quiz)


quiz_list = [
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "score": 20
    },
    {
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "score": 20
    }
]


collection = connect_mongo("mongodb://localhost:27017", "local", "solvingproblem")

# 각각의 정보를 mongoDB로 insert
for quiz in [0, 1, 2, 3, 4]:
    quiz_info_list = quiz_list[quiz]
    input_quiz(quiz_info_list)
pass