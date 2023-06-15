# grokking_algorithms

In this repo, I am tracking my progress reading **Grokking Algorithms** book. This is an elementary book introducing algorithms. I highly recommend you to check that out if you are new to algorithms, or you want to refresh your knowledge.

## Selection Sort

Iterate the list to find the maximum element and put this element to the end of the list. Repeat this process for the first n-1 elements, n-2 elements (n is the length of the list) and so on.

Complexity -> O(n^2)

## Divide and Conquer

Divide and Conquer is a method of creating an algorithm for a given problem. It does not give a reasonable solution to every kind of problem.

1. Figure out a simple case as the base case.
2. Figure out how to reduce the problem to the base case.

## Quicksort

Quicksort is an divide-and-conquer algorithm. It selects a pivot and divides the list into two: the elements less than or equal to pivot are to the left of the pivot, and elements greater than or equal to the pivot are to the right of the pivot. It repeats this process to the left and right sublists until the whole list is sorted.

Complexity:
Best, Average -> O(n*log(n))
Worst -> O(n^2)


