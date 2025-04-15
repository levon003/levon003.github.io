from __future__ import annotations


class EmptyTree(Exception):
    pass


class TreeNode:
    def __init__(self, value: int = 0, parent: TreeNode | None = None):
        self.value = value
        self.counter: int = 1
        self.parent: TreeNode | None = parent
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self._refresh_heights()

    def _refresh_heights(self):
        self.left_height = self.left.height if self.left else 0
        self.right_height = self.right.height if self.right else 0
        self.height = max(self.left_height, self.right_height) + 1

    def _bubble_up_heights(self):
        node = self
        while node is not None:
            node._refresh_heights()
            node = node.parent

    def _to_list_recursive(self, lst: list[int]):
        if self.left is not None:
            self.left._to_list_recursive(lst)
        lst.append(self.value)
        if self.right is not None:
            self.right._to_list_recursive(lst)

    def to_list(self) -> list[int]:
        lst = []
        self._to_list_recursive(lst)
        return lst

    def insert(self, value: int) -> None:
        if value == self.value:
            self.counter += 1
            return
        elif value < self.value:
            if self.left is None:
                self.left = TreeNode(value, parent=self)
                self.left_height += 1
            else:
                self.left.insert(value)
                self.left_height = self.left.height
        elif value > self.value:
            if self.right is None:
                self.right = TreeNode(value, parent=self)
                self.right_height += 1
            else:
                self.right.insert(value)
                self.right_height = self.right.height
        self._refresh_heights()

    def _replace_child(self, child: TreeNode, new_child: TreeNode | None):
        if self.left == child:
            self.left = new_child
        elif self.right == child:
            self.right = new_child
        else:
            raise ValueError(f"{child} not one of {self}'s children.")
        if new_child is not None:
            new_child.parent = self
        self._refresh_heights()

    def _replace(self, new_node: TreeNode):
        self.left = new_node.left
        self.right = new_node.right
        self.value = new_node.value
        self.left_height = new_node.left_height
        self.right_height = new_node.right_height
        self._refresh_heights()

    def _delete(self) -> None:
        has_left = self.left is not None
        has_right = self.right is not None
        if not has_left and not has_right:
            # no children, just delete this node
            if self.parent is not None:
                self.parent._replace_child(self, None)
            else:
                self.counter += 1
                raise EmptyTree()
        elif has_left and not has_right:
            # promote left child
            if self.parent is not None:
                self.parent._replace_child(self, self.left)
            else:
                self._replace(self.left)
        elif not has_left and has_right:
            # promote right child
            if self.parent is not None:
                self.parent._replace_child(self, self.right)
            else:
                self._replace(self.right)
        else:  # has two children
            # promote the "in-order predecessor"
            iop = self.left.get_largest_node()
            self.value = iop.value
            iop.parent._replace_child(iop, None)
            iop.parent._bubble_up_heights()
        self._refresh_heights()

    def delete(self, value: int) -> None:
        if value == self.value:
            self.counter -= 1
            if self.counter <= 0:
                self._delete()
        elif value < self.value:
            if self.left is None:
                raise ValueError(f"{value} not in tree.")
            self.left.delete(value)
        elif value > self.value:
            if self.right is None:
                raise ValueError(f"{value} not in tree.")
            self.right.delete(value)

    def get_largest_node(self) -> TreeNode:
        if self.right is None:
            return self
        return self.right.get_largest_node()

    def __str__(self):
        return f"TreeNode(value={self.value}, height={self.height}[l={self.left_height},r={self.right_height}])"

    def __repr__(self):
        return str(self)


class SelfBalancingBinarySearchTree:
    """
    A binary search tree (BST) "is a binary tree where
    every node in the left subtree is less than the root, and every node
    in the right subtree is of a value greater than the root."

    Per Wikipedia: "a self-balancing binary search tree (BST) is any node-based
    binary search tree that automatically keeps its height (maximal number of
    levels below the root) small in the face of arbitrary item insertions
    and deletions."

    See these lecture notes on Binary Search Trees:
    https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture8.pdf
    """

    def __init__(self, initial_value: int = 0):
        self.root = TreeNode(initial_value)

    def insert(self, value: int) -> None:
        self.root.insert(value)

    def delete(self, value: int) -> None:
        self.root.delete(value)

    def __repr__(self):
        return f"SelfBalancingBinarySearchTree(root={self.root})"
