# IMPLEMENTATION OF BACKWARD CHAINING

# Facts: known information (True / False)
facts = {
    'a': True,
    'b': True,
    'c': False
}

# Rules: (conclusion, [conditions])
rules = [
    ('d', ['a', 'b']),   # d is true if a and b are true
    ('e', ['b', 'c']),   # e is true if b and c are true
    ('f', ['d', 'e'])    # f is true if d and e are true
]


def backward_chaining(goal, facts, rules):
    """Return True if the goal can be proved from the facts and rules."""
    # If the goal is a known fact, use its value
    if goal in facts:
        return facts[goal]

    # Otherwise find a rule that concludes the goal and prove all its conditions
    for conclusion, conditions in rules:
        if conclusion == goal:
            if all(backward_chaining(c, facts, rules) for c in conditions):
                return True

    # The goal cannot be proved
    return False


if __name__ == "__main__":
    for goal in ['f', 'd']:
        if backward_chaining(goal, facts, rules):
            print(f"The goal '{goal}' can be achieved.")
        else:
            print(f"The goal '{goal}' cannot be achieved.")


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None (facts, rules and goals are fixed in the code)
#
# Output:
#   The goal 'f' cannot be achieved.
#   The goal 'd' can be achieved.
