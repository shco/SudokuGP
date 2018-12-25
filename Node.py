class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.setSize()
        self.height = 0

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

    def findTreeHeight(self):
        rightHeight = 0
        leftHeight = 0
        if self.right is not None:
            rightHeight = self.right.findTreeHeight()
        if self.left is not None:
            leftHeight = self.left.findTreeHeight()
        if leftHeight > rightHeight:
            self.height = leftHeight + 1
            return leftHeight + 1
        else:
            self.height = rightHeight + 1
            return rightHeight + 1

    def findHeight(self):
        return self.findTreeHeight()

    def getSize(self):
        return self.size

    def setSize(self):
        leftSize = 0
        rightSize = 0
        if self.left is not None:
            leftSize = self.left.setSize()
        if self.right is not None:
            rightSize = self.right.setSize()
        self.size = 1 + leftSize + rightSize
        return self.size

    def getParentNode(self, parent, num):
        if num == 1:
            return parent, self
        if self.left is not None and num <= self.left.getSize() + 1:
            return self.left.getParentNode(self, num - 1)
        if self.right is not None:
            return self.right.getParentNode(self, num - (self.size - self.right.size))
        raise ValueError("get number out of bound tree")
