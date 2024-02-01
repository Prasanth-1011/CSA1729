fruit(Apple, Red).
fruit(Banana, Yellow).
fruit(Orange, Orange).
fruit(Grape, Purple).
fruit(Watermelon, Green).

color(Fruit, Color) :-
    fruit(Fruit, Color).
color(Fruit, Color) :-
    fruit(Fruit, Color);
    not(fruit(Fruit,_)),
    fail.
