# from tkinter import simpledialog
# # bloki warunkowe
# # kolor = "biały"
# # if kolor == "różowy":
# #     print("SUPER!")
# # elif kolor != "biały":
# #     print("kupie")
# # else:
# #     print("nie kupie")

# # kolor = "zielony"
# # cena = 60000
# # #kupie do 65k w kolorze zielonym
# # if (kolor=="zielony" or kolor == "biały") and \
# #     cena <= 65000:
# #     print("Kupie")
# # else:
# #     print("jakiś rabacik?")


# #input uzytkownika
# # cena=input("Podaj maksymalną cenę w liczbach całkowitych: ")
# # if cena=="":
# #     print("Brak liczby")
# # elif cena.isdigit()==False: #alternatywny zapis elif not cena.isdigit():
# #     print("Input to nie liczba całkowita")
# # else:
# #     cena=float(cena)
# #     print(f"Podałeś że maksymalna cena to: {cena:.2f} zł")


# #użycie biblioteki do kontroli inputu -  od razu robi float i nie musi byc calkowite

# kurs=simpledialog.askfloat("kurs", "Podaj kurs walut:  ",initialvalue=0.0)
# if kurs==None:
#     print("STOP!")
# elif kurs==0:
#     print("Kurs musi być różny od zera!")
# else:
#     tekst_CSV = "03/22/2025 marek piKNY wypłata PLN: 8000"
#     rok = tekst_CSV[6:10]
#     miesiac = tekst_CSV[0:2]
#     dzien = tekst_CSV[3:5]
#     spacja = tekst_CSV.find(" ")
#     druga_spacja = tekst_CSV.find(" ", spacja + 1)
#     trzecia_spacja = tekst_CSV.find(" ", druga_spacja + 1)
#     imie = tekst_CSV[spacja + 1 : druga_spacja].title()
#     nazwisko = tekst_CSV[druga_spacja + 1 : trzecia_spacja].title()
#     pln = tekst_CSV.find("PLN: ")
#     kasa = float(tekst_CSV[pln + 5 :]) / kurs

#     print(
#         f"{rok}-{miesiac}-{dzien} \nImie i Nazwisko: {imie} {nazwisko}\nKasa Euro: {kasa:.2f}"
#     )

#for w listach
cars = ["audi", "bmw", "skoda", "kia"]
i = 1
for car in cars:
    print(f"Autko_{i}: {car}")
    i = i + 1

# # alternatywa
# i = 1
# for id in range(len(cars)):
#     print(f"Autko_{i}: {cars[id]}")
#     i = i + 1


# #for w słownikach
# garaz={"Toyota":'Corolla', "Mazda":'MX-5', 'BMW':'M3', 'Tesla':'Model S'}
# for marka,model in garaz.items():
#     print(f'Marka: {marka}; Model: {model}')

# auta_szczegoly = {
# "WA12345": {"marka": "Toyota", "rok": 2020, "przebieg": 50000},
# "KR67890": {"marka": "BMW", "rok": 2018, "przebieg": 120000}
# }

#alternatywa
from pojazdy import auta_szczegoly as furki
for blacha,y in furki.items():
    przebieg=y["przebieg"]
    print(f"Nr rej. to: {blacha} , a przebieg to: {przebieg}")


from prettytable import PrettyTable as pt
tabelka=pt(["Marka","Rocznik"])
from pojazdy import garaz
for marka,y in garaz.items():
    rocznik=y[1][0]
    #print(f'Marka: {marka}, rocznik: {rocznik}')
    tabelka.add_row([marka,rocznik])
print(tabelka)
csv=tabelka.get_csv_string() #tworzy format przyajzny dla csv
