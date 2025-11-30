def dodaj(a, b):
    return a + b

assert dodaj(2, 3) == 5
assert dodaj(-1, 1) == 0
assert dodaj(0, 0) == 0

# assert dodaj(0.1, 0.2) == 0.3
assert abs(dodaj(0.1, 0.2) - 0.3) < 0.00001
