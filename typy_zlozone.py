# listy
owoce = ["jabłko", "banan", "wiśnia", "banan"]
print(owoce)
owoce[3]="truskawka"
print(owoce)
owoce.sort() #lista jest zmienialna dlatego funkcje dzialaja na nich bezposrednio
# print(owoce[1])
# print(owoce[1:])
print(owoce)
owoce.append(["kiwi","mango"])#lista w liście
print(owoce)

owoce.extend(["kiwi","mango"])#lista płaska - część oryginalnej listy

print(owoce)

owoce = [["jabłko", "banan", "wiśnia", "banan"],["jabłko", "banan", "wiśnia", "mango","jajo"]]
el=owoce[1][3] #pierwszy wymar to wiersz a drugi kolumna tablica[w][k]
print(el)
print(owoce[0])
print(len(owoce[1])) #len dla tablicy liczy ilość komórek

tekst_CSV = "03/22/2025 marek piKNY wypłata PLN: 696969"
moja_lista = tekst_CSV.split(" ") #robi split po seperatorze
print(moja_lista)

#extend test
moja_lista.extend(moja_lista[1]+" "+moja_lista[2])
print(moja_lista)

#append test
moja_lista = tekst_CSV.split(" ") #robi split po seperatorze
moja_lista.append(moja_lista[1]+" "+moja_lista[2])
print(moja_lista)

#usun komorki ktore maja pojedynczo imie i nazwisko
moja_lista.pop(1)
moja_lista.pop(1)
print(moja_lista)

#alternatywa
# del moja_lista[2:4]

#koryguj znaki w imieniu i nazwisku
moja_lista[-1]=moja_lista[-1].title() #tak bo string jest w komórce a on nie jest zmienialny wiec trzeba nadpisac
print(moja_lista)
print("*"*120)

#krotki - tuple
#-lista która jest niezmienna
owoce_krotka = ("jabłko", "banan", "wiśnia", "banan")

print(owoce_krotka[0])

#rozpakowanie krotki do pojedynczych zmiennych
krotka=(1,2,3)
m,n,b=krotka
print(f"{m} , {n} , {b}")


#zestawy, zbiory, sety - coś unikalnego dla Pythona - nie pozwala na duplikaty

owoce_set = {"jabłko", "banan", "wiśnia", "banan"}
print(owoce_set)

owoce=list(owoce_set) #zrobienie tablicy z setu (tak samo z krotki)
print(owoce)

#usuwanie powtórek z listy
numery=[1,1,1,1,2,3,3,3,3,4]
bez_dupli=list(set(numery))
print(bez_dupli)


#słowniki - typ (na lewo od :) niezmienialny w środku (nie mozna dać listy ale krotke tak) -wartość nie ma tego ograniczenia
slownik={"marka":"Ford", "model":"Mondeo", "rocznik":2000, "wlasciwosci":["skora","klima"]}
print(slownik["model"], slownik["wlasciwosci"][0])

#dodaj nowe
slownik["rocznik"]=1999
slownik["kolor"]="srebrny"
print(slownik)

print(slownik.items())