:- module(solar_bot, [chat/0]).

% Knowledge Base: planet_info(Name, OrderFromSun, Moons, KeyFact)
planet_info(mercury, 1, 0, "the smallest planet and closest to the Sun").
planet_info(venus, 2, 0, "the hottest planet due to a dense greenhouse atmosphere").
planet_info(earth, 3, 1, "our home planet and the only world known to support life").
planet_info(mars, 4, 2, "known as the Red Planet due to iron oxide on its surface").
planet_info(jupiter, 5, 95, "the largest planet in the Solar System").
planet_info(saturn, 6, 146, "famous for its extensive, bright ring system").
planet_info(uranus, 7, 28, "an ice giant that uniquely rotates on its side").
planet_info(neptune, 8, 16, "the furthest planet from the Sun, known for extreme winds").

planet(P) :- planet_info(P, _, _, _).

% Main REPL loop
chat :-
    writeln('--- SolarBot Initialized ---'),
    writeln('Ask about planets (e.g., "tell me about mars", "how many planets", "largest planet", "hottest planet").'),
    writeln('Type "quit" or "exit" to end the session.'),
    nl,
    repeat,
    write('You: '),
    read_line_to_string(user_input, Input),
    string_lower(Input, Lower),
    split_string(Lower, " ", " .?!", Words),
    (   (member("quit", Words) ; member("exit", Words) ; member("bye", Words))
    ->  writeln('Bot: Goodbye! Safe travels through space!'), !
    ;   respond(Words),
        fail
    ).

% Intent 1: Specific planet lookup (e.g., "mars", "tell me about jupiter")
respond(Words) :-
    planet(P),
    atom_string(P, PStr),
    member(PStr, Words),
    !,
    planet_info(P, Order, Moons, Fact),
    format('Bot: ~w is planet #~w from the Sun. It has ~w moon(s) and is ~s.~n', [P, Order, Moons, Fact]).

% Intent 2: Total count of planets
respond(Words) :-
    member("planets", Words),
    (member("how", Words) ; member("many", Words) ; member("count", Words) ; member("total", Words)),
    !,
    aggregate_all(count, planet(_), Count),
    format('Bot: There are ~w recognized major planets in our solar system.~n', [Count]).

% Intent 3: Largest / Biggest planet
respond(Words) :-
    (member("largest", Words) ; member("biggest", Words)),
    !,
    planet_info(P, _, _, Fact),
    sub_string(Fact, _, _, _, "largest"),
    !,
    format('Bot: ~w is the largest planet in our solar system.~n', [P]).

% Intent 4: Smallest planet
respond(Words) :-
    member("smallest", Words),
    !,
    planet_info(P, _, _, Fact),
    sub_string(Fact, _, _, _, "smallest"),
    !,
    format('Bot: ~w is the smallest planet in our solar system.~n', [P]).

% Intent 5: Hottest planet
respond(Words) :-
    member("hottest", Words),
    !,
    planet_info(P, _, _, Fact),
    sub_string(Fact, _, _, _, "hottest"),
    !,
    format('Bot: ~w is the hottest planet in our solar system.~n', [P]).

% Intent 6: Querying moons
respond(Words) :-
    member("moons", Words),
    planet(P),
    atom_string(P, PStr),
    member(PStr, Words),
    !,
    planet_info(P, _, Moons, _),
    format('Bot: ~w has ~w moon(s).~n', [P, Moons]).

% Fallback response
respond(_) :-
    writeln('Bot: I am not sure about that. Try asking:'),
    writeln('  - "Tell me about Mars"'),
    writeln('  - "How many planets are there?"'),
    writeln('  - "What is the largest planet?"'),
    writeln('  - "Which planet is the hottest?"').
