# 자료구조개론 5주차 과제3
# Circular Linked List 구현
#
# 미래모빌리티학과
# 2021271402 이지오

# import sys for call main
import sys


# 1. Node 클래스 정의 :
# - member field : data 필드, link 필드
class Node:
    data: any
    link: id

    def __init__(self, data: any) -> None:
        self.data = data
        self.link = None


# - data 필드 : computerArray = [keyboard, mouse, monitor, printer, scanner]
computerArray = ["keyboard", "mouse", "monitor", "printer", "scanner"]


# 2. Node 클래스로 부터 node들을 생성 후 data 필드, link 필드를 fill하여 Circular linked list를 완성
class Circular_List:
    head: id
    tail: id
    current: id
    previous: id
    size: int = 0

    def __init__(self, items: list = None) -> None:
        self.clear_list(items)

    # 3. 필요한 함수 작성
    # ① isEmpty() : 빈 linked list인가?
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        else:
            return False

    # ② clear_list() : linked list 초기화
    def clear_list(self, items: list = None) -> None:
        self.head = None
        self.tail = None
        self.current = None
        self.previous = None
        self.size = 0
        # print("Cleared circular list.")
        if type(items) == list:
            for item in items:
                self.add_Node(item)

    # ③ size_of_list() : linked list의 node 개수
    def size_of_list(self) -> int:
        return self.size

    # ④ print_linked_list() : linked list의 node 출력
    def print_linked_list(self) -> None:
        if self.isEmpty():
            print("List is now empty.")
        else:
            self.current = self.head
            print(f"[\"{self.current.data}\"", end="")
            for i in range(self.size_of_list() - 1):
                self.previous = self.current
                self.current = self.current.link
                print(f", \"{self.current.data}\"", end="")
            print("]")

    # add_Node() : 새로운 node 추가
    def add_Node(self, data: any) -> None:
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.link = self.tail.link
            self.tail.link = new_node
        self.tail = new_node
        self.size += 1

    # check_index() : index가 현재 list의 범위 안에 있는지 확인
    def check_index(self, index: int) -> int:
        last_index = self.size_of_list() - 1

        if (index == 0 or index == -1) and self.isEmpty():  # Empty인데 처음 혹은 끝을 요구했을때
            return -1
        elif index >= 0 and index <= last_index:  # index 범위 내일때
            return index
        elif index < 0 and index >= -self.size_of_list():  # 뒤에서부터 일때
            return last_index + index + 1
        else:
            raise IndexError("Out of list index range.")

    # ⑤ insert_Node() : 새로운 node 삽입
    def insert_Node(self, data: any, index: int) -> None:
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            index = self.check_index(index)
            self.current = self.head
            self.previous = self.tail
            for i in range(index):
                self.previous = self.current
                self.current = self.current.link
            new_node.link = self.current
            self.previous.link = new_node
            if index == 0:
                self.head = new_node
        self.size += 1

    # ⑥ delete_Node() : node 삭제
    def delete_Node(self, index: int) -> None:
        if self.isEmpty():
            raise ValueError("There is nothing to delete!")
        else:
            index = self.check_index(index)
            self.current = self.head
            self.previous = self.tail
            for i in range(index):
                self.previous = self.current
                self.current = self.current.link
            self.previous.link = self.current.link
            if index == 0:
                self.head = self.current.link
            if index == self.size_of_list() - 1:
                self.tail = self.previous
        self.size -= 1

    # ⑦ find_Node() : node 검색
    def find_Node(self, data: str = None, index: int = None) -> None:
        print()
        if data == None and index != None:
            index = self.check_index(index)
            if index == -1:
                print("List is Empty.")
            self.current = self.head
            for i in range(index):
                self.current = self.current.link
            print(f"index:{index} = [{self.current.data}]")

        elif data != None and index == None:
            self.current = self.head
            find = False
            for i in range(self.size_of_list()):
                if data in str(self.current.data):
                    print(f"index:{i} = {self.current.data}")
                    find = True
                self.current = self.current.link
            if not find:
                print(f"Can't find [{data}] in circular list.")
        else:
            raise ValueError("Wrong value!")


def main() -> int:
    circular_list = Circular_List(computerArray)
    while True:
        try:
            print()
            print(
                f"Now {circular_list.size_of_list()} item(s) in circular list : ")
            circular_list.print_linked_list()
            print()
            print("===== Linked List =====")
            print("1. Add item in list.")
            print("2. Insert item in list.")
            print("3. Delete item in list.")
            print("4. Find items in list.")
            print("5. Clear list.")
            print("6. Reset list to default.")
            print("7. Exit")
            print("=" * 22)
            select = input("Select the menu >> ")
            print()

            # 메뉴에 맞는 동작 구성
            # Add Item
            if select == '1' or select.lower() == "add":
                circular_list.add_Node(
                    input("[Add] Enter the name of the item >> "))

            # Insert Item
            elif select == '2' or select.lower() == "insert":
                index = int(
                    input("[Insert] Enter the index number you want to insert >> "))
                circular_list.insert_Node(input(
                    "[Insert] Enter the name of the item >> "), index)

            # Delete Item
            elif select == '3' or select.lower() == "delete":
                circular_list.delete_Node(
                    int(input("[Delete] Enter the index number you want to delete >> ")))

            # Find Item
            elif select == '4' or select.lower() == "find":
                print("[Find] Enter the number you want to find: ")
                select = input(
                    "1) Index to Data 2) Data to Index >> ")
                if select == '1' or select.lower() == "index to data" or select.lower() == "index":
                    circular_list.find_Node(
                        index=int(input("[Find] Enter the index number you want to find >> ")))
                elif select == '2' or select.lower() == "data to index" or select.lower() == "data":
                    circular_list.find_Node(data=input(
                        "[Find] Enter the data you want to find >> "))
                else:
                    raise ValueError("Wrong Input!")

            # Clear
            elif select == '5' or select.lower() == "clear":
                circular_list.clear_list()

            # Reset
            elif select == '6' or select.lower() == "reset":
                circular_list.clear_list(computerArray)

            # Exit
            elif select == '7' or select.lower() == "exit" or select.lower() == "quit" or select.lower() == "end":
                print("Good Bye!")
                return 0
            else:
                raise ValueError("Wrong Input!")
        except Exception as e:
            print()
            print("Error : ", e)


# call main()
if __name__ == "__main__":
    sys.exit(main())
