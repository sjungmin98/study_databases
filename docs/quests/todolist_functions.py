# MongoClient 모듈을 import
from pymongo import MongoClient

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

# MongoDB에서 문제와 선택지를 가져와서 사용자에게 문제를 출제하고 답을 받는 함수
def question_choices_from_mongodb(collection):
    user_name = input("이름을 입력해 주세요 : ")  # 사용자 이름 입력 받기

    query = {}  # MongoDB에서 모든 문서를 선택하기 위한 빈 쿼리(딕셔너리) 생성
    
    # 필요한 필드만 선택하기 위한 프로젝션 생성
    # 프로젝션 : 한 document 전체를 선택하는 것이 아니라, 특정 필요한 데이터를 선택하는 것
    projection = {'title': 1, 'description': 1, 'answer_number': 1, '_id': 1}  
                                                                            
    # 쿼리와 프로젝션을 사용하여 MongoDB에서 데이터를 가져옴
    result = collection.find(query, projection)
    result = list(result)  # 결과를 리스트로 변환








def get_mixed_questions():
    
    list_mixed_questions = []

    # input 기능 추가
    for inputs in range(3):
        question = input("question : ")

        list_mixed_answers = []
        
        answer = input("answer : ")
        list_mixed_answers.append(answer)
        correct_index = input("correct_index : ")
        score = input("score : ")

        # 입력값을 딕셔너리로 저장
        dict_mixed_questions = {
            'question': question,
            'answer': list_mixed_answers,
            'correct_index': correct_index,
            'score': score
        }
        list_mixed_questions.append(dict_mixed_questions)

    return list_mixed_questions

mixed_questions_data = get_mixed_questions()

def print_mixed_questions(list_mixed_questions):
    
    # 입력값 출력
    for mixed_questions in list_mixed_questions:
        print("\"question\" : {}".format(mixed_questions['question']))
        print("\"answer\" : {}".format(mixed_questions['answer']))
        print("\"correct_index\" : {}".format(mixed_questions['correct_index']))
        print("\"score\" : {}".format(mixed_questions['score']))

# 함수 호출
print_mixed_questions(get_mixed_questions())