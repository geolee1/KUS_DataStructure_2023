# 자료구조개론 6주차 과제4
# Stack 구현
#
# 미래모빌리티학과
# 2021271402 이지오

# module containing
import sys


# Stack
class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.clear()
    
    def is_empty(self) -> bool:
        return self._top is None
    
    def push(self, data) -> None:
        new_node = Node(data)
        if not self.is_empty():
            new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self) -> any:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        pop_node = self._top
        self._top = pop_node.next
        pop_node.next = None
        self._size -= 1
        return pop_node.data
    
    def peek(self) -> any:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._top.data
    
    def clear(self) -> None:
        self._top = None
        self._size = 0
        
    def __len__(self) -> int:
        return self._size
    
    def __iter__(self) -> any:
        self._current = self._top
        return self
    
    def __next__(self) -> None:
        if self._current is None:
            raise StopIteration
        result = self._current.data
        self._current = self._current.next
        return result
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        result = [str(item) for item in self]
        result.reverse()
        return ", ".join(result)
    

# 괄호 검사 프로그램
open_bracket = "({["
close_bracket = "]})"

def match_bracket(bracket_open:str, bracket_close:str)->bool:
    if bracket_open == '(':
        return bracket_close == ')'
    elif bracket_open == '{':
        return bracket_close == '}'
    elif bracket_open == '[':
        return bracket_close == ']'
    else:
        raise ValueError("Invalid bracket")


def bracket_checker(formula:str) -> bool:
    bracket_stack = Stack()
    
    char_no = 5
    stack_no = 13
    note_no = 25
    
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{note_no}}-+")
    print(f"| {"char":^{char_no}} | {"bracket_stack":^{stack_no}} | {"note":^{note_no}} |")
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{note_no}}-+")
    for char in formula:
        if char == ' ':
            continue
        # 괄호 사용 규칙
        if char in open_bracket:
            bracket_stack.push(char)
            print(f"| {char:^{char_no}} | {str(bracket_stack):^{stack_no}} | {"bracket open":^{note_no}} |")
        elif char in close_bracket:
        # 1. “]“, “}“, “)“이 출현할 경우 stack이 empty이면 에러
            if bracket_stack.is_empty():
                print(f"| {char:^{char_no}} | {str(bracket_stack):^{stack_no}} | {"not have open bracket":^{note_no}} |")
                print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{note_no}}-+")
                return False
        # 2. “]“, “}“, “)“ 중 하나가 출현할 경우 stack에는 각각 “[“, “{“, “(“ 중 하나가 있어야 한다.
            if not match_bracket(bracket_stack.pop(), char):
                print(f"| {char:^{char_no}} | {str(bracket_stack):^{stack_no}} | {"bracket not match":^{note_no}} |")
                print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{note_no}}-+")
                return False
            print(f"| {char:^{char_no}} | {str(bracket_stack):^{stack_no}} | {"bracket close":^{note_no}} |")
        else:
            print(f"| {char:^{char_no}} | {str(bracket_stack):^{stack_no}} | {"continue":^{note_no}} |")
        # 3. 더 이상 “]“, “}“, “)“이 출현하지 않을 경우 stack은 비어있어야 한다.
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{note_no}}-+")
    return bracket_stack.is_empty()
            

# postfix 변환 프로그램
open_bracket = "({["
close_bracket = "]})"
operator = "+-*/"
priority = {"/":3,"*":3,"-":4,"+":4}

def operator_higher(high:str, low:str) -> bool:
    if high in operator and low in operator:
        return priority[high] <= priority[low]
    elif high in open_bracket and low in operator:
        return True
    else:
        raise ValueError("Invalid operator")

def infix_to_postfix(formula:str) -> str:
    operator_stack = Stack()
    postfix = ""
    
    char_no = 5
    stack_no = 25
    postfix_no = 25
    note_no = 25
    
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{postfix_no}}-+-{"":-^{note_no}}-+")
    print(f"| {"char":^{char_no}} | {"operator_stack":^{stack_no}} | {"postfix_output":^{postfix_no}} | {"note":^{note_no}} |")
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{postfix_no}}-+-{"":-^{note_no}}-+")
    
    for char in formula:
        if char == ' ':
            continue
        # Infix to Postfix 변환규칙
        # 1. operand가 나오면 출력한다.
        if char.isdigit():
            note = "operand"
            postfix += char
        # 2. 여는 괄호가 나오면 stack에 push()한다.
        elif char in open_bracket:
            note = "open bracket"
            operator_stack.push(char)
        # 4. 닫는 괄호가 나오면 stack에 pop()하여 출력한다.
        elif char in close_bracket:
            note = "close bracket"
            if operator_stack.peek() in operator:
                postfix += " "
                postfix += operator_stack.pop()
            operator_stack.pop()
        # 오퍼레이터 부분
        elif char in operator:
            postfix += " "
        # 3. 첫번째 operator가 나오면 stack에 push()한다.
            first_operator = True
            for stack_item in operator_stack:
                if stack_item in operator:
                    first_operator = False
                    break
            if first_operator:
                note = "first operator"
                operator_stack.push(char)
        # 5. operator가 나오면 stack에 있는 operator와 비교하여 자신보다 높은 연산자들을
        # pop()하여 출력하고 자신은 stack에 push()한다.
            else:
                if operator_higher(operator_stack.peek(), char) :
                    note = "operator priority high"
                    if operator_stack.peek() in operator:
                        postfix += operator_stack.pop() + " "
                    operator_stack.push(char)
                        
                else:
                    note = "operator priority low"
                    postfix += char + " "
        print(f"| {char:^{char_no}} | {str(operator_stack):^{stack_no}} | {postfix:^{postfix_no}} | {note:^{note_no}} |")
                
        # 6. stack에 남아 있는 operator들을 pop()하여 출력한다. 
    while not operator_stack.is_empty():
        poped = operator_stack.pop()
        if poped in operator:
            postfix += " "
            postfix += poped
            print(f"| {"":^{char_no}} | {str(operator_stack):^{stack_no}} | {postfix:^{postfix_no}} | {"last pop":^{note_no}} |")
    print(f"+-{"":-^{char_no}}-+-{"":-^{stack_no}}-+-{"":-^{postfix_no}}-+-{"":-^{note_no}}-+")
    return postfix  

