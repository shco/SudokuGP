from abc import ABC, abstractmethod
import copy
import Node


class TerminalOrFunction(ABC, Node):

    @abstractmethod
    def run(self, row, col, key, board, gradeboard):
        pass

    def __init__(self, nodeType, operationName):
        self.nodeType = nodeType
        self.operationName = operationName

    def getNodeType(self):
        return self.nodeType

    def getOperationName(self):
        return self.operationName

    def clone(self):
        return copy.deepcopy(self)

    def isTerminal(self):
        return self.nodeType == "Terminal"

    def isFunction(self):
        return self.nodeType == "Function"
