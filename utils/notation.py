import collections
import json
import operator
from typing import Optional


class MathExpression:
    OPERATORS = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "//": operator.floordiv,
        "/": operator.truediv,
        "^": operator.pow,
        "**": operator.pow,
    }

    def __init__(self, data: str):
        self.raw: str = data
        self.expression: Optional[list] = self.loads(data)
        # raise NotImplemented

    def json(self):
        raise NotImplemented

    # TODO: ошибки при парсинге - мало чисел, много чисел
    def loads(self, data) -> list:
        raw_data = data.split()
        return raw_data

    def dumps(self):
        raise NotImplemented

    def evaluate(self):
        stack = collections.deque()
        for item in self.expression:
            if item in MathExpression.OPERATORS:
                second = stack.pop()
                first = stack.pop()
                result = MathExpression.OPERATORS.get(item)(int(first), int(second))
                stack.append(result)
            else:
                stack.append(item)
        if len(stack) != 1:
            raise ValueError
        return stack.pop()
