class binaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = binaryTree(newNode)
        else:
            temp = binaryTree(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = binaryTree(newNode)
        else:
            temp = binaryTree(newNode)
            temp.right = self.right
            self.right = temp

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key
