import solvingProblems_function

# MongoDB에 연결
database_name = 'local'
collection_name = 'solvingproblem'
collection = solvingProblems_function.connect_to_mongodb(database_name, collection_name)

# MongoDB 컬렉션의 모든 문서를 삭제하여 초기화
collection.delete_many({})

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
solvingProblems_function.insert_quiz_data(collection, quiz_list)

# 문제를 출제하고, 사용자의 답을 받아 정답 개수를 계산
correct_answers = solvingProblems_function.question_choices_from_mongodb(collection)

# 최종 점수를 계산
final_score = solvingProblems_function.calculate_final_score(correct_answers)

# 최종 점수를 출력
print("최종 점수: {}".format(final_score))