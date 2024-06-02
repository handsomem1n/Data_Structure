def postfix_to_infix(postfix_expr):
    stack = []

    for token in postfix_expr:
        if token.isalpha() or token.isdigit():  # 피연산자인 경우
            stack.append(token)
        else:  # 연산자인 경우
            operand2 = stack.pop()
            operand1 = stack.pop()
            infix_expr = f"({operand1}{token}{operand2})"
            stack.append(infix_expr)

    return stack[0]

# Test
postfix_expression = "abe+d*-"
infix_expression = postfix_to_infix(postfix_expression)
print(infix_expression)  # Expected: (a*b+c)
