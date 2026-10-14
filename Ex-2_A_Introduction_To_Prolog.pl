/*
Ex No: 2-A
INTRODUCTION TO PROLOG

THEORY:
Prolog (PROgramming in LOGic) is a declarative logic programming language
based on formal logic. Instead of specifying how to solve a problem, the
programmer states what is true, and Prolog finds the answer by itself.
It is mainly used in Artificial Intelligence, expert systems, knowledge
representation and natural language processing.

A Prolog program consists of:
1. Facts   - statements that are true.            e.g. parent(john, mary).
2. Rules   - relationships defined by conditions. e.g. father(X, Y) :- male(X), parent(X, Y).
3. Queries - questions asked to the system.       e.g. ?- father(john, mary).

Key concepts:
- Atom        : a constant name, e.g. john, apple.
- Variable    : starts with a capital letter or _, e.g. X, Person.
- Predicate   : a relationship, written as name/arity, e.g. parent/2.
- Unification : matching two terms by assigning values to variables.
- Backtracking: searching for alternative solutions when one fails.
- Recursion   : a predicate that calls itself.
- Cut (!)     : stops Prolog from backtracking past that point.
- Negation    : \+ means "cannot be proven".

Operators: a comma (,) means AND, a semicolon (;) means OR.
*/

% Facts
male(john).
male(peter).
female(mary).

parent(john, mary).
parent(john, peter).
parent(mary, david).

% Rules
father(X, Y) :- male(X), parent(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

/*
QUERIES OUTPUT:

?- father(john, mary).
true.

?- grandparent(john, david).
true.

?- parent(john, X).
X = mary ;
X = peter.
*/
