# IMPLEMENTATION OF FORWARD CHAINING

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


def forward_chaining(facts, rules, goal):
    """Start from the known true facts and keep applying rules until
    nothing new can be inferred. Return True if the goal is inferred."""
    # Only facts that are True count as known
    inferred = {fact for fact, value in facts.items() if value}

    new_fact_added = True
    while new_fact_added:
        new_fact_added = False
        for conclusion, conditions in rules:
            if conclusion not in inferred and all(c in inferred for c in conditions):
                inferred.add(conclusion)
                new_fact_added = True

    return goal in inferred


if __name__ == "__main__":
    for goal in ['f', 'e', 'd']:
        if forward_chaining(facts, rules, goal):
            print(f"The goal '{goal}' can be achieved.")
        else:
            print(f"The goal '{goal}' cannot be achieved.")


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None (facts, rules and goals are fixed in the code)
#
# Output:
#   The goal 'f' cannot be achieved.
#   The goal 'e' cannot be achieved.
#   The goal 'd' can be achieved.
