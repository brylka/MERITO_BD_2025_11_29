# slownik = {"krol": "Bartosz", 1: "Ala", 2: "Tomasz", 3: "Irena", 4: "Kazio"}
#
# print(slownik["krol"])
#
# slownik["krolowa"] = "Katarzyna"
#
# print(slownik)
#
# slownik[1] = ["ala", "ma", "kota"]
# slownik["test"] = "dane testowe!"
# print(slownik.get("test", "brak danych"))

slownik = {"krol": "Bartosz", 1: "Ala", 2: "Tomasz", 3: "Irena", 4: "Kazio"}

# iterowanie po kluczach
for klucz in slownik:
    print(klucz)

# iterowanie po wartościach
for wartosc in slownik.values():
    print(wartosc)

# interowanie po elementach
for klucz, wartosc in slownik.items():
    print(f"{klucz} -> {wartosc}")