# Tworzenie pliku CSV do ćwiczeń
dane =  """imie,nazwisko,wiek,miasto,ocena
Jan,Kowalski,25,Warszawa,4.5
Anna,Nowak,30,Kraków,3.8
Piotr,Wiśniewski,22,Gdańsk,4.2
Maria,Zielińska,28,Poznań,4.9
Tomasz,Lewandowski,35,Wrocław,3.5
Ewa,Kamińska,24,Łódź,4.0"""

with open("studenci.csv", "w", encoding="utf-8") as plik:
    plik.write(dane)

print("Plik studenci.csv został utworzony!")
