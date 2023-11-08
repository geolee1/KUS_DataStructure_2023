# 자료구조개론 4주차 과제1
# 선형 리스트 구현
# 
# 미래모빌리티학과
# 2021271402 이지오

# import module for call main
import sys

# 1. 동물 = []
animals_list = []


# 2. 동물 = [동물1, 동물2, 동물3, 동물4]을 만드는 동물 리스트 완성하는 함수()
#   - 빈 칸 추가 후 insert
animals = ["dog", "cat", "tiger", "elephant", "giraff"]

def add_item(item:any) -> None:
    animals_list.append(None)
    animals_list[len(animals_list) -1] = item
    # print(f"{item} is added to animals_list.")

def default_array():
    # print("Set animals_list in Default.")
    animals_list.clear()
    # print("animals_list is now cleared.")
    for item in animals:
        add_item(item)
 

# 3. 특정 위치에 새로운 동물을 삽입하는 함수()
#   - 0보다 작고, 리스트 크기보다 큰 경우 확인
#   - 빈 칸 추가 후 [맨 뒤 - 1]의 이름을 [맨 뒤]로 복사
#   - 특정 위치 뒤까지 반복
#   - 특정 위치에 insert
def insert_item(index:int, item:any) -> None:
    if index < len(animals_list) and index >= -len(animals_list):
        if index < 0:
            index = len(animals_list) + index
        animals_list.append(None)
        last_index = len(animals_list) - 1
        for i in range(last_index - index):
            animals_list[last_index - i] = animals_list[last_index - i - 1]
        animals_list[index] = item
    else:
        raise IndexError("Out of list range.")


# 4. 특정 위치의 데이터를 삭제하는 함수()
#   - 0보다 작고, 리스트 크기보다 큰 경우 확인
#   - 특정 위치의 자료 delete
#   - 특정 위치에 특정위치 다음의 자료 복사
#   - [맨 뒤]까지 복사 후 [맨 뒤]는 삭제
def delete_item(index:int) -> None:
    if index < len(animals_list) and index >= -len(animals_list):
        if index < 0:
            index = len(animals_list) + index
        last_index = len(animals_list) - 1
        for i in range(last_index - index):
            animals_list[index + i] = animals_list[index + i + 1]
        animals_list.pop(-1)
    else:
        raise IndexError("Out of list range.")


# 5. 2~4를 선택하여 각각을 수행하는 main() 함수
def main() -> int:
    # 초기화
    default_array()
    while True:
        try:
            # 메뉴 인터페이스 출력
            print()
            print(f"Now {len(animals_list)} item(s) in animals_list : ")
            print(animals_list)
            print()
            print("===== Liner List =====")
            print("1. Add item in list.")
            print("2. Insert item in list.")
            print("3. Delete item in list.")
            print("4. Reset list to default.")
            print("5. Exit")
            print("=" * 23)
            select = input("Select the menu >> ")
            print()

            # 메뉴에 맞는 동작 구성
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
                return 0
            else:
                raise ValueError("Wrong Input!")

        except Exception as e:
            print()
            print("Error : ", e)


# main 함수 호출
if __name__ == "__main__":
    sys.exit(main())