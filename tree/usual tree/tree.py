from collections import deque

class Tree:
    def __init__(self):
        self.root = None

    def find(self, val, node):
        if val > node.val:
            if node.right:
                return self.find(val, node.right)
            else:
                node.right = TreeNode(val)
        if val < node.val:
            if node.left:
                return self.find(val, node.left)
            else:
                node.left = TreeNode(val)

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.find(val, self.root)

    def printTree(self, node):
        if node:
            print(node.val)
            self.printTree(node.left)
            self.printTree(node.right)

    def find_depth(self, node):
        if not node:
            return 0
        return max(self.find_depth(node.left), self.find_depth(node.right)) + 1

    def find_node_depth(self, val, node, depth=1):
        if val > node.val:
            if node.right:
                return self.find_node_depth(val, node.right, depth + 1)
        if val < node.val:
            if node.left:
                return self.find_node_depth(val, node.left, depth + 1)
        return depth

    def find_max(self, node):
        if node and node.right:
            return self.find_max(node.right)
            if node.right.right is None:
                return node.val
        return node.left.val

    def pre_order(self, node): # сверхну вниз сначала корень, потом левое и тд
        if node:
            print(node.val, end=' ')
            self.in_order(node.left)
            self.in_order(node.right)

    def in_order(self, node): # снизу вверх отсортированное
        if node:
            self.pre_order(node.left)
            print(node.val)
            self.pre_order(node.right)

    def post_order(self, node): # снизу вверх
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val, end=' ')

    def stack_pre(self, node):
        stack = [node]
        while stack:
            v = stack.pop()
            print(v.val, end=' ')
            if v.right:
                stack.append(v.right)
            if v.left:
                stack.append(v.left)

    def stack_post(self, node):
        stack = [node]
        ans = []
        while stack:
            v = stack.pop()
            ans.append(v.val)
            if v.left:
                stack.append(v.left)
            if v.right:
                stack.append(v.right)
        print(*(ans[::-1]))

    def stack_in(self, node):
        stack = []
        v = node
        while stack or v:
            if v:
                stack.append(v)
                v = v.left
            else:
                v = stack.pop()
                print(v.val, end=' ')
                v = v.right

    def v_shirinu(self, node):
        queue = deque()
        queue.append(node)
        while queue:
            v = queue.popleft()
            print(v.val, end=' ')
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)

    def only_leafs(self, node):
        if node:
            self.only_leafs(node.left)
            if not node.left and not node.right:
                print(node.val)
            self.only_leafs(node.right)

    def with_two_leafs(self, node):
        if node:
            self.with_two_leafs(node.left)
            if node.left and node.right:
                print(node.val)
            self.with_two_leafs(node.right)

    def only_one_leaf(self, node):
        if node:
            self.only_one_leaf(node.left)
            if (node.left and not node.right) or (not node.left and node.right):
                print(node.val)
            self.only_one_leaf(node.right)

    def check_avl(self, node):
        queue = deque()
        queue.append(node)
        while queue:
            v = queue.popleft()
            left = self.find_depth(v.left)
            right = self.find_depth(v.right)
            if left == right or left - 1 == right or left + 1 == right:
                pass
            else:
                return "NO"
            if v.left:
                queue.append(v.left)
            if v.right:
                queue.append(v.right)
        return "YES"

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


lister = [int(x) for x in input().split()]

lister.pop()

t = Tree()
for x in lister:
    t.add(x)

print(t.check_avl(t.root))