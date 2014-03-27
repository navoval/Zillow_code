__author__ = 'changyunglin'

# Question 2: Implement insert and delete in a tri-nary tree.
# finished build up Tri-Tree
# finished print our Tri-Tree
# haven't finish delete node, will update soon


class Node:

    def __init__(self, data):
        self.root = None
        self.left = None
        self.right = None
        self.center = None
        self.data = data
        self.level = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while 1:
                # left child
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                # center child
                elif data == current.data:
                    if current.center is None:
                        current.center = Node(data)
                        break
                    else:
                        current = current.center
                # right child
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right
                else:
                    break

    def lookUp(self, value, parent=None):
        '''
        look up contain data
        return node and node's parent if found or None
        '''
        if value < self.left.data:
            if self.root.left is None:
                return None, None
            else:
                return self.root.left.lookUp(value, self)
        elif value == self.center.data:
            if self.root.center is None:
                return None, None
            else:
                return self.center.lookUp(value, self)
        elif value > self.right.data:
            if self.root.right is None:
                return None, None
            else:
                return self.root.right.lookUp(value, self)
        else:
            return self, parent

    def childrenCount(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        if self.center:
            count += 1
        return count

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.center)
            self.inorder(node.right)

    def printTree(self):
        self.root.level = 0
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.level > current_level:
                current_level += 1
                out.append("\n")
            out.append(str(current_node.data) + " ")

            if current_node.left:
                current_node.left.level = current_level + 1
                queue.append(current_node.left)
            else:
                out.append(" left-Null ")

            if current_node.center:
                current_node.center.level = current_level + 1
                queue.append(current_node.center)
            else:
                out.append(" center-Null ")

            if current_node.right:
                current_node.right.level = current_level + 1
                queue.append(current_node.right)
            else:
                out.append(" right-Null ")

        print(''.join(out))


# Test Cases
l1 = [5, 4, 9, 5, 7, 2, 2]
tree1 = Node(0)
[tree1.insert(e) for e in l1]
print "Test case 1: ",l1 
print "Tree 1" 
print tree1.printTree()

# Another test case
l2 = [5, 4, 9, 5, 7, 2, 2, 9, 10]
tree2 = Node(0)
[tree2.insert(e) for e in l2]
print "Test case 2: ", l2
print "Tree 2"
print tree2.printTree()


# Output explain. I also listed out the Null part for each node.
# For example, "4 center-Null  right-Null" means that 'center and right' under node 4 are Null
# Original Tree
# 5  
# 4  center-Null  right-Null 5  left-Null  center-Null  right-Null 9  center-Null  right-Null 
# 2  left-Null  right-Null 7  left-Null  center-Null  right-Null 
# 2  left-Null  center-Null  right-Null 
# None
# 


