from pymongo import MongoClient

def connect_and_select():
    # MongoDB에 연결하고 컬렉션들을 선택하는 함수
    client = MongoClient('mongodb://localhost:27017/')
    database = client['local']
    todos_collection = database['todos_list']  
    part_collection = database['participants']  
    part_todos_collection = database['participants_todos']  
    return todos_collection, part_collection, part_todos_collection

def init_todo_list(todos_collection, part_todos_collection):
    # 참여자들의 할 일 목록을 초기화하는 함수
    part_todos_collection.delete_many({}) 
    todo_list = [todo['title'] for todo in todos_collection.find()]  # 'todos_list' 컬렉션의 모든 할 일의 제목을 리스트로 만듦
    return todo_list

def get_participants(part_collection, name):
    # 참여자 이름을 통해 MongoDB에서 해당 참여자 정보를 검색하는 함수
    participant = part_collection.find_one({ "name": name })  # 이름이 일치하는 참여자를 찾음
    if participant is None:
        print("{}은(는) 참여자 목록에 없습니다.".format(name))
    return participant

def update_participants(part_collection, name, title, status):
    # 참여자의 설문 응답을 업데이트하는 함수
    # "$addToSet" 연산자는 주어진 값을 배열 필드에 추가하는데, 값이 이미 배열에 존재하면 아무 작업도 수행하지 않음.
    # 따라서 이 연산자를 사용하면, 중복 없이 설문 응답을 "Titles" 배열에 추가
    part_collection.update_one(
        { "name": name },
        { 
            "$addToSet": {
                "Titles": {
                    "Title": title,
                    "status": status
                }
            }
        }
    )

def add_todos(todos_collection, todo_list):
    # 'title'과 'description' 키를 가진 dictionary의 list를 받음
    for todo in todo_list:
        # 각 할 일에서 'title'과 'description'을 추출
        title = todo['title']
        description = todo['description']
        # 만약 해당 'title'을 가진 할 일이 todos_collection에 없다면
        if todos_collection.find_one({"title": title}) is None:
            # 새로운 할 일을 todos_collection에 추가
            todos_collection.insert_one({"title": title, "description": description})

def add_participants(part_collection, participants):
    # 'name' 키를 가진 dictionary의 list를 받음
    for participant in participants:
        # 각 참가자에서 'name'을 추출
        name = participant['name']
        # 만약 해당 'name'을 가진 참가자가 part_collection에 없다면
        if part_collection.find_one({"name": name}) is None:
            # 새로운 참가자를 part_collection에 추가
            # 이 때 참가자는 아직 어떤 할 일도 가지고 있지 않으므로 "Titles"는 빈 리스트로 설정
            part_collection.insert_one({"name": name, "Titles": []})

def reset_participants_titles(part_collection):
    # 참여자들의 'Titles' 필드를 초기화하는 함수
    part_collection.update_many({}, {"$set": {"Titles": []}})

def run_todo_list():
    todos_collection, part_collection, part_todos_collection = connect_and_select()
    reset_participants_titles(part_collection)  # 참여자들의 'Titles' 필드 초기화
    todo_list = init_todo_list(todos_collection, part_todos_collection)
    name = input("Input Your Name: ")  
    
    participant = get_participants(part_collection, name)  
    if participant is None:  
        return  

    while True:
        print("ToDo List 중 하나 선택하세요!")
        i = 1
        for todo in todo_list:  
            print(str(i) + ". " + todo)
            i += 1
        title_index = int(input("Title 번호: ")) - 1  
        status = input("Status: ")  

        title = todo_list[title_index]  

        # 참여자의 할 일과 설문 응답을 'participants_todos' 컬렉션에 추가
        part_todos_collection.insert_one({
            "name": name,
            "Title": title,
            "status": status,
            "object_id": participant['_id']
        })
        update_participants(part_collection, name, title, status)  # 참여자의 설문 응답 업데이트

        quit_input = input("종료 여부: ") 
        print("------------------------")
        if quit_input == 'x':  
            print("프로그렘이 종료되었습니다.")
            return  
        elif quit_input == 'q':  
            name = input("Input Your Name: ")  
            participant = get_participants(part_collection, name) 
            if participant is None:  
                return 
run_todo_list()