symptom(high_temperature).
symptom(cough).
symptom(skin_rash).

% Rules
has_symptom(high_temperature) :- has_condition(fever).
has_symptom(cough) :- has_condition(flu).
has_symptom(skin_rash) :- has_condition(allergy).

has_condition(fever).
has_condition(flu).
has_condition(allergy).

% Backward chaining
backward_chain(Patient, Hypothesis) :-
    writeln('Checking for symptoms in reverse order:'),
    has_symptom(Symptom),
    writeln('Patient may have:'),
    writeln(Symptom).

% Example usage
?- backward_chain(john, Hypothesis).
