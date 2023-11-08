# 자료구조개론 4주차 과제2
# Linked List 구현
#
# 미래모빌리티학과
# 2021271402 이지오


# import module for call main
import sys

# global variable
head: id = None
size: int = 0


# 1. Node 클래스 정의 :
# - member field : data 필드, link 필드
class Node:
    data: any
    link: id = None

    def __init__(self, data: any) -> None:
        self.data = data


# - data 필드 : computerArray = [keyboard, mouse, monitor, printer, scanner]
computerArray = ["keyboard", "mouse", "monitor", "printer", "scanner"]


# 2. Node 클래스로 부터 node들을 생성 후 data 필드, link 필드를 fill하여 linked list를 완성
def default_list() -> None:
    clear_list()
    for element in computerArray:
        add_Node(element)


# 3. 필요한 함수 작성
# ① isEmpty() : 빈 linked list인가?
def isEmpty() -> bool:
    if head == None:
        return True
    else:
        return False


# ② clear_list() : linked list 초기화
def clear_list() -> None:
    global head, size
    head = None
    size = 0
    # print("list is cleared")


# ③ size_of_list() : linked list의 node 개수
def size_of_list() -> int:
    global size
    return size


# ④ print_linked_list() : linked list의 node 출력
def print_linked_list() -> None:
    if isEmpty():
        print("linked list is now empty.")
        return
    global head
    current_node = head
    print("[", end='')
    for i in range(size_of_list()):
        print(current_node.data, end='')
        if i != size_of_list() - 1:
            print(end=", ")
        current_node = current_node.link
    print("]")


# (추가) index의 범위를 확인하는 함수
def int_to_index(index: int) -> int:
    last_index = size_of_list() - 1

    if index >= 0 and index <= last_index:  # index 범위 내일때
        return index
    elif index < 0 and index >= -size_of_list():  # 뒤에서부터 일때
        return last_index + index + 1
    elif (index == 0 or index == -1) and isEmpty(): # Empty인데 처음 혹은 끝을 요구했을때
        return -1
    else:
        raise IndexError("Out of list index range.")


# (추가) add_Node() : 새로운 node 추가
# -> add와 insert의 작동방식이 달라 구분
def add_Node(data: any) -> None:
    global head, size
    new_node = Node(data)
    if isEmpty():
        head = new_node
    else:
        before_node = head
        for i in range(size_of_list() - 1):
            before_node = before_node.link
        before_node.link = new_node
    # print(f"\nadd [{data}] in linked list")
    size += 1


# ⑤ insert_Node() : 새로운 node 삽입
def insert_Node(data: any, index: int = -1) -> None:
    global head, size
    index = int_to_index(index)
    new_node = Node(data)
    if isEmpty():
        head = new_node
    else:
        if index == 0:
            next_node = head
            head = new_node
        else:
            before_node = head
            for i in range(index - 1):
                before_node = before_node.link
            next_node = before_node.link
            before_node.link = new_node
        new_node.link = next_node
    # print(f"\ninsert [{data}] in linked list")
    size += 1


# ⑥ delete_Node() : node 삭제
def delete_Node(index: int = -1) -> None:
    global head, size
    index = int_to_index(index)
    if index == -1:
        raise IndexError("There is nothing to delete.")
    elif index == 0:
        delete_node = head
        head = delete_node.link
    else:
        before_node = head
        for i in range(index - 1):
            before_node = before_node.link
        delete_node = before_node.link
        before_node.link = delete_node.link
    # print(f"\ndelete [{delete_node.data}] in linked list")
    size -= 1


# ⑦ find_Node() : node 검색
def find_Node(data: str = None, index: int = None) -> None:
    global head
    print()
    if data == None and index != None:
        index = int_to_index(index)
        if index == -1:
            print("List is Empty.")
        current_node = head
        for i in range(index):
            current_node = current_node.link
        print(f"index:{index} = [{current_node.data}]")

    elif data != None and index == None:
        current_node = head
        find = False
        for i in range(size_of_list()):
            if data in str(current_node.data):
                print(f"index:{i} = {current_node.data}")
                find = True
            current_node = current_node.link
        if not find:
            print(f"Can't find [{data}] in linked list.")
    else:
        raise ValueError("Wrong value!")

# main 함수


def main() -> int:
    # 초기화
    default_list()

    while True:
        try:
            print()
            print(f"Now {size_of_list()} item(s) in linked_list : ")
            print_linked_list()
            print()
            print("===== Linked List =====")
            print("1. Add item in list.")
            print("2. Insert item in list.")
            print("3. Delete item in list.")
            print("4. Find items in list.")
            print("5. Reset list to default.")
            print("6. Exit")
            print("=" * 22)
            select = input("Select the menu >> ")
            print()

            # 메뉴에 맞는 동작 구성
            if select == '1' or select.lower() == "add":
                add_Node(input("[Add] Enter the name of the item >> "))

            elif select == '2' or select.lower() == "insert":
                index = int(
                    input("[Insert] Enter the index number you want to insert >> "))
                insert_Node(input(
                    "[Insert] Enter the name of the item >> "), index)

            elif select == '3' or select.lower() == "delete":
                delete_Node(
                    int(input("[Delete] Enter the index number you want to delete >> ")))

            elif select == '4' or select.lower() == "find":
                print("[Find] Enter the number you want to find: ")
                select = input(
                    "1) Index to Data 2) Data to Index >> ")
                if select == '1' or select.lower() == "index to data" or select.lower() == "index":
                    find_Node(
                        index=int(input("[Find] Enter the index number you want to find >> ")))
                elif select == '2' or select.lower() == "data to index" or select.lower() == "data":
                    find_Node(data=input(
                        "[Find] Enter the data you want to find >> "))
                else:
                    raise ValueError("Wrong Input!")

            elif select == '5' or select.lower() == "reset":
                default_list()

            elif select == '6' or select.lower() == "exit" or select.lower() == "quit" or select.lower() == "end":
                print("Good Bye!")
                return 0
            else:
                raise ValueError("Wrong Input!")

        except Exception as e:
            print()
            print("Error : ", e)


# main 함수 호출
if __name__ == "__main__":
    sys.exit(main())
