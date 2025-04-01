from levon_misc.leetcode import april2025

import pytest


@pytest.mark.parametrize("rotate_func", [april2025.rotate1, april2025.rotate2])
def test_rotate(rotate_func):
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    rotate_func(nums, k)
    assert nums == [7, 1, 2, 3, 4, 5, 6]
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_func(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
