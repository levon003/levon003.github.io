from levon_misc.streaming import tracker


def test_PopularityTracker():
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
