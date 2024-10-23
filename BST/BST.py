class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if(self.root):
            self.root.insert(data)
        else:
            self.root = Node(data)

    def find(self, data):
        if(self.root):
            return self.root.find(data)
        return False

    def delete(self, data):
        if(self.root):
            self.root = self.root.delete(data)

    def preorder(self):
        if(self.root):
            self.root.preorder(self.root)

    def inorder(self):
        if self.root:
            self.root.inorder(self.root)

    def postorder(self):
        if self.root:
            self.root.postorder(self.root)

    def print_tree(self):
        if self.root:
            print("current elements in the tree\n")
            self.root.print()
        else:
            print("tree is empty")

    def findHeight(self):
        if self.root:
            return self.root.findHeight(self.root)
        return -1

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self,data):
        if(self.data == data):
            raise Exception("Data already exist within tree")
        elif(self.data > data):
            if(self.left):
                self.left.insert(data)
            else:
                 self.left = Node(data)
        else:
            if(self.right):
                self.right.insert(data)
            else:
                self.right = Node(data)

    def find(self, data):
        if self.data == data:
            return True
        elif data < self.data and self.left != None:
            return self.left.find(data)
        elif data > self.data and self.right != None:
            return self.right.find(data)
        return False

    def delete(self,data):
        if(data < self.data and self.left):
            self.left = self.left.delete(data)
        elif(data > self.data and self.right):
            self.right = self.right.delete(data)
        else:
            if(self.data == data):
                if(self.right and self.left):
                    minVal = self.right.findMin()
                    self.data = minVal
                    self.right = self.right.delete(minVal)
                elif(self.left):
                    return self.left
                elif(self.right):
                    return self.right
                else:
                    return None
        return self

    def preorder(self, currentNode):
        if currentNode:
            print(currentNode.data)
            self.preorder(currentNode.left)
            self.preorder(currentNode.right)
    
    def findHeight(self, currentNode):
        if currentNode == None:
            return -1

        leftHeight = self.findHeight(currentNode.left)
        rightHeight = self.findHeight(currentNode.right)

        return max(leftHeight,rightHeight) + 1

    def postorder(self, currentNode):
        if currentNode:
            self.postorder(currentNode.left)
            self.postorder(currentNode.right)
            print(currentNode.data)

    def inorder(self,currentNode):
        if currentNode:
            self.inorder(currentNode.left)
            print(currentNode.data)
            self.inorder(currentNode.right)

    def findMin(self):
        if(self.left):
            return self.left.findMin()
        else:
            return self.data

    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end= ' ')
        if self.right:
            self.right.print()

# Example Usage
bst = BST()

# Inserting values
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

# Deleting values
bst.delete(30)
bst.delete(20)
bst.delete(70)

print(bst.find(60))

bst.preorder()

