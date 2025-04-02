from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def rotate1(nums: List[int], k: int) -> List[int]:
    """
    https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
    """
    n = len(nums)
    k = k % n
    if k == 0:
        return
    nums[:] = nums[n - k :] + nums[: n - k]
    assert len(nums) == n


def rotate2(nums: List[int], k: int) -> None:
    """
    k = 1
    [0123] -> [1230]
    k = 2
    [0123] -> [2301]
    When k is 1, we observe that we can shift one after another... we only need to remember a single element, the first.

    n=6,k=2
    The destination index is not the value we need!
    [012345] -> [234501]
    index 0 -> n-k = 4
    index 4 -> n-k = 2
    so updating just the first index seems to imply updating indices 2 and 4 as well!
    That can be accomplished in a cycle, potentially; each time, we know what index we need to replace
    and where _that_ replacement value should go.
    """
    n = len(nums)
    k = k % n
    if k == 0:
        return
    curr_index = 0
    curr_value = nums[0]
    n_replaced = 0
    # TODO this is the right idea, but it rotates to the left...
    while n_replaced < n:
        target_index = curr_index - k
        next_value = nums[target_index]
        nums[target_index] = curr_value
        curr_value = next_value
        curr_index = target_index
        n_replaced += 1


class MaxDepthOfBinaryTree:
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.maxDepthRecursive(root, 0)

    def maxDepthRecursive(self, node: Optional[TreeNode], depth: int) -> int:
        if node is None:
            return depth
        left_depth = self.maxDepthRecursive(node.left, depth + 1)
        right_depth = self.maxDepthRecursive(node.right, depth + 1)
        depth = max((left_depth, right_depth))
        return depth

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        """maxDepth1 works fine, but the need to track the depth in a separate variable is unfortunate.
        Do we really need to track it in a function parameter?
        No, because intuitively we don't need to know our current depth, which implies we can put the "+1" in the return statement.
        """
        if root is None:
            return 0
        return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1

    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        """maxDepth2 uses recursion, which will start running us into max stack size issues.
        What about an iterative implementation of Breadth First Search?"""
        if root is None:
            return 0
        queue: deque[tuple[TreeNode | None, int]] = deque([(root, 1)])
        max_depth = 0
        while len(queue) > 0:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                queue.append((node.left, depth + 1))
            if node.right is not None:
                queue.append((node.right, depth + 1))
        return max_depth

    def maxDepth4(self, root: Optional[TreeNode]) -> int:
        """maxDepth2 uses recursion, which will start running us into max stack size issues.
        What about an iterative implementation of Depth First Search?
        Note we can just use a list, as pop()"""
        if root is None:
            return 0
        stack: list[tuple[TreeNode | None, int]] = [(root, 1)]
        max_depth = 0
        while len(stack) > 0:
            node, depth = stack.pop()
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))
        return max_depth
