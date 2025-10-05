""". Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

helyes_jelszo = "python123"

beirt_jelszo = ""

while beirt_jelszo != helyes_jelszo:
    beirt_jelszo = input ("Add meg a jelszót!")

print("Sikeres belépés")