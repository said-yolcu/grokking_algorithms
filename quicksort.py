import utilities as util
import selection_sort as sel

# Sums the elements in an array using the divide-and-conquer method
def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])


# Find the maximum of an array using divide-and-conquer method
def find_max(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        tail_max = find_max(arr[1:])

        if arr[0] >= tail_max:
            return arr[0]
        else:
            return tail_max

# Sort the array with quicksort starting in the interval [sta, end)
def quicksort(liste, sta, end):
    l = end-sta

    # If length is 0 or 1, return the list
    if l == 0 or l == 1:
        return liste

    pivots = [liste[sta], liste[sta + l//2], liste[end - 1]]

    # Sort the first, middle and last elements and select the element in
    # in the middle of the sorted list. This will decrease the sorting 
    # time of the list
    pivot = sel.selection_sort(pivots)[1]

    point = 0

    # Select the index the chosen pivot corressponds to
    if liste[sta] == pivot:
        point = sta
    elif liste[sta+l//2] == pivot:
        point = sta+l//2
    else:  # liste[l-1] == pivot
        point = end-1

    # Get the pivot out of the way, to the first index
    util.swap(liste, sta, point)

    left, right = sta+1, end-1

    # Start with pointers to left and right. Increase the left pointer 
    # and decrease the right pointer until left points to an element
    # greater than pivot, and right points to an element less than pivot.
    # Then swap these elements. Repeat this process until right and left
    # meets.
    while True:
        while left < end and liste[left] <= pivot:
            left += 1

        while right > sta and liste[right] >= pivot:
            right -= 1

        if right <= left:
            break
        else:
            util.swap(liste, left, right)

    util.swap(liste, sta, right)
    # After this swap, at the right index our pivot resides. to the right 
    # of the pivot, the elements are less than or equal to the pivot. To
    # the right of the pivot the elements are greater than or equal to the 
    # pivot


    # Quicksort the left and right sides
    quicksort(liste, sta, right)
    quicksort(liste, right+1, end)


if __name__ == "__main__":
    # liste = []

    # util.fill_rand(liste, 10, 100)

    # print("liste is:", liste)
    # print("sum is:", sum(liste))
    # print("sum of an empty list is:", sum([]))

    # print("max of liste is:", find_max(liste))
    # print("max of empty list is:", find_max([]))
    # print("max of [5] is: ", find_max([5]))

    liste = []

    util.fill_rand(liste,3,100)

    print("liste is:", liste)
    quicksort(liste, 0, len(liste))
    print("sorted liste is:", liste)
