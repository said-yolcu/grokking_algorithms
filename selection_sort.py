import utilities as util


def selection_sort(liste):
    end = len(liste)

    for high in range(end, 1, -1):
        m = 0
        i = 0

        for i in range(high):
            if liste[i] > liste[m]:
                m = i

        temp = liste[i]
        liste[i] = liste[m]
        liste[m] = temp

    return liste


if __name__ == "__main__":
    liste = [12, 23, 65, 23, 643, 651, 23, 54, 23, 7,
             46, 787, 4, 17, 4643, 53, 782, 346, 213, 13]

    # util.fill_fibo(liste, 15)

    

    print("Original list: ", liste)
    print("What it should be:    ", sorted(liste))
    print("When I sort the list: ", selection_sort(liste))