# postfix 계산 프로그램
def calculate(a, b, operator) -> any:
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        
def postfix_calculation(formula:str) -> any:
    formula = formula.split(' ')
    operand_stack = Stack()
    
    term_no = 5
    stack_no = 20
    variable_no = 10
    note_no = 25
    
    print(f"+-{"":-^{term_no}}-+-{"":-^{stack_no}}-+-{"":-^{variable_no}}-+-{"":-^{note_no}}-+")
    print(f"| {"term":^{term_no}} | {"operand_stack":^{stack_no}} | {"variable":^{variable_no}} | {"note":^{note_no}} |")
    print(f"+-{"":-^{term_no}}-+-{"":-^{stack_no}}-+-{"":-^{variable_no}}-+-{"":-^{note_no}}-+")
    
    for term in formula:
    # Postfix 계산규칙 :
    # 1. operand가 나오면 stack에 push()
        if term.isdigit():
            operand_stack.push(int(term))
            print(f"| {term:^{term_no}} | {str(operand_stack):^{stack_no}} | {"":^{variable_no}} | {"operand push":^{note_no}} |")
    # 2. operator가 나오면
        elif term in operator:
            print(f"| {term:^{term_no}} | {str(operand_stack):^{stack_no}} | {term:^{variable_no}} | {"find operator":^{note_no}} |")
    # - operand2 = pop() # 순서 중요
            operand2 = operand_stack.pop()
            print(f"| {"":^{term_no}} | {str(operand_stack):^{stack_no}} | {operand2:^{variable_no}} | {"operand2 pop":^{note_no}} |")
    # - operand1 = pop()
            operand1 = operand_stack.pop()
            print(f"| {"":^{term_no}} | {str(operand_stack):^{stack_no}} | {operand1:^{variable_no}} | {"operand1 pop":^{note_no}} |")
    # 3. operand1 operator(+-*/) operand2 수행 후 stack에 push()
            calculated = calculate(operand1, operand2, term)
            operand_stack.push(calculated)
            print(f"| {"":^{term_no}} | {str(operand_stack):^{stack_no}} | {calculated:^{variable_no}} | {"calculate and push":^{note_no}} |")
    # 4. 끝까지 반복
        else:
            raise ValueError("Invalid term")
    # 5. stack에 남아 있는 값 출력
    print(f"+-{"":-^{term_no}}-+-{"":-^{stack_no}}-+-{"":-^{variable_no}}-+-{"":-^{note_no}}-+")
    return operand_stack.pop()


def main() -> int:
    # 1. 괄호 사용 검사 프로그램을 완성하여 아래 입력 예제의 결과를 출력하시오.
    # - {a[(i+1)] = 0; }
    # - if ((i == 0) && (k == 0)
    # - while (f < 00)) (f -= f)
    # - A[(B+1] = 0
    print("1. 괄호 사용 검사 프로그램을 완성하여 아래 입력 예제의 결과를 출력하시오.")
    print()
    ex1 = [
        "{a[(i+1)] = 0; }", 
        "if ((i == 0) && (k == 0)", 
        "while (f < 00)) (f -= f)", 
        "A[(B+1] = 0"
    ]
    for one in ex1:
        print("bracket checking: ", one)
        print(one, " is ", bracket_checker(one))
        print()
    print()
    print()

    # 2-1. 아래 식을 postfix로 변환하여 출력하는 프로그램을 완성하시오.
    # • 3 + 4 * 5
    # • (3 + 4) * 5
    # • 3 * (4 * (5 + 6))
    # • 3 / 4 – 5 + ( 6 * 7)
    print("2-1. 아래 식을 postfix로 변환하여 출력하는 프로그램을 완성하시오.")
    print()
    ex2 = [
        "3 + 4 * 5",
        "(3 + 4) * 5",
        "3 * (4 * (5 + 6))",
        "3 / 4 - 5 + ( 6 * 7)"
    ]
    ex2_result = []
    for one in ex2:
        print("postfixing: ", one)
        postfixed = infix_to_postfix(one)
        ex2_result.append(postfixed)
        print(one, " is converted in ", postfixed)
        print()
    print()
    print()
    

    # 2-2. 변환된 postfix를 이용하여 계산하는 프로그램을 완성하시오.
    print("2-2. 변환된 postfix를 이용하여 계산하는 프로그램을 완성하시오.")
    print()
    for one in ex2_result:
        print("calculating: ", one)
        print(one, " = ", postfix_calculation(one))
        print()
    

if __name__ == "__main__":
    sys.exit(main())