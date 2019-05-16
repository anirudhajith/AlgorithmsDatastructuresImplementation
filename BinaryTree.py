class BinaryTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

        if not isinstance(left, BinaryTree) or not isinstance(right, BinaryTree):
            raise ValueError('Children must be instances of BinaryTree')
        if key == None:
            raise ValueError('BinaryTree cannot have None key')
        else:
            if left != None:
                left.parent = self
            if right != None:
                right.parent = self

    def createLeaf(self, key, direction):
        return self.insertSubtree(BinaryTree(key), direction)

    def insertSubtree(self, tree, direction):
        if not isinstance(tree, BinaryTree):
            raise ValueError('tree is not an instance of BinaryTree')
        else:
            if direction == 'left':
                self.left = tree
            elif direction == 'right':
                self.right = tree
            else:
                raise ValueError('Invalid direction')

            tree.parent = self
            return tree

    def detachSubtree(self):
        direction = self.getDirection()

        if direction == 'left':
            self.parent.left = None
        elif direction == 'right':
            self.parent.right = None

        self.parent = None
        return self

    def getDirection(self):
        parent = self.parent
        if parent != None:
            if parent.left is self:
                return 'left'
            elif parent.right is self:
                return 'right'
        else:
            return None

    def getSubtreeSize(self):
        size = 1

        if self.left != None:
            size += self.left.getSubtreeSize()
        if self.right != None:
            size += self.right.getSubtreeSize()

        return size

    def getDeepCopy(self):
        copy = BinaryTree(self.key)

        if self.left != None:
            copy.left = self.left.getDeepCopy()
        if self.right != None:
            copy.right = self.right.getDeepCopy()

        return copy
