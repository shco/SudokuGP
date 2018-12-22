class Node:

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getValue(self):
        return self.value

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def setValue(self, value):
        self.value = value

    def createLeft(self, leftValue):
        self.left = Node(leftValue)
        return self.left

    def createRight(self, rightValue):
        self.right = Node(rightValue)
        return self.right

    def findTreeHeight(self):
        rightHeight = 0
        leftHeight = 0
        if  self.right is not None:
            rightHeight = self.right.findTreeHeight()
        if  self.left is not None:
            leftHeight = self.left.findTreeHeight()
        if leftHeight > rightHeight:
            return leftHeight + 1
        else :
            return rightHeight + 1

    def findHeight(self):
        return self.findTreeHeight()


