class BTNode:
    def __init__(self, val):
        self.leftNode = None
        self.rightNode = None
        self.val = val

    def insertNode(self, val):
        if self.val:
            if val < self.val:
                if self.leftNode is None:
                    self.leftNode = BTNode(val)
                else:
                    self.leftNode.insertNode(val)
            elif val > self.val:
                if self.rightNode is None:
                    self.rightNode = BTNode(val)
                else:
                    self.rightNode.insertNode(val)
        else:
            self.val = val
    def displayTree(self):
        if self.leftNode:
            self.leftNode.displayTree()
        print( self.val)
        if self.rightNode:
            self.rightNode.displayTree()

    def searchVal(self, data):
        if data < self.val:
            if self.leftNode is None:
                return str(data)+" is not Found in the Binary Tree"
            return self.leftNode.searchVal(data)
        elif data > self.val:
            if self.rightNode is None:
                return str(data)+" is not Found in the Binary Tree"
            return self.rightNode.searchVal(data)
        else:
            return str(self.val) + " is found in the Binary Tree"
root = BTNode(70)
root.insertNode(80)
root.insertNode(50)
root.insertNode(100)
root.insertNode(30)
root.insertNode(20)
root.displayTree()
