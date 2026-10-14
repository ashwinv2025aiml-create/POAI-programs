#IMPLEMENTATION OF UNIFICATION AND RESOLUTION ALGORITHM

from itertools import combinations


# ---------------------------------------------------------
# Part A: Unification
# Variables are lowercase (x, y); constants and predicate/function
# names start with a capital letter (A, P, F); terms are lists.
# ---------------------------------------------------------
def is_variable(term):
    return isinstance(term, str) and term[:1].islower()


def occurs_check(var, term, subst):
    """Check for cyclic dependencies (var occurring inside term)."""
    if var == term:
        return True
    if is_variable(term) and term in subst:
        return occurs_check(var, subst[term], subst)
    if isinstance(term, list):
        return any(occurs_check(var, t, subst) for t in term)
    return False


def unify_var(var, term, subst):
    """Handle unification for variables."""
    if var in subst:
        return unify(subst[var], term, subst)
    if is_variable(term) and term in subst:
        return unify(var, subst[term], subst)
    if occurs_check(var, term, subst):
        return None
    return {**subst, var: term}


def unify(x, y, subst):
    """Return the substitution that makes x and y identical, or None."""
    if subst is None:
        return None
    if x == y:
        return subst
    if is_variable(x):
        return unify_var(x, y, subst)
    if is_variable(y):
        return unify_var(y, x, subst)
    if isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        for a, b in zip(x, y):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    return None


def show_unify(x, y):
    result = unify(x, y, {})
    print(f"unify({x}, {y})")
    print("  ->", result if result is not None else "Unification fails")


# ---------------------------------------------------------
# Part B: Resolution (propositional)
# A clause is a set of literals; "~P" is the negation of "P".
# ---------------------------------------------------------
def negate(literal):
    """Negate a literal."""
    return literal[1:] if literal.startswith("~") else "~" + literal


def fmt(clause):
    return "{" + ", ".join(sorted(clause)) + "}" if clause else "{} (empty clause)"


def resolve(c1, c2):
    """Resolve two clauses to find their resolvents."""
    resolvents = []
    for lit in c1:
        if negate(lit) in c2:
            resolvents.append((c1 - {lit}) | (c2 - {negate(lit)}))
    return resolvents


def resolution(kb, query):
    """
    Resolution refutation: add the negated query to the knowledge base.
    Returns True if the empty clause is derived (KB + ~query is
    unsatisfiable, so the query follows from the KB), otherwise False.
    """
    clauses = [frozenset(c) for c in kb]
    negated_query = frozenset([negate(query)])
    if negated_query not in clauses:
        clauses.append(negated_query)

    while True:
        new = []
        for c1, c2 in combinations(clauses, 2):
            for r in resolve(c1, c2):
                r = frozenset(r)
                if r in clauses or r in new:
                    continue
                print(f"  Resolve {fmt(c1)} and {fmt(c2)} -> {fmt(r)}")
                if not r:
                    return True
                new.append(r)
        if not new:
            return False
        clauses.extend(new)


def run_resolution(kb, query):
    print("Knowledge Base:", kb)
    print("Query:", query)
    if resolution(kb, query):
        print("Empty clause derived: KB + negated query is NOT satisfiable,")
        print("so the query is PROVED.")
    else:
        print("No empty clause: KB + negated query is satisfiable,")
        print("so the query CANNOT be proved.")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------
if __name__ == "__main__":
    print("===== Unification =====\n")
    show_unify(['P', 'x'], ['P', 'A'])
    show_unify(['P', 'x', 'y'], ['P', 'A', 'x'])
    show_unify(['P', 'x', ['F', 'y']], ['P', 'A', ['F', 'B']])
    show_unify(['P', 'A'], ['P', 'B'])
    show_unify('x', ['F', 'x'])

    print("\n===== Resolution =====\n")
    knowledge_base = [["~P", "Q"], ["P"], ["~Q", "R"], ["~R"]]
    run_resolution(knowledge_base, "R")

    print("\n--- Second example (knowledge base without ~R) ---\n")
    run_resolution([["~P", "Q"], ["P"], ["~Q", "R"]], "S")


# ---------------- INPUT / OUTPUT ----------------
# Input:
#   None (the terms, knowledge base and queries are fixed in the code)
#
# Output:
#   ===== Unification =====
#
#   unify(['P', 'x'], ['P', 'A'])
#     -> {'x': 'A'}
#   unify(['P', 'x', 'y'], ['P', 'A', 'x'])
#     -> {'x': 'A', 'y': 'A'}
#   unify(['P', 'x', ['F', 'y']], ['P', 'A', ['F', 'B']])
#     -> {'x': 'A', 'y': 'B'}
#   unify(['P', 'A'], ['P', 'B'])
#     -> Unification fails
#   unify(x, ['F', 'x'])
#     -> Unification fails
#
#   ===== Resolution =====
#
#   Knowledge Base: [['~P', 'Q'], ['P'], ['~Q', 'R'], ['~R']]
#   Query: R
#     Resolve {Q, ~P} and {P} -> {Q}
#     Resolve {Q, ~P} and {R, ~Q} -> {R, ~P}
#     Resolve {R, ~Q} and {~R} -> {~Q}
#     Resolve {Q, ~P} and {~Q} -> {~P}
#     Resolve {P} and {R, ~P} -> {R}
#     Resolve {Q} and {~Q} -> {} (empty clause)
#   Empty clause derived: KB + negated query is NOT satisfiable,
#   so the query is PROVED.
#
#   --- Second example (knowledge base without ~R) ---
#
#   Knowledge Base: [['~P', 'Q'], ['P'], ['~Q', 'R']]
#   Query: S
#     Resolve {Q, ~P} and {P} -> {Q}
#     Resolve {Q, ~P} and {R, ~Q} -> {R, ~P}
#     Resolve {P} and {R, ~P} -> {R}
#   No empty clause: KB + negated query is satisfiable,
#   so the query CANNOT be proved.
