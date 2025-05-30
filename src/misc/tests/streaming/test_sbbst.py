import random

import pytest

from levon_misc.streaming import sbbst


def test_insert():
    tree = sbbst.SelfBalancingBinarySearchTree(0)
    assert tree.root.height == 1
    expected_list = [0]
    assert tree.root.to_list() == expected_list
    for i in range(1, 5):
        tree.insert(i)
        assert tree.root.height == 1 + i
        expected_list.append(i)
        assert tree.root.to_list() == expected_list


def test_delete():
    tree = sbbst.SelfBalancingBinarySearchTree(1)
    with pytest.raises(sbbst.EmptyTree):
        tree.delete(1)
    with pytest.raises(ValueError):
        tree.delete(0)

    # test promotion
    tree.insert(0)
    tree.delete(0)
    assert tree.root.left is None
    tree.insert(2)
    assert tree.root.right is not None
    tree.delete(2)
    assert tree.root.right is None
    assert tree.root.value == 1

    # test root promotion
    tree.insert(0)
    tree.delete(1)
    assert tree.root.value == 0

    # multiple children
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.delete(2)
    assert tree.root.value == 0
    assert tree.root.left is None
    assert tree.root.right.value == 1
    assert tree.root.right.right.value == 3

    # test more complex removals
    """
        6
      4   7
     2 5
    """
    tree = sbbst.SelfBalancingBinarySearchTree(6)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    assert tree.root.to_list() == [3, 4, 5, 6, 7]
    tree.delete(6)
    assert tree.root.to_list() == [3, 4, 5, 7]
    """
           6
        3     7
       2 4
          5
    """
    tree = sbbst.SelfBalancingBinarySearchTree(6)
    tree.insert(3)
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(7)
    assert tree.root.to_list() == [2, 3, 4, 5, 6, 7]
    tree.delete(6)
    assert tree.root.to_list() == [2, 3, 4, 5, 7]
    """
           6
        2     7
       1 4
        3 5
    """
    tree = sbbst.SelfBalancingBinarySearchTree(6)
    tree.insert(2)
    tree.insert(1)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(7)
    assert tree.root.to_list() == [1, 2, 3, 4, 5, 6, 7]
    tree.delete(6)
    assert tree.root.to_list() == [1, 2, 3, 4, 5, 7]

    tree = sbbst.SelfBalancingBinarySearchTree(5)
    for value in [2, 4, 1, 0, 3]:
        tree.insert(value)
    assert tree.root.to_list() == [0, 1, 2, 3, 4, 5]
    tree.delete(5)
    assert tree.root.to_list() == [0, 1, 2, 3, 4]
    tree.delete(2)
    assert tree.root.to_list() == [0, 1, 3, 4]
    tree.delete(4)
    assert tree.root.to_list() == [0, 1, 3]
    tree.delete(1)
    assert tree.root.to_list() == [0, 3]
    tree.delete(0)
    assert tree.root.to_list() == [3]


def test_behavior():
    n = 5
    expected_output = list(range(n + 1))
    for i in range(100):
        # try to insert a bunch of items, verifying that to_list() always returns the sorted order
        shuffled_input = random.sample(expected_output, len(expected_output))
        tree = sbbst.SelfBalancingBinarySearchTree(shuffled_input[0])
        for value in shuffled_input[1:]:
            tree.insert(value)
        assert tree.root.to_list() == expected_output
        assert tree.root.check_uniqueness()

        expected_reduction = expected_output[:]
        for value in shuffled_input[: n // 2]:
            tree.delete(value)
            expected_reduction.remove(value)
            assert (
                tree.root.check_uniqueness()
            ), f"Dupes present: {tree.root.to_list()}, expected {expected_reduction} (from {shuffled_input})"
            assert tree.root.to_list() == expected_reduction
