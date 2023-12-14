from solvingProblems_main import connect_to_mongodb

def question_choices_from_mongodb(collection, max_questions=5):
    # MongoDB에서 문제와 선택지를 가져오는 함수
    # 쿼리 작성
    query = {}

    # 프로젝션 작성
    projection = {'question': 1, 'choices': 1, 'answer_number': 1, 'user_answer': 1, '_id': 0}

    # 쿼리 실행
    result = collection.find(query, projection)
    result = list(result)  

    # 결과 출력
    question_number = 1
    correct_answers = 0  # 정답 개수 초기화

    for document in result:
        # 문제 출력
        print("문제{}. {}".format(question_number, document['question']))
        
        # 선택지 출력
        choice_number = 1
        for choice in document['choices']:
            print("{}. {}".format(choice_number, choice))
            choice_number += 1
        
        # 사용자 입력 받기
        user_answer = input("답을 입력하세요 : ")

        # 정답 확인
        if 'answer_number' in document and int(user_answer) == document['answer_number'] :
            print("정답입니다!")
            correct_answers += 1
        else:
            print("틀렸습니다!")

        question_number += 1

        # 일정 개수의 문제를 출제하고 종료
        if question_number > max_questions :
            break

    return correct_answers

def calculate_final_score(correct_answers) :
    # 정답 개수에 따라 최종 점수 계산
    final_score = correct_answers * 20
    if final_score > 100 :
        final_score = 100
    return final_score

# 문제와 답안 출력 및 사용자 입력
database_name = 'local'
collection_name = 'solvingproblem'
collection = connect_to_mongodb(database_name, collection_name)
correct_answers = question_choices_from_mongodb(collection, max_questions=5)

# 최종 점수 계산 및 출력
final_score = calculate_final_score(correct_answers)
print("최종 점수 : {}".format(final_score))