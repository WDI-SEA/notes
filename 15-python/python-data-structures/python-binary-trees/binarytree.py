class TreeNode:
    left = None
    right = None

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

class BinaryTree:
    root = None

    IN_ORDER_TEMPLATE   = "{left} {curr} {right}"
    PRE_ORDER_TEMPLATE  = "{curr} {left} {right}"
    POST_ORDER_TEMPLATE = "{left} {right} {curr}"

    # default to printing the tree using an "in order" traversal.
    def __str__(self):
        return self.print_in_order()

    # print the left node, then the current node, then the right node.
    # this results in all the data in the tree being printed in sorted order.
    def print_in_order(self):
        # return "[" + self.print_in_order_helper(self.root) + "]"
        return "[" + self.print_helper(self.root, self.IN_ORDER_TEMPLATE) + "]"

    # one generic print_helper that accepts a template that defines how results
    # are accumulated.
    def print_helper(self, node, template):
        if node is None:
            return ""
        left = self.print_in_order_helper(node.left)
        curr = str(node.data)
        right = self.print_in_order_helper(node.right)
        return template.format(left=left, curr=curr, right=right)

    # a helper function to print the tree in order manually without a template.
    def print_in_order_helper(self, node):
        if node is None:
            return ""
        left = self.print_in_order_helper(node.left)
        curr = str(node.data)
        right = self.print_in_order_helper(node.right)
        return left + " " + curr + " " + right

    # print each node before it's sub tree
    def print_pre_order(self):
        return "[" + self.print_pre_order_helper(self.root) + "]"

    def print_pre_order_helper(self, node):
        if node is None:
            return ""
        curr = str(node.data)
        left = self.print_in_order_helper(node.left)
        right = self.print_in_order_helper(node.right)
        return curr + " " + left + " " + right

    # print each node after it's sub tree
    def print_post_order(self):
        return "[" + self.print_post_order_helper(self.root) + "]"

    def print_post_order_helper(self, node):
        if node is None:
            return ""
        left = self.print_in_order_helper(node.left)
        right = self.print_in_order_helper(node.right)
        curr = str(node.data)
        return left + " " + right + " " + curr

    def add(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.add_helper(self.root, data)        

    def add_helper(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.add_helper(node.left, data)
        elif data >= node.data:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.add_helper(node.right, data)

    def contains(self, value):
        return self.contains_helper(self.root, value)

    def contains_helper(self, node, value):
        if node is None:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self.contains_helper(node.left, value)
        if value > node.data:
            return self.contains_helper(node.right, value)


tree = BinaryTree()
tree.add(12)
tree.add(42)
tree.add(32)
tree.add(54)
tree.add(2)
tree.add(6)

print(tree)
print("  in order traversal:", tree.print_in_order())
print(" pre order traversal:", tree.print_pre_order())
print("post order traversal:", tree.print_post_order())
print()

print(tree.contains(12), "should be True")
print(tree.contains(54), "should be True")
print(tree.contains(0), "should be False")
print(tree.contains(13), "should be False")
print(tree.contains(99), "should be False")
