slowo = "Kamil Ślimak"
print(slowo[::-1].lower().replace(" ", ""))

if slowo.lower().replace(" ","") == slowo[::-1].lower().replace(" ", ""):
    print("palindrom!")
else:
    print("nie palindrom")


lista = [123,456,"ala",789,"ma","ostatni"]
print(lista)
print(lista[::-1])
print(lista[0:3:2])