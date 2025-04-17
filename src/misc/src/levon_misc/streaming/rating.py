class RatingScale:
    def __init__(self, min_value: int = 0, max_value: int = 10, step_size: float = 1):
        self.min_value = min_value
        self.max_value = max_value
        self.step_size = step_size

    def get_valid_ratings(self) -> list[float]:
        value = self.min_value
        valid_ratings = []
        while value <= self.max_value:
            valid_ratings.append(value)
            value += self.step_size
        return valid_ratings

    def is_valid_rating(self, new_rating):
        # TODO we should check that this lies on one of the steps
        return new_rating >= self.min_value and new_rating <= self.max_value

    def __repr__(self):
        return f"RatingScale(min_value={self.min_value}, max_value={self.max_value}, step_size={self.step_size})"


class NamedRateableEntity:
    def __init__(self, name: str):
        self.name = name
        self.n_ratings = 0
        self.total_rating = 0

    def get_average_rating(self):
        # TODO we should define more reasonable before for the no-ratings case
        if self.n_ratings == 0:
            raise ValueError("No ratings yet!")
        return self.total_rating / self.n_ratings

    def add_rating(self, new_rating) -> None:
        self.n_ratings += 1
        self.total_rating += new_rating


class ReportGenerator:
    @classmethod
    def get_entity_report(
        self, entities: list[NamedRateableEntity]
    ) -> list[tuple[str, float]]:
        return [(entity.name, entity.get_average_rating()) for entity in entities]


class RatingTracker:
    def __init__(self, rating_scale: RatingScale):
        self.rating_scale = rating_scale
        self.entities: dict[str, NamedRateableEntity] = {}

    def get_sorted_ratings(self) -> list[tuple[str, float]]:
        """This method can be improved. In particular, we have to sort the entities we are tracking every time.

        A few options:
        1.  Maintain a cached sorted list in self.sorted_entities.
            If few entities change their ratings, then the sort should empirically be faster, though still O(n log n).
        2.  Keep track of "dirty" entities and sort them separately
            (either by creating a dirty_set or adding a boolean flag to NamedRateableEntity).
         a. Extract m dirty_entities and clean_entities from self.sorted_entities. - O(n)
            (or, build clean_entities on the fly and build dirty_entities iteratively as add_rating is called.)
            Sort dirty_entities. (clean_entities is already sorted.) - O(m log m)
            Sort dirty_entities + clean_entities - O(n log n), but potentially much faster. Why?
            Because the Timsort implementation that Python uses should be effective at recognizing sorted regions,
            this should approach O(n) for sorting as m decreases.
            Total time complexity: O(m log m + n) for small m.
         b. Extract m dirty_entities and clean_entities from self.sorted_entities - O(n)
            Sort dirty_entities. (clean_entities is already sorted.) - O(m log m)
            Do a linear-time merge of dirty_entities and clean_entities - O(n)
            Total time complexity: O(m log m + n)
            This degrades to the naive approach when m == n,
            but as m decreases relative to n the total cost approaches O(n).

        Returns:
            list[tuple[str, float]]: Entity names and average ratings.
        """
        sorted_entities = sorted(
            self.entities.values(),
            key=lambda entity: entity.get_average_rating(),
            reverse=True,
        )
        return ReportGenerator.get_entity_report(sorted_entities)

    def add_entity(self, new_entity: NamedRateableEntity) -> None:
        if new_entity.name in self.entities:
            raise ValueError("Already an entity with that name!")
        self.entities[new_entity.name] = new_entity

    def remove_entity(self, entity: NamedRateableEntity) -> None:
        if entity.name not in self.entities:
            raise ValueError("Entity does not exist in our tracker!")
        del self.entities[entity.name]

    def remove_entity_by_name(self, entity_name: str) -> None:
        if entity_name not in self.entities:
            raise ValueError(f"Entity with name {entity_name} does not exist.")
        self.remove_entity(self.entities[entity_name])

    def add_rating(self, entity_name: str, new_rating: float) -> None:
        if entity_name not in self.entities:
            raise ValueError(f"Entity {entity_name} not in tracker.")
        if self.rating_scale.is_valid_rating(new_rating):
            self.entities[entity_name].add_rating(new_rating)
        else:
            raise ValueError(
                f"Rating {new_rating} is not valid according to scale {self.rating_scale}."
            )
