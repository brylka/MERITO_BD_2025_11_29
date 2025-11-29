print("+"*50,"Moja aplikacja","+"*50, sep="\n")

a = float(input("Podaj liczbę pierwszą: "))
b = float(input("Podaj liczbę drugą: "))
c = a + b

print(f"Wynik dodawania: {a} + {b} = {c}")
print(f"Wynik odejmowania: {a} - {b} = {a-b}")
print(f"Wynik mnożenia: {a} * {b} = {a*b}")
if b == 0:
    print("Nie dzieli się przez zero")
else:
    print(f"Wynik dzielenia: {a} : {b} = {a/b}")
    print(f"Część całkowita dzielenia: {a//b}")
    print(f"Reszta z dzielenia: {a%b}")

