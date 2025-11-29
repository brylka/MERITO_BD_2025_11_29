# lista = [5,3,6,[1,[3.15,'Bartosz',13],3],10,-5,4,2,4,6,4,3,56,7,0,9,7,43,534,23,32,32,4]
# #        0 1 2 3       4
# print(lista[3][1][0])
# print(len(lista))
# print(lista[-23])

# imiona = []
#
# print("Podaj pięć imion:")
# for _ in range(5):
#     imie = input("Podaj imię: ")
#     imiona.append(imie)
#
# print(imiona)

imiona = ['Bartosz', 'Ala', 'Tomasz', 'Irena', 'Kazio']

# print(f"Lista pierwotna: {imiona}")
# imiona.append("Sebastian")
# print(f"Lista z dodanym rekordem: {imiona}")
# imiona.insert(1, "Tadeusz")
# print(f"Lista z dodanym rekordem w konkretne miejsce: {imiona}")
# imiona.remove('Tomasz')
# print(f"Lista z usuniętym konkretnym rekordem: {imiona}")
# imiona.pop()
# print(f"Lista z usuniętym ostatnim rekordem: {imiona}")
# imiona.pop(1)
# print(f"Lista z usuniętym rekordem o indeksie nr 1: {imiona}")

for a in range(len(imiona)):
    print(imiona[a])

for imie in imiona:
    print(imie)


