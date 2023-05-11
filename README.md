# Travelling-Salesman-Problem
Program solving travelling salesman problem using a few different algorithms.

It creates a set of cities as points with coordinates x, y on a plane. The cost of going from city A to city B is equal to the Euclidean distance between two cities, if there exists a road.

There are 2 scenarios defined:

1. One with all the direct connections
2. Second one with 80% of possible roads.

The randomly generated map is represented as a weighted graph where cities are the nodes and roads are the edges of the graph.

In the created scene the travelling salesman problem is solved (the salesman starts from a randomly chosen city and has to visit each city exactly obce) in 4 different ways:

1. Full search of tree using breadth-first search method.
2. Full search of tree using deapth-first search method.
3. Approximation of the solution using Minimum Spanning Tree.
4. Approximation of the solution using greedy search.

At the end the shortest path between 2 chosen cities is found using bidirectional search.

In the 80% scenario, MST and greedy search sometimes doesn't work as they are designed to work in the 100% scenario.
