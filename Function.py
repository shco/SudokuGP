from TerminalOrFunction import TerminalOrFunction
import copy


class Function(TerminalOrFunction):
    functions = {
        "Plus": lambda a, b: a + b,
        "Minus": lambda a, b: abs(a - b),
        "Multi": lambda a, b: a * b,
        # "div": lambda a, b: 0 i sf b == 0 else a / b,
        # "Mod": lambda a, b: 0 if b == 0 else a % b,
        # "Maximum": lambda a, b: max(a, b),
        # "Minimum": lambda a, b: min(a, b)
    }

    def __init__(self, operationName):
        super().__init__("Function", operationName)

    def clone(self):
        return copy.deepcopy(self)

    def run(self, row, col, key, board, gradeboard, squaresboard):
        return Function.functions.get(self.getOperationName())(self.getLeft().run(row, col, key, board, gradeboard, squaresboard)
                                                               , self.getRight().run(row, col, key, board, gradeboard, squaresboard))

