def infix_to_postfix(expression):
    def get_precedence(op):
        precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        return precedence[op] if op in precedence else 0

    def is_operator(c):
        return c in ['+', '-', '*', '/', '^']

    output = []
    stack = []

    for char in expression:
        if char.isalpha():  # Operand
            output.append(char)
        elif char == '(':  # Left Parenthesis
            stack.append(char)
        elif char == ')':  # Right Parenthesis
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif is_operator(char):  # Operator
            while stack and get_precedence(stack[-1]) >= get_precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Test
infix_expression = "A+B*C-D/E"
postfix_expression = infix_to_postfix(infix_expression)
print(postfix_expression)  # Expected: ABC*+DE/-
