def czesc(imie):
    print(f"Witaj, {imie}!")
    print("MERITO")

#czesc("Bartosz")
#czesc("Paweł")

def tablizcka(max=10):
    for b in range(0, max+1):
        for a in range(0, max+1):
            if a == 0 and b == 0:
                print("\033[31m*\033[0m", end="\t")
            elif a == 0:
                print(b, end="\t")
            elif b == 0:
                print(a, end="\t")
            elif a == b:
                print('\033[31m', a * b, '\033[0m', sep="", end="\t")
            else:
                print(a * b, end="\t")
        print()

#tablizcka(15)

def dodaj(a, b):
    return a + b

# c = dodaj(2,3)
# print(c)


if __name__ == '__main__':
    tablizcka()