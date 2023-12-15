import solvingProblems_function

# MongoDB에 연결
database_name = 'local'
collection_name = 'solvingproblem'
collection = solvingProblems_function.connect_to_mongodb(database_name, collection_name)

# MongoDB 컬렉션의 모든 문서를 삭제하여 초기화
collection.delete_many({})

# 퀴즈 데이터를 MongoDB에 삽입
solvingProblems_function.insert_quiz_data(collection, solvingProblems_function.quiz_list)

# 문제를 출제하고, 사용자의 답을 받아 정답 개수를 계산
correct_answers = solvingProblems_function.question_choices_from_mongodb(collection)

# 최종 점수를 계산
final_score = solvingProblems_function.calculate_final_score(correct_answers)

# 최종 점수를 출력
print("최종 점수 : {}".format(final_score))