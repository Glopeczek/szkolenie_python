# import
import cowsay

# Ctrl+/

# różnice w print
# print("tekst","inny tekst",sep="-")
# print("tekst"+"inny tekst")
# print("X"* 60)

# zmienne
x = 2
y = 10
print(x + y)

# kilka zmiennych w jednym wierszu
z1, z2, z3 = 1, 1234.48938493893, 3
print(z1, z2, z3)

w = True  # bool

# zaokraglenie wyniku
# round(wynik,2)

# "f" w print łączy teksty z zawartością zmiennych - F string
print(f"lubie {z1} bardziej niż {z3}, a najbardziej {z2:.2f}")

# :.xf zaokrągla do x miejsc po przecinku (. - angielskie rozdzielenie)
# :,.xf dodatkowo dodaje przecinek co każde 3 cyfry np. 1,234.12

# replace
ładna_liczba = f"{z2:_.2f}".replace("_", " ").replace(
    ".", ","
)  # zamiana _ na spację i . na , w liczbie
print(f"Liczba = {ładna_liczba}")

# len - ilość znaku stringa
print(len(ładna_liczba))

# operacje na stringach

# wypisanie znaków z przedziału
b = "zdzichu"
print(b[2:4])  # python liczy od 0 dodatkowo ten nawias to tak naprawdę < )

# str są niezmienne dlatego trzeba je nadpisywac lub tworzyc nowa zmienna
b = b.title()  # title zmienia pierwszą literę na wielką
print(b)

# łańcuch wywołań - dużo funkcji po kropkach

# b="jan kowalski"
# spacja = b.find(" ")
# print(b[spacja+1:100])


# ĆWICZENIE

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
rok = tekst_CSV[6:10]
miesiac = tekst_CSV[0:2]
dzien = tekst_CSV[3:5]
spacja = tekst_CSV.find(" ")
druga_spacja = tekst_CSV.find(" ", spacja + 1)
trzecia_spacja = tekst_CSV.find(" ", druga_spacja + 1)
imie = tekst_CSV[spacja + 1 : druga_spacja].title()
nazwisko = tekst_CSV[druga_spacja + 1 : trzecia_spacja].title()
pln = tekst_CSV.find("PLN: ")
kasa = float(tekst_CSV[pln + 5 :]) / 4.33

print(
    f"Rok: {rok} \nMiesiąc: {miesiac} \nDzień: {dzien} \nImie i Nazwisko: {imie} {nazwisko}\nKasa Euro: {kasa:.2f}"
)


tekst_CSV = "03/22/2025 marek piKNY wypłata PLN: 696969"
rok = tekst_CSV[6:10]
miesiac = tekst_CSV[0:2]
dzien = tekst_CSV[3:5]
spacja = tekst_CSV.find(" ")
druga_spacja = tekst_CSV.find(" ", spacja + 1)
trzecia_spacja = tekst_CSV.find(" ", druga_spacja + 1)
imie = tekst_CSV[spacja + 1 : druga_spacja].title()
nazwisko = tekst_CSV[druga_spacja + 1 : trzecia_spacja].title()
pln = tekst_CSV.find("PLN: ")
kasa = float(tekst_CSV[pln + 5 :]) / 4.33

print(
    f"Rok: {rok} \nMiesiąc: {miesiac} \nDzień: {dzien} \nImie i Nazwisko: {imie} {nazwisko}\nKasa Euro: {kasa:.2f}"
)

#operacje czas
from datetime import datetime, date, timedelta
teraz=datetime.now()
print(f"Teraz jest: {teraz}")

urodziny = date(1995,10,10)
print(f"Urodzony: {urodziny}")

#arytmetyka 
przyszłość = teraz + timedelta(days=100)
print(przyszłość)

ładna_data = teraz.strftime("%m.%d.%Y")
print(f"Ameryczka data: {ładna_data}")

data = tekst_CSV[0:10]
git_data = datetime.strptime(data,"%m/%d/%Y")
print(f"data:{git_data.date()}")