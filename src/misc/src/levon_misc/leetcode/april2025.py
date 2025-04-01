from typing import List


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
