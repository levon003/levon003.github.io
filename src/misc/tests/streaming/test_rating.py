import numpy as np

from levon_misc.streaming.rating import RatingScale, RatingTracker, NamedRateableEntity


class TestRatingScale:
    def test_get_valid_ratings(self):
        scale = RatingScale(0, 5, 1)
        assert scale.get_valid_ratings() == [
            0,
            1,
            2,
            3,
            4,
            5,
        ], scale.get_valid_ratings()
        scale = RatingScale(0, 1, 0.2)
        assert np.isclose(
            scale.get_valid_ratings(),
            [
                0,
                0.2,
                0.4,
                0.6,
                0.8,
                1.0,
            ],
        ).all()


class TestCustomerSupportAgent:
    def test_add_rating(self):
        agent = NamedRateableEntity("Zach")
        agent.add_rating(1)
        assert agent.total_rating == 1

    def test_get_average_rating(self):
        agent = NamedRateableEntity("Zach")
        agent.add_rating(1)

        try:
            agent = NamedRateableEntity("Zach")
            agent.get_average_rating()
            assert False, "Expected exception."
        except ValueError:
            assert True


class TestRatingTracker:
    def test_get_agent_ratings(self):
        scale = RatingScale(-2, 2, 1)
        tracker = RatingTracker(scale)
        tracker.add_entity(NamedRateableEntity("Heeba"))
        tracker.add_rating("Heeba", 0)
        tracker.add_rating("Heeba", 2)
        tracker.add_rating("Heeba", 1)
        tracker.add_entity(NamedRateableEntity("Zach"))
        tracker.add_rating("Zach", -2)
        tracker.add_rating("Zach", -2)
        assert tracker.get_sorted_ratings() == [("Heeba", 1), ("Zach", -2)]

        try:
            tracker.add_rating("Nonexistent", 0)
            assert False
        except ValueError:
            pass

        try:
            tracker.add_rating("Zach", 3)
            assert False
        except ValueError:
            pass

        try:
            tracker.remove_entity_by_name("Nonexistent")
            assert False
        except ValueError:
            pass
        tracker.remove_entity_by_name("Heeba")
        assert tracker.get_sorted_ratings() == [("Zach", -2)]
