class Node:

    def __init__(self, value = None, left = None, right = None):
        self.left = left
        self.right = right

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
            return leftHeight + 1
        else :
            return rightHeight + 1

    def findHeight(self):
        return self.findTreeHeight()



