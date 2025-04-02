import bisect

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


@pytest.mark.parametrize(
    ("bisect_left", "bisect_right"),
    [
        (bisect.bisect_left, bisect.bisect_right),
    ],
)
def test_bisect(bisect_left, bisect_right):
    a = [1, 2, 3, 3, 3, 4, 5]
    assert bisect_left(a, 3) == 2
    assert bisect_right(a, 3) == 5
    assert bisect_left(a, 0) == 0
    assert bisect_right(a, 0) == 0
    assert bisect_left(a, 6) == 7
    assert bisect_right(a, 6) == 7
    assert bisect_left(a, 3.5) == 5
    assert bisect_right(a, 3.5) == 5
