# MongoClient 모듈을 import
from pymongo import MongoClient

# 데이터베이스 및 컬렉션 이름을 설정
database_name = 'local'
collection_name = 'solvingproblem'

# MongoDB에 연결하고 지정된 데이터베이스와 컬렉션에 연결하는 함수를 정의
def connect_to_mongodb(database_name, collection_name):
    # MongoClient를 사용하여 로컬호스트의 MongoDB에 연결
    client = MongoClient('mongodb://localhost:27017/')
    # 지정된 데이터베이스를 선택
    database = client[database_name]
    # 지정된 컬렉션을 선택
    collection = database[collection_name]
    # 컬렉션 변수를 반환
    return collection

# 퀴즈 데이터를 MongoDB에 삽입하는 함수를 정의
def insert_quiz_data(collection, quiz_list):
    # 퀴즈 리스트의 각 퀴즈에 대해
    for quiz in quiz_list:
        # 동일한 데이터를 중복시키지 않기 위해 count.documents 사용
        ## 만약 동일한 경우가 없다면
        if collection.count_documents({'question': quiz['question'], 
                                       'choices': quiz['choices'], 
                                       'answer': quiz['answer'], 
                                       'answer_number': quiz['answer_number'], 
                                       'score': x['score']}) == 0:
            # 퀴즈를 컬렉션에 삽입
            collection.insert_one(quiz)

# MongoDB에 연결하고 지정된 데이터베이스와 컬렉션에 연결
collection = connect_to_mongodb(database_name, collection_name)

# 삽입할 퀴즈 데이터를 정의
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
        "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
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

# 퀴즈 데이터를 MongoDB에 삽입
insert_quiz_data(collection, quiz_list)
