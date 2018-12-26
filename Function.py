from TerminalOrFunction import TerminalOrFunction
import Terminal
import copy


class Function(TerminalOrFunction):
    functions = {
        "Plus": lambda a, b: a + b,
        "Minus": lambda a, b: abs(a - b),
        "Multi": lambda a, b: a * b,
        "div": lambda a, b: 0 if b == 0 else a / b,
        "Mod": lambda a, b: 0 if b == 0 else a % b,
        "Maximum": lambda a, b: max(a, b),
        "Minimum": lambda a, b: min(a, b)
    }

    def __init__(self, operationName):
        super().__init__("Function", operationName)

    def clone(self):
        return copy.deepcopy(self)

    def run_(self, row, col, key, board, gradeboard, squaresboard):
        return Function.functions.get(self.getOperationName())(self.getLeft().run(row, col, key, board, gradeboard, squaresboard)
                                                               , self.getRight().run(row, col, key, board, gradeboard, squaresboard))
    @staticmethod
    def peek(stack):
        if len(stack) > 0:
            return stack[-1]
        return None

    def run(self, row, col, key, board, gradeboard, squaresboard):
        stack = []
        root = self
        val1 = 0
        while True:

            while (root):
                # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)

                # Set root as root's left child
                root = root.left

                # Pop an item from stack and set it as root
            root = stack.pop()
            while isinstance(root, int) or isinstance(root, float):
                val2 = root
                root = stack.pop()
                val1 = Function.functions.get(root.getOperationName())(val2, val1)
                if not stack:
                    return val1
                root = stack.pop()

            # if isinstance(root, int) or isinstance(root, float):
            #     val2 = root
            #     root = stack.pop()
            #     val1 = Function.functions.get(root.getOperationName())(val1, val2)
            #     root = stack.pop()
            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if (root.right is not None and
                    Function.peek(stack) == root.right):
                stack.pop()  # Remove right child from stack
                stack.append(root)  # Push root back to stack
                stack.append(val1)  # Push root back to stack
                root = root.right  # change root so that the
                # righ childis processed next

            # Else print root's data and set root as None
            else:
                if root.isTerminal():
                    val1 = root.run(row, col, key, board, gradeboard, squaresboard)
                    root = None

            if len(stack) <= 0:
                break
    @staticmethod
    def methodIsFunction(oparationName):
        return oparationName in Function.functions.keys()

