s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2

s|={'e':5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}

list= []

slow = {}
while True:

    wpis = input("Wpisz coś")
    if wpis == "":
        break
    # slow.get (wpis)
    n = slow.get (wpis,0)
    n += 1
    slow[wpis] = n

print (slow)


nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
dziesiatki = {10: "dziesiec", 20: "dwadziescia", 30: "trzydziesci", 40: "czterdziesci", 50: "piecdziesiat",
              60: "szescdziesiat", 70: "siedemdziesiat", 80: "osiemdziesiat", 90: "dziewiecdziesiat"}

nastki = {11: "jedenascie", 12: "dwanascie", 13: "trzynascie", 14: "czternascie", 15: "pietnascie",
          16: "szesnascie", 17: "siedemnascie", 18: "osiemnascie", 19: "dziewietnascie"}

slownik = {}

n = int(input("Wpisz liczbe:"))
if n in range(11, 20):
    napis = nastki[n]
else:
    napis = dziesiatki[n - n % 10] + " " + nazwy_jednosci[n % 10]

print(napis)

#drugi

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nastki = {0: "", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14:"czternaście", 15:"pietnascie", 16:"szesnaście",
          17: "siedemnascie", 18:"osiemnaście", 19:"dziewietnascie"}
dziesiatki = {0: "", 10: "dziesięć", 20: "dwadzieścia", 30: "trzydzieści",
                   40: "czterdzieści", 50: "pięćdziesiąt", 60: "sześćdziesiąt", 70: "siedemdziesiąt", 80: "osiemdziesiąt",
                 90: "dziewięćdziesiąt"}
setki = {0: "", 100: "sto", 200: "dwiescie", 300: "trzysta",
                   400: "czterysta", 500: "piecset", 600: "szescset", 700: "siedemset",
         800: "osiemset", 900: "dziewiecset"}
slownik = {}

n = int(input("wpisz liczbe:"))
napis = setki[n-n%100]
n%= 100
if n in range (11, 20):
    napis += nastki[n]
else:
    napis += dziesiatki[n-n%10] + " " + nazwy_jednosci[n%10]

print(napis)

#trzeci
#Slowniki :
nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_nast = {10: "dziesięć", 11: "jedenaście", 12: "dwanaście", 13: "trzynaście", 14: "czternaście", 15: "piętnaście", 16: "szesnaście", 17: "siedemnaście", 18: "osiemnaście",
                  19: "dziewiętnaście"}
nazwy_dziesiatek = {2: "dwadzieścia", 3: "trzydzieści", 4: "czterdzieści", 5: "pięćdziesiąt", 6: "sześćdziesiąt", 7: "siedemdziesiąt", 8: "osiemdziesiąt", 9: "dziewięćdziesiąt"}

nazwy_setek = {1: "sto", 2: "dwieście", 3: "trzysta", 4: "czterysta" , 5: "pięćset", 6: "sześćset", 7: "siedemset", 8: "osiemset", 9: "dziewięćset"}
#KOD:
liczba = int(input("Wpisz cyfre"))

g = int(liczba) // 100
d = (liczba % 100 ) // 10
j = liczba % 10
lista_2 = []
if g != 0:
    lista_2.append(nazwy_setek[g])
if d == 1:
    lista_2.append(nazwy_nast[liczba % 100])
else:
    lista_2.append(nazwy_dziesiatek[d])
    lista_2.append(nazwy_jednosci[j])
print (" ".join(lista_2) )