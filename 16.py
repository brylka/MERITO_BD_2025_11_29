start = 6
max = 30

print("Pn\tWt\tŚr\tCz\tPt\tSo\tNd")

print("\t" * (start-1), end="")

for dzien in range(1, max+1):
    print(dzien, end="\t")

    if (dzien + start-1) % 7 == 0:
        print()