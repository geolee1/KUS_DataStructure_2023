# 자료구조개론 3주차 과제
# 선형 리스트 구현
# 
# 미래모빌리티학과
# 2021271402 이지오

# 1. parts_list = []
parts_list = []


# 2. computerArray = [keyboard, mouse, monitor, printer, scanner] 을 만드는 parts_list
#    완성하는 함수()
#   - 빈 칸 추가 후 insert
computerArray = ["keyboard", "mouse", "monitor", "printer", "scanner"]

def add_item(item:any) -> None:
    parts_list.append(None)
    parts_list[len(parts_list) -1] = item
    # print(f"{item} is added to parts_list.")

def default_array():
    # print("Set parts_list in Default.")
    parts_list.clear()
    # print("parts_list is now cleared.")
    for item in computerArray:
        add_item(item)
 

# 3. 특정 위치에 부속을 추가하는 함수()
#   - 0보다 작고, 리스트 크기보다 큰 경우 확인
#   - 빈 칸 추가 후 [맨 뒤 - 1]의 이름을 [맨 뒤]로 복사
def insert_item(index:int, item:any) -> None:
    if index < len(parts_list) and index >= -len(parts_list):
        if index < 0:
            index = len(parts_list) + index
        parts_list.append(None)
        last_index = len(parts_list) - 1
        for i in range(last_index - index):
            parts_list[last_index - i] = parts_list[last_index - i - 1]
        parts_list[index] = item
    else:
        print()
        print("Warning : Out of Range.")


# 4. 특정 위치의 데이터를 삭제하는 함수()
#   - 0보다 작고, 리스트 크기보다 큰 경우 확인
#   - 특정 위치의 자료 delete
#   - 특정 위치에 특정위치 다음의 자료 복사
#   - [맨 뒤]까지 복사 후 [맨 뒤]는 삭제
def delete_item(index:int) -> None:
    if index < len(parts_list) and index >= -len(parts_list):
        if index < 0:
            index = len(parts_list) + index
        last_index = len(parts_list) - 1
        for i in range(last_index - index):
            parts_list[index + i] = parts_list[index + i + 1]
        parts_list.pop(-1)
    else:
        print()
        print("Warning : Out of Range.")


# 5. 2~4를 선택하여 각각을 수행하는 main() 함수
def main() -> None:
    # 초기화
    default_array()
    while True:
        # 메뉴 인터페이스 출력
        print()
        print(f"Now {len(parts_list)} item(s) in parts_list : ")
        print(parts_list)
        print()
        print("===== Liner List =====")
        print("1. Add item in list.")
        print("2. Insert item in list.")
        print("3. Delete item in list.")
        print("4. Reset list to default.")
        print("5. Exit")
        print("=" * 22)
        select = input("Select the menu >> ")
        print()

        # 메뉴에 맞는 동작 구성
        try:
            if select == '1' or select.lower() == "add":
                add_item(input("[Add] Enter the name of the item >> "))

            elif select == '2' or select.lower() == "insert":
                index = int(input("[Insert] Enter the index number you want to insert >> "))
                insert_item(index, input("[Insert] Enter the name of the item >> "))

            elif select == '3' or select.lower() == "delete":
                delete_item(int(input("[Delete] Enter the index number you want to delete >> ")))

            elif select == '4' or select.lower() == "reset":
                default_array()

            elif select == '5' or select.lower() == "exit" or select.lower() == "quit" or select.lower() == "end":
                print("Good Bye!")
                break

            else:
                print("Warning : Wrong Input!") # 메류를 잘못 입력했을때 출력

        except:
            print()
            print("Warning : Error occurred! Try again.") # index 입력시 문자를 입력했을때 혹은 기타 오류 발생 시 작동

# main 호출
main()