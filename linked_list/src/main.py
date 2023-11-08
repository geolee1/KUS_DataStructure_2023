import sys
import liner_list, linked_list

def main() -> int:
    while True:
        try:
            print()
            print("===== List =====")
            print("1. Liner List.")
            print("2. Linked List.")
            print("3. Exit")
            print("=" * 16)
            select = input("Select the menu >> ")
            print()

            if select == '1' or select.lower() == "liner" or select.lower() == "liner list":
                liner_list.main() 
            elif select == '2' or select.lower() == "linked" or select.lower() == "linked list":
                linked_list.main()
            elif select == '3' or select.lower() == "exit" or select.lower() == "quit" or select.lower() == "end":
                print("Good Bye!")
                return 0
            else:
                raise ValueError("Wrong Input!")
        except Exception as e:
            print()
            print("Error : ", e)
    return 0

# main 함수 호출
if __name__ == "__main__":
    sys.exit(main())