def binary_search(liste, low, high, value):

    while (high-low > 1):
        mid = (high+low)//2

        if liste[mid] < value:
            low = mid
        elif liste[mid] > value:
            high = mid
        else:  # liste[mid] == value
            return mid

    return -1


def fill_fibo(liste, until):
    a = 1
    b = 1

    liste.append(b)

    for i in range(until-2):
        b, a = a+b, b
        liste.append(b)


if __name__ == "__main__":
    liste = []

    fill_fibo(liste, 10)

    value = 56

    at = binary_search(liste, -1, len(liste), value)

    print("liste: ", liste)

    print("value at", at)
