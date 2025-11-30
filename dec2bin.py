import time
from fractions import Fraction
from decimal import Decimal


def parse_input(text):
    """Parsuje input na Fraction - obsługuje ułamki, notację naukową i zwykłe liczby"""
    text = text.strip()
    if "/" in text:
        # Ułamek np. "1/5"
        return Fraction(text)
    else:
        # Notacja naukowa lub zwykła liczba - przez Decimal dla precyzji
        return Fraction(Decimal(text))


def float_to_binary(frac):
    if frac < 0:
        print("-", end="")
        frac = -frac

    # Część całkowita
    integer_part = int(frac)
    fractional_part = frac - integer_part

    # Konwersja części całkowitej
    if integer_part == 0:
        print("0", end="")
    else:
        bits = []
        while integer_part > 0:
            bits.append(str(integer_part % 2))
            integer_part //= 2
        print("".join(reversed(bits)), end="")

    # Część ułamkowa
    if fractional_part > 0:
        print(".", end="")

        while fractional_part > 0:
            time.sleep(0.1)
            fractional_part *= 2
            if fractional_part >= 1:
                print("1", end="")
                fractional_part -= 1
            else:
                print("0", end="")

    print()


# Główna pętla
try:
    text = input("Podaj liczbę (np. 0.2, 1/5, 1e-10): ")
    frac = parse_input(text)
    print(f"Jako ułamek: {frac}")
    print("Binarnie: ", end="", flush=True)
    float_to_binary(frac)
except KeyboardInterrupt:
    print("\n\nPrzerwano.")
except Exception as e:
    print(f"Błąd: {e}")