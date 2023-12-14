# solvingProblems_main 모듈에서 connect_to_mongodb와 insert_quiz_list 함수를 가져옴
from solvingProblems_main import connect_to_mongodb, insert_quiz_list

# MongoDB에서 문제와 선택지를 가져와서 사용자에게 문제를 출제하고 답을 받는 함수
def question_choices_from_mongodb(collection):
    user_name = input("이름을 입력해 주세요: ")  # 사용자 이름 입력 받기

    query = {}  # MongoDB에서 모든 문서를 선택하기 위한 빈 쿼리(딕셔너리) 생성
    
    # 필요한 필드만 선택하기 위한 프로젝션 생성
    # 프로젝션 : 한 document 전체를 선택하는 것이 아니라, 특정 필요한 데이터를 선택하는 것
    projection = {'question': 1, 'choices': 1, 'answer_number': 1, '_id': 1}  
                                                                            
    # 쿼리와 프로젝션을 사용하여 MongoDB에서 데이터를 가져옴
    result = collection.find(query, projection)
    result = list(result)  # 결과를 리스트로 변환

    question_number = 1  # 문제 번호 초기화
    correct_answers = 0  # 정답 개수 초기화

    # 각 문서에 대해
    for document in result:
        question = document['question']  # 문제를 가져옴
        choices = document['choices']  # 선택지를 가져옴

        # 문제를 출력
        print("문제{}. {}".format(question_number, question))

        # 각 보기에 대해
        choice_number = 1  # 보기 번호 초기화
        for choice in choices:
            # 보기를 출력
            print("{}. {}".format(choice_number, choice))
            choice_number += 1  # 선택지 번호를 하나 증가시킴

        # 사용자로부터 답을 입력 받음
        user_answer = int(input("답을 입력하세요 : "))

        # 문서(document)에 'answer_number' 키가 있는지 확인
        if 'answer_number' in document:
            # 사용자가 입력한 답(int(user_answer))과 문서에 저장된 정답(document['answer_number'])을 비교
            if int(user_answer) == document['answer_number']:
                # 사용자가 입력한 답과 문서에 저장된 정답이 일치하는 경우, 즉 정답인 경우
                print("정답입니다!")
                correct_answers += 1  # 정답 개수를 증가시킵니다.
            else:
                # 사용자가 입력한 답과 문서에 저장된 정답이 일치하지 않는 경우, 즉 오답인 경우
                print("틀렸습니다!")

        # MongoDB에 사용자의 이름과 답을 저장
        #  $set은 MongoDB의 update 연산자 중 하나로, 특정 필드의 값을 변경하거나 새 필드를 추가할 때 사용
        #  _id: MongoDB에서 document는 고유한 _id 필드 자동으로 생성, _id 필드를 사용하면 특정 문서를 쉽게 찾을 수 있음
        collection.update_one({'_id': document['_id']}, {"$set": {user_name: user_answer}})

        question_number += 1  # 문제 번호를 하나 증가시킴

    return correct_answers  # 정답 개수를 반환

# 정답 개수에 따라 최종 점수를 계산하는 함수
def calculate_final_score(correct_answers):
    final_score = correct_answers * 20  # 정답 개수에 20을 곱하여 점수를 계산
    if final_score > 100:  # 점수가 100을 초과하면
        final_score = 100  # 점수를 100으로 조정
    return final_score  # 최종 점수를 반환

# MongoDB에 연결하고, 문제 리스트를 가져옴
collection = connect_to_mongodb(database_name, collection_name)
quiz_list = insert_quiz_list(collection)

# 문제를 출제하고, 사용자의 답을 받아 정답 개수를 계산
correct_answers = question_choices_from_mongodb(collection)

# 최종 점수를 계산
final_score = calculate_final_score(correct_answers)

# 최종 점수를 출력
print("최종 점수 : {}".format(final_score))
