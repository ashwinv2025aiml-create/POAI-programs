%Query Execution	 	 

% 1. Likes relationship

likes(mary, food).
likes(mary, wine).
likes(john, wine).
likes(john, mary).

likes(john, X) :- likes(mary, X).   % John likes anything Mary likes
likes(john, Y) :- likes(Y, wine).   % John likes anyone who likes wine
likes(john, Y) :- likes(Y, Y).      % John likes anyone who likes themselves

% ?- likes(john, food).
% true.
% ?- likes(john, wine).
% true.
% ?- likes(john, Y).
% Y = wine ;
% Y = mary ;
% Y = food ;
% Y = wine ;
% Y = mary ;
% Y = john ;
% ...   (press Enter to stop; the last rule keeps repeating john)


% 2. Placement eligibility (CGPA >= 7.5, no arrears, good communication)

cgpa(ash, 8.5).
cgpa(rahul, 7.2).
cgpa(priya, 9.1).

arrears(ash, 0).
arrears(rahul, 1).
arrears(priya, 0).

communication(ash, good).
communication(rahul, good).
communication(priya, average).

eligible(Student) :-
    cgpa(Student, C), C >= 7.5,
    arrears(Student, 0),
    communication(Student, good).

% ?- eligible(ash).
% true.
% ?- eligible(rahul).
% false.
% ?- eligible(priya).
% false.
% ?- eligible(S).
% S = ash.


% 3. Smart home automation

temperature(high).
light(dark).
home(yes).

action(turn_on_ac) :- temperature(high), home(yes).
action(turn_on_lights) :- light(dark), home(yes).
action(activate_alarm) :- home(no).

% ?- action(A).
% A = turn_on_ac ;
% A = turn_on_lights.
% (change the fact to home(no). to test the alarm: A = activate_alarm.)


% 4. Library management

registered(ash).
registered(priya).
registered(rahul).

overdue(ash, no).
overdue(priya, no).
overdue(rahul, no).

request(ash, book).
request(priya, book).
request(rahul, book).
available(book).

can_borrow(Student, Book) :-
    registered(Student),
    overdue(Student, no),
    request(Student, Book),
    available(Book).

% ?- can_borrow(ash, book).
% true.
% ?- can_borrow(S, book).
% S = ash ;
% S = priya ;
% S = rahul.


% 5. Elective course recommendation

interest(ash, ai).
interest(ash, python).
interest(priya, data_science).
interest(rahul, cyber_security).

recommend(Student, machine_learning) :- interest(Student, ai).
recommend(Student, machine_learning) :- interest(Student, python).
recommend(Student, data_analytics) :- interest(Student, data_science).
recommend(Student, ethical_hacking) :- interest(Student, cyber_security).

% ?- recommend(ash, C).
% C = machine_learning ;
% C = machine_learning.
% ?- recommend(priya, C).
% C = data_analytics.
% ?- recommend(rahul, C).
% C = ethical_hacking.


% 6. Family tree

parent(ram, sita).
parent(ram, raja).
parent(sita, anu).
parent(raja, deepa).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% ?- grandparent(ram, Y).
% Y = anu ;
% Y = deepa.
% ?- sibling(sita, raja).
% true.
% ?- ancestor(ram, X).
% X = sita ;
% X = raja ;
% X = anu ;
% X = deepa.
