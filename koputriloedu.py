# zad4.1
# print(input("Podaj imię kota:")+ " hmm...OK")

# zad 4.2
# print(input("Wpisz jakiś tekst:")*10)

#zad 6
# print(42, type(42), "Tajemnica", type("Tajemnica"), 3.14, type(3.14))

# zad7
# print (int(input("Liczba: "))+int(input("Liczba: ")))

#zad8
# print (int(input("Liczba: "))*int(input("Liczba: "))*int(input("Liczba: ")))

# zad 9
# print(int(float(input("Podaj liczbę z przecinkiem:"))))

# zad10
# print(input("Podaj napis małymi literami:").upper())

# zad11
# print(input("Podaj napis:").lower())

# print ("b"<"a")
# print("A">"a")

# zad13
# print(int(input("Liczba1:"))!= int(input("Liczba2:")))

#zad14
# print((int(input("Liczba1:"))+ int(input("Liczba2:")))<100)

#zad 17
# if input("Podaj hasło:")=="pizza":
#      print("Komnata otwarta!")

#zad18
# if input("Podaj pole kwadratu o boku 5:")=="25":
#     print("Brawo!")
# else:
#     print("Źle nieuku!")

#zad19
# if input("Podaj słowo:").find("samochód") != -1:
#     print('W podanym napisie znajduje się słowo "samochód"')

# a=1
# b=4
# c=3
# print("Średnia arytmetyczna liczb:", (a+b+c)/3)

#zad23
# tekst=input("wpisz tekst:")
# tekst+=input("wpisz tekst:")
# tekst+=input("wpisz tekst:")
# tekst+=input("wpisz tekst:")
# print(tekst)

# import time

#zad25
# print(1)
# time.sleep(1)
# print(2)
# time.sleep(1)
# print(3)
# time.sleep(1)
# print(4)
# time.sleep(1)
# print(5)
# time.sleep(1)

#zad26
# C=1
# for i in range(5):
#     print (C)
#     C+=1
#     time.sleep(1)

# zad27
# czas = int(input("Podaj l. sekund:"))
# if czas<10:
#     time.sleep(czas)
# else:
#     print("Nie będę tak długo czekać")

# print(time.gmtime()[3:6])

#zad30
# czas1=time.time()
# wynik_podany=int(input("Wpisz wynik mnożenia 5*5:"))
# print(wynik_podany)
# if wynik_podany==25:
#     czas2=time.time()
#     print("zajęło ci to:", czas2-czas1)
# else:
#     wynik_podany = int(input("Wpisz wynik mnożenia 5*5:"))

# #zad32
# print(time.strftime("%Y, %B, %d, %H:%M:%S", time.gmtime()))


# if time.gmtime()[-3]<4:
#     print ("Byle do piątku")
# elif time.gmtime()[-3]==4:
#     print("TGIF!")
# else:
#     print ("weekend")

# import random
#zad37
#a=3
# b=3*a
# print(random.randint(a,b))

#zad38
# napis=input("tekst:")
# multiplier=random.randint(1,15)
# print(napis*multiplier)

#powtorzeniowe4
# a=random.randint(1,10)
# b=random.randint(1,10)
# c=random.randint(1,10)
# print(a,b,c)
# answer=int(input("Największa to:"))
#
# if answer ==a:
#     if a>b and a>c:
#         print("prawidłowo")
#     else:
#         print("źle")
# if answer==b:
#     if b>a and b>c:
#         print("prawidłowo")
#     else:
#         print("źle")
# if answer==c:
#     if c>a and c>b:
#         print("prawidłowo")
#     else:
#         print("źle")
print("test")