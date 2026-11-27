import pandas as pd

#odczyt pliku
# df = pd.read_excel(r'DATA\samochody.xlsx',sheet_name='dane')
# print(df.head(1))

df=pd.read_csv(r'DATA\dane_2_mln.csv',sep=';',encoding='utf-8')
# print(df_csv.head(1))

#test czy formaty git
# print(df.dtypes)
# print(df.columns.to_list)

# drogie=df[df['Cena_PLN']>150000]
# if drogie.empty:
#     print("brak")
# else:
#     print(drogie)


#filtrowanie
# kolumny=["Kolor",'Cena_PLN','Marka']
# filtr=((df['Kolor']=='Różowy') | (df['Kolor']=='Zielony'))&(df["Cena_PLN"]<=15000)
marka=df['Marka pojazdu']
marka=marka.str.upper()
# print(marka.head(20))
# filtr1=(df['Kolor'].isin(['Czarny','Biały']))&(df["Cena_PLN"]<=100000)&df['Marka'].str.contains("bmw",case=False)

# df_filtr=df.loc[filtr1,kolumny].sort_values(['Cena_PLN'],ascending=False)
# print(df_filtr)

# #szukanie brakujących informacji po wierszach (axis=0 to kolumny)
# brak=df[df.isna().any(axis=1)]
# print(brak)
# df['Cena_brutto']=df['Cena_PLN']*1.23
# print(df)

#połączenie kolumn ale nie usuwanie starej
# df["Autko"]=(df['Marka']+" "+df['Model'])
# print(df["Autko"])

#biale lub czerowne ladne inne brzydkie
df.loc[df["Kolor"].isin(['Czerwony','Biały']),"Czy_ładny"]='Ładny'
df.loc[~df["Kolor"].isin(['Czerwony','Biały']),"Czy_ładny"]='Brzydki'
# print(df.head().to_string())

# liczba=df["Cena_PLN"].count()
# suma=df["Cena_PLN"].sum()
# print(f'Liczba aut: {liczba}; suma cen: {suma}')

df["Marka_clean"]=marka

liczba_ofert=df.groupby("Marka_clean").size().reset_index(name='Ile ofert') #size - odpowiednik count
# print(liczba_ofert)

# lokalizacje=df['Lokalizacja'].unique()
# for lok in lokalizacje:
#     df_filtr=df.loc[df["Lokalizacja"]==lok]
#     car_stats=df_filtr.groupby("Marka_clean", as_index=False).agg(Liczba_ofert=("Cena netto","count"),Suma_cen=("Cena netto","sum"),Srednia_cena=("Cena netto",'mean')).sort_values('Liczba_ofert',ascending=False)
#     # print(car_stats)

#     # car_stats.to_csv(r'DATA\raport1.csv',index=False,sep=";")


#     moja_ramka=pd.DataFrame([{
#         "Marka_clean":"TOTAL",
#         "Liczba_ofert":car_stats['Liczba_ofert'].sum(),
#         "Suma_cen":car_stats["Suma_cen"].sum(),
#         "Srednia_cena":car_stats['Srednia_cena'].mean()
#     }])
#     # print(moja_ramka)

#     car_stats=pd.concat([car_stats,moja_ramka])
#     # print(car_stats)
#     car_stats.to_excel('DATA\\'+lok+'.xlsx',index=False)

#policz ile ładnych i ile brzydkich + ich udział%
ilosc=df.groupby('Czy_ładny').size().reset_index(name='Piekny') #size - odpowiednik count

brzydkie=ilosc['Piekny'][0]
ladne=ilosc['Piekny'][1]
total=brzydkie+ladne
rameczka=pd.DataFrame([{"Jaki kolor":"Ładny","Ile":ladne,"udział":ladne/total*100},{"Jaki kolor":"Brzydki","Ile":brzydkie,"udział":brzydkie/total*100},{"Jaki kolor":"TOTAL","Ile":total,"udział":total/total*100}])

print(rameczka)