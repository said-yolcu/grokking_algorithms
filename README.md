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

Complexity: <br />
Best, Average -> O(n*log(n)) <br />
Worst -> O(n^2)

## Hash Tables

Hash tables are created via combining a hash function with an array. Below table shows the average and worst-case complexities of different operations on hash tables. Best-case complexities are similar to the average-case.

| | Average | Worst |
| --- | --- | --- |
| **Search** | O(1) | O(n) |
| **Insert** | O(1) | O(n) |
| **Delete** | O(1) | O(n) |

## Breadth-First Search

In breadth-first search we start by visiting a node. We enqueue its neighbor nodes to a visiting queue. After we finish visiting this node, we dequeue a node from the queue and repeat the actions above for this node. We repeat this process until no node is left in the queue.

It can be said that breadth-first search divides a graph into levels and it visits nodes level by level.

Given a graph with V number of vertices (nodes) and E number of edges. Running time of breadth-first search is O(V + E).