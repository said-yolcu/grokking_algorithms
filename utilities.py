
def fill_fibo(liste, until):
    a = 1
    b = 1

    liste.append(b)

    for i in range(until-2):
        b, a = a+b, b
        liste.append(b)
