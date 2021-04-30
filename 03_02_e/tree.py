class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def toStr(self):
        if not self.isBalanced():
            return str(self.data)+'*'
        return str(self.data)

    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")


    def getNodesAtDepth(self, depth, nodes):
        if depth == 0:
            nodes.append(self)
            return nodes
        
        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def add(self, data):
        if data == self.data:
            # Binary search tree does not contain duplicates
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            else:
                self.left.add(data)                
        
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.add(data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self

    def delete(self, target):
        if self.data == target:
            if self.right and self.left:
                minimumValue = self.right.findMin()
                self.data = minimumValue.data
                self.right = self.right.delete(minimumValue.data)
                return self
            else: 
                return self.right or self.left
        
        if self.right and target > self.data:
                self.right = self.right.delete(target)

        if self.left and target < self.data:
                self.left = self.left.delete(target)
        return self

    def isBalanced(self):
        leftHeight = self.left.height()+1 if self.left else 0
        rightHeight = self.right.height()+1 if self.right else 0
        return abs(leftHeight - rightHeight) < 2

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(n.toStr())+1
        return n.toStr()+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePreorder(self):
        self.root.traversePreorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def search(self, target):
        return self.root.search(target)

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def height(self):
        return self.root.height()

    def add(self):
        self.root.add()

    def delete(self, target):
        self.root = self.root.delete(target)


def rotateRight(root):
    pivot = root.left 
    reattachNode = pivot.right
    root.left = reattachNode
    pivot.right = root
    return pivot

def rotateLeft(root):
    pivot = root.right 
    reattachNode = pivot.left
    root.right = reattachNode
    pivot.left = root
    return pivot

unbalancedLeftLeft = Tree(Node(30), 'UNBALANCED LEFT LEFT')
unbalancedLeftLeft.root.left = Node(20)
unbalancedLeftLeft.root.left.right = Node(21)
unbalancedLeftLeft.root.left.left = Node(10)
unbalancedLeftLeft.root.left.left.left = Node(9)
unbalancedLeftLeft.root.left.left.right = Node(11)
unbalancedLeftLeft.print()
unbalancedLeftLeft.root = rotateRight(unbalancedLeftLeft.root)

unbalancedRightRight = Tree(Node(10), 'UNBALANCED RIGHT RIGHT')
unbalancedRightRight.root.right = Node(20)
unbalancedRightRight.root.right.left = Node(19)
unbalancedRightRight.root.right.right = Node(30)
unbalancedRightRight.root.right.right.left = Node(29)
unbalancedRightRight.root.right.right.right = Node(31)
unbalancedRightRight.print()
unbalancedRightRight.root = rotateLeft(unbalancedRightRight.root)
unbalancedRightRight.print()

unbalancedLeftRight = Tree(Node(30), 'UNBALANCED LEFT RIGHT')
unbalancedLeftRight.root.right = Node(31)
unbalancedLeftRight.root.left = Node(10)
unbalancedLeftRight.root.left.right = Node(20)
unbalancedLeftRight.root.left.left = Node(9)
unbalancedLeftRight.root.left.right.left = Node(19)
unbalancedLeftRight.root.left.right.right = Node(21)
unbalancedLeftRight.print()

unbalancedLeftRight.root.left = rotateLeft(unbalancedLeftRight.root.left)
unbalancedLeftRight.root = rotateRight(unbalancedLeftRight.root)
unbalancedLeftRight.print()

unbalancedRightLeft = Tree(Node(30), 'UNBALANCED RIGHT LEFT')
unbalancedRightLeft.root.left = Node(31)
unbalancedRightLeft.root.right = Node(10)
unbalancedRightLeft.root.right.left = Node(20)
unbalancedRightLeft.root.right.right = Node(9)
unbalancedRightLeft.root.right.left.right = Node(19)
unbalancedRightLeft.root.right.left.left = Node(21)
unbalancedRightLeft.print()

unbalancedRightLeft.root.right = rotateRight(unbalancedRightLeft.root.right)
unbalancedRightLeft.root = rotateLeft(unbalancedRightLeft.root)
unbalancedRightLeft.print()
