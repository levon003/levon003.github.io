class PositiveCountTracker:
    """
    Keeps track of the highest value item given a stream
    of increases and decreases associated with particular content IDs
    (e.g. likes and dislikes on videos).

    To implement this spec, we need a data structure that can:
    -Insert and pop rapidly - O(1)
    -Get most popular item - O(1)

    We accomplish this with two Hash Maps:
    - The first maps content IDs to the current count of that content ID.
    - The second maps counts to the set of content IDs currently at that count.
    Finally, we keep track of the highest count of any tracked content ID.

    In Java, we might consider use a TreeMap, which implements the SortedMap interface.
    However, that leaves insertions, deletions, and search at O(log n).
    """

    def __init__(self):
        self.counts: dict[int, int] = {}  # content_id -> count
        self.content_ids: dict[int, set[int]] = (
            {}
        )  # count -> {content_id1, content_id2, etc.}
        self.max_count = 0

    def get_largest(self) -> int:
        """Get the largest bit.

        Returns:
            int: Returns the content ID with the highest count, or -1 if no content with a non-zero count.
        """
        if len(self.counts) == 0:
            # no content ID with a positive value
            return -1
        assert self.max_count > 0
        return next(iter(self.content_ids[self.max_count]))

    def _set_new_count(self, content_id: int, prev_count: int, new_count: int):
        if new_count > 0:
            if new_count not in self.content_ids:
                self.content_ids[new_count] = set()
            self.content_ids[new_count].add(content_id)
            self.counts[content_id] = new_count
        else:
            # count at zero, so stop counting this content_id
            del self.counts[content_id]
        if prev_count > 0:
            self.content_ids[prev_count].remove(content_id)
            if len(self.content_ids[prev_count]) == 0:
                del self.content_ids[prev_count]

    def increase(self, content_id: int) -> None:
        if content_id < 0:
            raise ValueError(f"Content ID {content_id} not positive.")
        if content_id not in self.counts:
            self.counts[content_id] = 0
        prev_count = self.counts[content_id]
        new_count = prev_count + 1
        self._set_new_count(content_id, prev_count, new_count)
        if new_count > self.max_count:
            self.max_count = new_count

    def decrease(self, content_id: int):
        if content_id < 0:
            raise ValueError(f"Content ID {content_id} not positive.")
        if content_id not in self.counts:
            # we never track negative counts
            return
        prev_count = self.counts[content_id]
        new_count = prev_count - 1
        self._set_new_count(content_id, prev_count, new_count)
        if prev_count == self.max_count:
            # this content ID was the previous max
            if self.max_count not in self.content_ids:
                # there's no other content ID at this value
                self.max_count = new_count


class AllPositiveCountTracker(PositiveCountTracker):
    """
    What if we wanted to add a get_largest_k(k: int) method?

    Probably, the most efficient thing to do is use a Red-Black tree implementation.
    That would give us:
    - insert/delete: O(log n)
    - largest k: O(k + log n)

    We could use the same data structure as in PositiveCountTracker,
    and just commit to sorting the counts and retrieving the k largest.
    That would give us:
    - insert/delete: O(1)
    - largest k: O(n log n)
    Note the largest k is actually slightly better than O(n log n), as we only need to sort the *counts*,
    not all of the unique content IDs, and # counts <= # content IDs.
    """

    def get_largest_k(self, k: int) -> list[int]:
        sorted_counts = sorted(self.content_ids.keys(), reverse=True)
        result = []
        for count in sorted_counts:
            result.extend(self.content_ids[count])
            if len(result) >= k:
                break
        return result[:k]
