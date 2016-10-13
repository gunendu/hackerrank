class Tree:
    def __init__(self):
        self.root = None

    class TreeNode:
        def __init__(self,value):
            self.left = None
            self.right = None
            self.value = value

    def addNode(self,node,value):
        if node == None:
            self.root = self.TreeNode(value)
        else:
            if value < node.value:
                if node.left == None:
                    node.left = self.TreeNode(value)
                else:
                    self.addNode(node.left,value)
            else:
                if node.right == None:
                    node.right = self.TreeNode(value)
                else:
                    self.addNode(node.right,value)

    def printTree(self,root):
        if root!=None:
            self.printTree(root.left)
            print root.value
            self.printTree(root.right)

    def heightOfTree(self,root):
        if(root==None):
            return 0

        leftH = self.heightOfTree(root.left)
        rightH = self.heightOfTree(root.right)

        if(leftH>rightH):
            return leftH + 1
        else:
            return rightH + 1

def main():
    tree = Tree()
    tree.addNode(tree.root,3)
    tree.addNode(tree.root,2)
    tree.addNode(tree.root,1)
    tree.addNode(tree.root,5)
    tree.addNode(tree.root,4)
    tree.addNode(tree.root,6)
    tree.addNode(tree.root,7)

    tree.printTree(tree.root)
    print tree.heightOfTree(tree.root)

main()
