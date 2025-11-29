with open("studenci.csv", "r", encoding="utf-8") as plik:
    linie = plik.readlines()

naglowki = linie[0].strip().split(',')
#print(naglowki)

dane = []
for linia in linie[1:]:
    wartosci = linia.strip().split(',')

    wiersz = {}
    for i in range(len(naglowki)):
        wiersz[naglowki[i]] = wartosci[i]
    dane.append(wiersz)

print(dane)

suma = 0
for student in dane:
    suma += float(student['wiek'])

srednia = suma/len(dane)

print(f"Średnia wieku: {srednia:.1f}")


#print(linie)

# for linia in linie[1:]:
#     print(linia.strip().split(',')[0])

# surowe_dane = 'ala,ma,kota\n'
# dane_w_liscie = surowe_dane.strip().split(',')
# print(surowe_dane)
# print(dane_w_liscie)