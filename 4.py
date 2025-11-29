# lista = [5,3,6,[1,[3.15,'Bartosz',13],3],10,-5,4,2,4,6,4,3,56,7,0,9,7,43,534,23,32,32,4]
# #        0 1 2 3       4
# print(lista[3][1][0])
# print(len(lista))
# print(lista[-23])

imiona = []

print("Podaj pięć imion:")
for _ in range(5):
    imie = input("Podaj imię: ")
    imiona.append(imie)

print(imiona)
