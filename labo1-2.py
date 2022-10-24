""""" zad 1 pole prostokąta

print('Obliczanie pola i obwodu prostokąta')
print('Podaj długości boków: ')
a = int(input("a =  "))
b = int(input("b =  "))
pole = a*b
obwod = 2*a+2*b
k1 = ""
print('Pole prostokata jest rowne: ', pole)
print('Obwód prostokąta jest równy: ', obwod) """


'''  zad 2 paliwo
d = int(input("długość drogi: "))
s = int(input("średnie spalanie(na 100 km): "))
cena = 6.5
sp = (d/100)*s
cp =  sp*cena
print('twój samochód spali ',sp ,'l paliwa' )
print('koszt paliwa wyniesie około: ', cp, 'zł' ) '''

'''import random
d = random.randint(1,1000)
s = int(input("średnie spalanie(na 100 km): "))
print('liczba kilometrow: ', d)
cena = 6.5
sp = (d/100)*s
cp =  sp*cena
print('twój samochód spali ',sp ,'l paliwa' )
print('koszt paliwa wyniesie około: ', cp, 'zł' )'''

'''zad bilety
wiek = int(input("Podaj swój wiek: "))
if wiek<4:
    print("Bilet dla Ciebie jest darmowy")
elif wiek>4 and wiek<18:
    print("Cena biletu 10zł")
else:
    print("Cena biletu 20zł")'''

'''zad wielkosc liter
z = str(input("Podaj literę: "))
duze = ["A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H", "I", "J", "K", "L", "Ł", "M", "N", "Ń", "O", "Ó", "P", "R", "S", "Ś", "T", "U", "W", "Y", "Z", "Ź", "Ż"]
male = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
if z in duze:
    print("Podana litera jest duża")
elif z in male:
    print("Podana litera jest mala")
else:
    print("Podany znak jest niepoprawny")'''

#zad kalkulator
print("Jaką operację chcesz wykonać? "
       "1)dodawanie"
       "2)odejmowanie"
       "3)mnożenie"
       "4)dzielenie"
       "5)potegowanie")
op = int(input("Podaj numer operacji: "))
a = int(input("Podaj argument 1:"))
b = int(input("Podaj argument 2:"))
if op == 1:
      print("wynik=",a + b)
elif op == 2:
      print("wynik=",a - b)
elif op == 3:
      print("wynik=",a * b)
elif op == 4:
      print("wynik=",a / b)
elif op == 5:
      print("wynik=",a ** b)