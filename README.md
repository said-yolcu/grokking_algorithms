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

Breadth-first search calculates shortest path for unweighted graphs.

In breadth-first search we start by visiting a node. We enqueue its neighbor nodes to a visiting queue. After we finish visiting this node, we dequeue a node from the queue and repeat the actions above for this node. We repeat this process until no node is left in the queue.

It can be said that breadth-first search divides a graph into levels and it visits nodes level by level.

Given a graph with V number of vertices (nodes) and E number of edges. Running time of breadth-first search is O(V + E).

## Dijkstra's Algorithm

Dijkstra's algorithm calculates the shortest path for a weighted graph. It can give erroneous results in negative weighted graphs.

Dijkstra's algo is comprised of 4 steps:

1. Start from the source node
2. Check whether the distance neighbor's of the current node to the source node is less if accessed via the current node
3. If so update their distances and add them to a queue
4. Pop the node with the smallest distance from the queue, and repeat steps 1 to 4
5. If there is nothing to pop (all nodes are processed), or you popped the destination node, end the algo.

In the algo, certain data structures are kept to record the distances of each node to source, parent of each node, whether a node is processed or not. Along the algo, this records are updated.

> Complexity of Dijkstra's algo is O(V^2) (V is the number of vertices/nodes) but with minimum priority queue, it drops down to O(V + E*log(V))

[Quotation Source](https://www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/tutorial/)

## Greedy Algorithm

Greedy algo is a type of algo that finds the global optimum via choosing local optima at each step. In other words, the solution for a problem is achieved by:

1. Dividing the problem into steps.
2. Choosing the best solution for each step one by one.
3. The global solution is the aggregation of subsolutions.

Most of the time, greedy algo is used to find a good-enough solution to complex problems. In such a situation the algo is called an approximation algo.

## Dynamic Programming

Dynamic programming is the art of building a solution for a problem out of solutions to subproblems. The algo can be divided into these steps:

1. Divide the problem into subproblems.
2. Find solutions to the most basic subproblems.
3. Find solutions to the encompassing subproblems, until the entire problem is solved.

For a problem to be solved by dynamic programming, two properties must be existent:

1. Overlapping Subproblems: The problem can be broken down into discrete subproblems, which are used many times during the solving of the problem. 
2. Optimal Substructure: The optimal solution to a  subproblem can be utilized to obtain the optimal solutions to the encompassing subproblems.

**Resources**:

- [1](https://www.educative.io/answers/what-is-dynamic-programming)
- [2](https://en.wikipedia.org/wiki/Overlapping_subproblems)

## K-Nearest Neighbors

K-nearest neighbors is an algo that is used in object classification and regression. The algo for classification can be summarized as follows:

1. Given a base set of objects, *extract features* (feature extraction is deciding on aspects of objects that can be used to classify them).
2. Put the base set of objects on a multidimensional graph, where each dimension represents a feature.
3. Given a new object, look at the k elements nearest to this object. The new object belongs to the class of elements that the relative majority of the elements belong.

Regression of a property can be performed via this algo by taking the average value of that property in k nearest neighbors.

