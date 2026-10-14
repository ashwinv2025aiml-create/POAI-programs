% Find minimum and maximum of two numbers

% Minimum of two numbers
minimum(X, Y, X) :- X =< Y.   % If X <= Y, X is the minimum
minimum(X, Y, Y) :- X > Y.    % If X > Y, Y is the minimum

% Maximum of two numbers
maximum(X, Y, X) :- X >= Y.   % If X >= Y, X is the maximum
maximum(X, Y, Y) :- X < Y.    % If X < Y, Y is the maximum

% ---------------- QUERIES / OUTPUT ----------------
% ?- minimum(5, 10, Min).
% Min = 5.
%
% ?- maximum(5, 10, Max).
% Max = 10.
%
% ?- minimum(8, 3, Min), maximum(8, 3, Max).
% Min = 3,
% Max = 8.
