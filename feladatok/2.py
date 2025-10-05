"""2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.
"""

a  = int(input("Adj meg egy számot!"))
b  = int(input("Adj meg egy másik  számot!"))

if b > a:
    for i  in range(b - 1, a, -1):
        print(i)

elif a > b:
    for i in range(a - 1, b, -1 ):
        print(i)

else:
    print("A két szám egyenlő, nincs közöttük szám")