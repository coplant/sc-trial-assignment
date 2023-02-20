import collections
import json
import operator
from typing import Optional


class MathExpression:
    OPERATORS = {
        "+": (2, operator.add),
        "-": (2, operator.sub),
        "*": (3, operator.mul),
        "%": (3, operator.floordiv),
        "/": (3, operator.truediv),
        "^": (4, operator.pow),
        "(": (0,),
        ")": (1,)
    }

    def __init__(self, data: str):
        self.raw: str = data
        self.expression: Optional[list] = self.parse(data)

    def __str__(self):
        return str(self.expression)

    @staticmethod
    def parse(data) -> list:
        stack = collections.deque()
        rpn = ''
        for item in data:
            if item in MathExpression.OPERATORS:
                data = data.replace(item, f" {item} ")

        for item in data.split():
            if item.isalnum():
                rpn += item + " "
                continue
            priority = MathExpression.OPERATORS.get(item)[0]
            if priority:
                if all(map(lambda x: MathExpression.OPERATORS.get(x)[0] < priority, stack)):
                    stack.append(item)
                elif stack:
                    while stack and MathExpression.OPERATORS.get(stack[-1])[0] >= priority:
                        rpn += stack.pop() + " "
                    if all(map(lambda x: MathExpression.OPERATORS.get(x)[0] < priority, stack)):
                        stack.append(item)
            if priority == 0:
                stack.append(item)
            if priority == 1:
                operation = stack.pop()
                while MathExpression.OPERATORS.get(operation)[0] != 0:
                    rpn += operation + " "
                    operation = stack.pop()
        while stack:
            rpn += stack.pop() + " "
        return rpn.split()

    def evaluate(self):
        stack = collections.deque()
        for item in self.expression:
            if item in MathExpression.OPERATORS:
                second = stack.pop()
                first = stack.pop()
                result = MathExpression.OPERATORS.get(item)[1](int(first), int(second))
                stack.append(result)
            else:
                stack.append(item)
        if len(stack) != 1:
            raise ValueError
        return stack.pop()
