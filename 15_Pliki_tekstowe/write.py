f = open('plik.txt', 'w')
f.write("Hello\n")
f.close()
#1
import os
print(os.getcwd())

with open('data/foods.csv') as f:
    for l in f:
        dane = l.strip().split(',')
        print ("\t".join(dane))


#2
import os
print(os.getcwd())

first_line = None
data = []
with open('data/foods.csv') as f:
    for l in f:
        if first_line is None:
            first_line = l.strip().split(',')
        else:
            dane = l.strip().split(',')

            slownik = dict(zip(first_line, dane))
            print(slownik)