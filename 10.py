with open("studenci.csv", "r", encoding="utf-8") as plik:
    linie = plik.readlines()

#print(linie)

for linia in linie[1:]:
    print(linia.strip().split(',')[0])

# surowe_dane = 'ala,ma,kota\n'
# dane_w_liscie = surowe_dane.strip().split(',')
# print(surowe_dane)
# print(dane_w_liscie)