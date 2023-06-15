import random as rnd

def fill_fibo(liste, until):
    a = 1
    b = 1

    liste.append(b)

    for i in range(until-2):
        b, a = a+b, b
        liste.append(b)

def fill_rand(liste, until, upto):

    for i in range(until):
        liste.append(rnd.randint(0,upto))

def swap(liste, left, right):
    temp = liste[left]
    liste[left] = liste[right]
    liste[right] = temp    