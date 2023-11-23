'''
# ex1
def check_parenthses(input_str):
    stack =[]
    open_brackets = "[{("
    close_brackets = "]})"

    for char in input_str:
        if char in open_brackets:
            stack.append(char)
            print(stack)
        elif char in close_brackets:
            if stack:
                top = stack.pop()
                print(stack)

            else:
                return "error"
            if top in open_brackets:
                continue
            else:
                return "erorr"
    if not stack:
        return "ok"
    else:
        return "error"

examples = ['{a[(i+1)] = 0; }', 'if ((i == 0) && (k == 0)',
            'while (f < 00)) (f -= f)', ' A[(B+1] = 0']

for example in examples:
    print(check_parenthses(example))
'''

# ex2
def infix_to_postfix(expression):
    def precedence(operator):
        if operator in ('+', '-'):
            return 1
        elif operator in('*', '/'):
            return 2
        return 0 # 괄호

    def is_operator(char):
        return char in ('+','-', '*', '/')

    def higher_precedence(op1, op2):
        return precedence(op1) >= precedence(op2)

    stack = []
    output = []

    for char in expression:
        if char.isnumeric():
            output.append(char)
            print(output)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
                print(output)
            stack.pop()
        elif is_operator(char):
            while stack and stack[-1] != '(' and higher_precedence(stack[-1], char):
                output.append(stack.pop())
                print(output)
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

infix_expression = "3 + 4 * 5"
postfix_expression = infix_to_postfix(infix_expression.replace(" ",""))
print(f"Infix 표현식: {infix_expression}")
print(f"Postfix 표현식: {postfix_expression}") 


def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isnumeric():
            stack.append(float(char))
        elif char in "+-*/":
            op2 = stack.pop()
            op1 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '/':
                if op2 == 0:
                    raise ValueError("Division by zero")
                stack.append(op1 / op2)
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression")

    return stack[0]


postfix_expression = "345*+"
result = evaluate_postfix(postfix_expression)
print(f"후위 표현식: {postfix_expression}")
print(f"계산 결과: {result}")
















































    

