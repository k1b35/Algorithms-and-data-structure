def calculate_expression(expression):
    stack = []
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: x - y,
                 '*': lambda x, y: x * y,
                 '/': lambda x, y: x // y,
                 '!': lambda x: factorial(x),
                 '#': lambda x: [x, x],
                 '@': lambda x, y, z: [y, z, x]}

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        elif token in operators:
            if token == '!':
                operand = stack.pop()
                result = operators[token](operand)
            elif token == '#':
                operand = stack[-1]
                result = operators[token](operand)
            elif token == '@':
                operand3 = stack.pop()
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](operand1, operand2, operand3)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operators[token](operand1, operand2)
            if isinstance(result, list):
                stack.extend(result)
            else:
                stack.append(result)

    return stack.pop()


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



expression = input()


result = calculate_expression(expression)
print(result)
