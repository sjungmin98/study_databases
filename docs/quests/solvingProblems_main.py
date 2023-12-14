from pymongo import MongoClient

# 기본 데이터베이스와 컬렉션 이름
database_name = 'local'
collection_name = 'solvingproblem'

def connect_to_mongodb(database_name, collection_name):
    # MongoDB에 연결하는 함수
    # MongoClient를 이용해 MongoDB 서버에 접속
    client = MongoClient('mongodb://localhost:27017/') 

    # 데이터베이스 선택
    database = client[database_name]
    
    # 컬렉션 선택 (없으면 새로 생성)
    collection = database[collection_name]

    return collection

def insert_quiz_data(collection, quiz_list):
    # MongoDB에 데이터를 삽입
    collection.insert_many(quiz_list)

# MongoDB에 연결
# 기본적으로 'local' 데이터베이스, 'solvingproblem' 컬렉션을 사용
collection = connect_to_mongodb(database_name, collection_name)

# 삽입할 퀴즈 데이터
quiz_list = [
    {
        "question": "Python의 생성자 함수 이름은 무엇인가요?",
        "choices": ["__init__", "__main__", "__str__", "__del__"],
        "answer": "__init__",
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
        "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
        "answer": "print('Hello, World!')",
        "answer_number": 1,
        "score": 20
    },
    {
        "question": "Python에서 주석을 나타내는 기호는 무엇인가요?",
        "choices": ["//", "/* */", "#", "--"],
        "answer": "#",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
        "choices": ["size()", "length()", "len()", "sizeof()"],
        "answer": "len()",
        "answer_number": 3,
        "score": 20
    },
    {
        "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
        "choices": ["str()", "int()", "char()", "float()"],
        "answer": "int()",
        "answer_number": 2,
        "score": 20
    }
]

# 퀴즈 데이터 삽입
insert_quiz_data(collection, quiz_list)