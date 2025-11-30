from datetime import datetime

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))

start = datetime(rok, miesiac, 1).weekday() + 1

if miesiac in [1, 3, 5, 7, 8, 10, 12]:
    max = 31
elif miesiac in [4, 6, 9, 11]:
    max = 30
elif miesiac == 2:
    if (rok % 4 == 0 and rok % 100 != 0) or rok % 400 == 0:
        max = 29
    else:
        max = 28


print("Pn\tWt\tŚr\tCz\tPt\t\033[33mSo\t\033[31mNd\033[0m")

print("\t" * (start - 1), end="")

for dzien in range(1, max+1):
    if (dzien + start - 1) % 7 == 0:
        print('\033[31m', end="")
    if (dzien + start - 1) % 7 == 6:
        print('\033[33m', end="")
    print(dzien, end="\t")
    print('\033[0m', end="")

    if (dzien + start-1) % 7 == 0:
        print()