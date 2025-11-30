start = 6
max = 30

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