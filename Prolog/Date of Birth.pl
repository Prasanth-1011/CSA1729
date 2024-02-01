dob(Siva, date(2002, 5, 15)).
dob(Sanjay, date(2005, 10, 20)).
dob(Guna, date(2004, 2, 8)).
dob(Suriya, date(2000, 7, 3)).
dob(Gowtham, date(2005, 9, 25)).
dob(Nithin, date(2002,8,9)).
dob(Prithvi, date(2003,2,22)).
dob(Pranav, date(2000,7,2)).
get(Name, DOB) :-
    dob(Name, DOB).
