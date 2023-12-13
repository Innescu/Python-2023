l = list(range(5, 10))
print(l)
i = int(input("podaj indeks "))
print(f'Pod indeksem {i} jest element {l[i]}')


suma = 0
while True:
    try:
        inp = str(input("Podaj liczbe"))
        for c in inp:
            suma += int(c)
        print(suma)
        if inp == "":
            break
    except IndexError as e:
        print(e)
    except ValueError as e:
        print("In Value Error")
        print(e)
    except Exception as e:
        print("In Exception")
        print(e)
    else:
        break
    finally:
        print("Finally")