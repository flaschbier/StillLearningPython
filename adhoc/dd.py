from collections import defaultdict

print "Enter car colours and ^C when done..."
try:
    car_count = defaultdict(int)
    while True:
        car_colour = raw_input("Car colour: ")
        car_count[car_colour] += 1
except KeyboardInterrupt:
    print
    print "Done with input, now the result"
    print

for c in car_count:
    print "Cars that are %s: %d" % (c, car_count[c])

"""
    $ python dd.py
    Enter car colours and ^C when done...
    Car colour: red
    Car colour: red
    Car colour: green
    Car colour: blue
    Car colour: ^C
    Done with input, now the result

    Cars that are blue: 1
    Cars that are green: 1
    Cars that are red: 2
    $
"""
