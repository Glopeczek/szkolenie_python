# bloki warunkowe
# kolor = "biały"
# if kolor == "różowy":
#     print("SUPER!")
# elif kolor != "biały":
#     print("kupie")
# else:
#     print("nie kupie")

kolor = "zielony"
cena = 60000
#kupie do 65k w kolorze zielonym
if (kolor=="zielony" or kolor == "biały") and \
    cena <= 65000:
    print("Kupie")
else:
    print("jakiś rabacik?")