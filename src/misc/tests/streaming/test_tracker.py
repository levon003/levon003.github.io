from levon_misc.streaming import tracker


def test_PositiveCountTracker():
    count_tracker = tracker.PositiveCountTracker()
    assert count_tracker.get_largest() == -1
    count_tracker.increase(7)
    count_tracker.increase(7)
    count_tracker.increase(8)
    assert count_tracker.get_largest() == 7
    count_tracker.increase(8)
    count_tracker.increase(8)
    assert count_tracker.get_largest() == 8
    count_tracker.decrease(8)
    count_tracker.decrease(8)
    assert count_tracker.get_largest() == 7
    count_tracker.decrease(7)
    count_tracker.decrease(7)
    count_tracker.decrease(8)
    assert count_tracker.get_largest() == -1


def test_AllPositiveCountTracker():
    count_tracker = tracker.AllPositiveCountTracker()
    assert count_tracker.get_largest_k(3) == []
    for content_id in [1, 2, 3, 4]:
        for i in range(5 + content_id):
            count_tracker.increase(content_id)
    assert count_tracker.get_largest_k(3) == [4, 3, 2]
