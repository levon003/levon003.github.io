"""Exhaustive simulation of Penn & Teller's "Love Ritual" self-working card trick.

The trick (as described in the post):

  1. Shuffle 4 cards into a stack.
  2. Tear the stack in half, drop one half-stack on the other -> 8 half-cards.
  3. Put the top card on the bottom.
  4. Put the top 2 cards on the bottom.
  5. Put the top 3 cards (together) somewhere in the middle.
  6. Pull the top card aside -- the comparison card.
  7. Take 1, 2, or 3 cards from the top and put them somewhere in the middle.
  8. Put the top card somewhere in the middle.
  9. Throw away 1, 2, or 3 cards from the top.
 10. Seven times: put the top card on the bottom.
 11. Alternating until one card is left: top card to the bottom, then throw away the new top.
 12. The surviving card matches the comparison card.

We model 8 half-cards as integers 0..7. The card a half belongs to is `uid % 4`,
so half `u` and half `u+4` are the two halves of the same card. A "match" at the end
means survivor and comparison belong to the same card (same value mod 4).

The interesting question: steps 2, 5, 7, 8, 9 all contain free choices. Does the trick
still land on a match for *every* combination? And what exactly does "somewhere in the
middle" have to mean for that to hold?
"""

from itertools import product

TOP = 0  # index 0 is the top of the stack


def card(uid):
    return uid % 4


# --- the two physical ways to stack the torn halves (step 2's "free" choice) ---
# Top-halves are uids 0..3, bottom-halves are uids 4..7, each in card order 0..3.
BASE_TOPS_UP = [0, 1, 2, 3, 4, 5, 6, 7]   # top-halves stack placed on top
BASE_BOTS_UP = [4, 5, 6, 7, 0, 1, 2, 3]   # bottom-halves stack placed on top


def rot(stack, k):
    """Move the top k cards to the bottom (a straight cut)."""
    k %= len(stack)
    return stack[k:] + stack[:k]


def take_top_to_middle(stack, m, pos):
    """Remove the top `m` cards (as a block, order preserved) and reinsert them
    into the remainder at index `pos`. pos is an index into the remaining stack."""
    block, rest = stack[:m], stack[m:]
    return rest[:pos] + block + rest[pos:]


def down_under(stack):
    """Step 11: one card under (to the bottom), next card off (discarded), repeat."""
    s = list(stack)
    while len(s) > 1:
        s = s[1:] + s[:1]   # under
        s = s[1:]           # off
    return s[0]


def run(base, pos5, k7, pos7, pos8, k9):
    """Run the whole trick for one set of choices. Returns (comparison, survivor)."""
    s = list(base)
    s = rot(s, 1)                          # step 3
    s = rot(s, 2)                          # step 4
    s = take_top_to_middle(s, 3, pos5)     # step 5  (block of 3 into the middle)
    comparison = s[TOP]                    # step 6
    s = s[1:]
    s = take_top_to_middle(s, k7, pos7)    # step 7  (block of k7 into the middle)
    s = take_top_to_middle(s, 1, pos8)     # step 8  (single card into the middle)
    s = s[k9:]                             # step 9  (throw away k9 from the top)
    s = rot(s, 7)                          # step 10
    survivor = down_under(s)               # step 11
    return comparison, survivor


def interior_positions(stack_len_after_removal):
    """'Somewhere in the middle' = strictly interior: not the very top (0) and not
    the very bottom (== len). Returns the list of valid insertion indices."""
    return list(range(1, stack_len_after_removal))   # 1 .. len-1


def all_positions(stack_len_after_removal):
    return list(range(0, stack_len_after_removal + 1))  # 0 .. len  (incl. top & bottom)


def sweep(position_fn, label):
    total = ok = 0
    failures = []
    for base in (BASE_TOPS_UP, BASE_BOTS_UP):
        # after steps 3,4 there are 8 cards; step 5 removes 3 -> remainder of 5
        for pos5 in position_fn(5):
            for k7 in (1, 2, 3):
                # after step 6 there are 7 cards; step 7 removes k7 -> remainder 7-k7
                for pos7 in position_fn(7 - k7):
                    # step 8 removes 1 -> remainder 6
                    for pos8 in position_fn(6):
                        for k9 in (1, 2, 3):
                            comp, surv = run(base, pos5, k7, pos7, pos8, k9)
                            total += 1
                            if card(comp) == card(surv):
                                ok += 1
                            else:
                                failures.append((base[0], pos5, k7, pos7, pos8, k9))
    print(f"{label}: {ok}/{total} matches  ({100*ok/total:.1f}%)")
    return failures


if __name__ == "__main__":
    print("Sweeping every spectator choice.\n")
    print('Reading "somewhere in the middle" as STRICTLY INTERIOR (never top, never bottom):')
    f_interior = sweep(interior_positions, "  interior-only")

    print('\nReading "somewhere in the middle" as ANY slot except the very top'
          ' (i.e. the bottom counts as a candidate):')
    f_loose = sweep(all_positions, "  any slot incl. bottom")

    if f_loose:
        print(f"\n  {len(f_loose)} failures under the loose reading.")
        # Characterize exactly which placements break it:
        #   - step 5 block on the very TOP (0) changes which card becomes the comparison
        #     card while its partner is left at the bottom -> mismatch.
        #   - step 5 block on the very BOTTOM (5) displaces the partner from the bottom.
        #   - steps 7/8 on the very BOTTOM displace the partner; on the very TOP they're
        #     harmless (the card simply goes back where it started).
        breaks = lambda b, pos5, k7, pos7, pos8, k9: (
            pos5 in (0, 5) or pos7 == (7 - k7) or pos8 == 6
        )
        explained = all(breaks(*x) for x in f_loose)
        safe_but_failed = [x for x in f_loose if not breaks(*x)]
        print("  Every failure is explained by 'a block landed on the very top or very"
              f" bottom of its stack': {explained}")
        print(f"  Failures NOT explained by that rule: {len(safe_but_failed)}")
