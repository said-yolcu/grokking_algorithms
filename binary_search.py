import utilities as util

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


if __name__ == "__main__":
    liste = []

    util.fill_fibo(liste, 10)

    value = 56

    at = binary_search(liste, -1, len(liste), value)

    print("liste: ", liste)

    print("value at", at)
