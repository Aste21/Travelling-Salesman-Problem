from classes import *

graph = Graph()

while graph.size < 9:
    graph.add_node()

# 80% code - comment it out if 100% is needed

eighty_percent_of_edges = 0.8 * graph.number_of_edges
while graph.number_of_edges > eighty_percent_of_edges:
    graph.delete_random_edge()

graph.print_nodes()

starting_node = int(input("\nWhat do you want the starting node to be: "))
s_node = int(input("What do you want the start node in bidirectional search to be: "))
e_node = int(input("What do you want the end node in bidirectional search to be: "))


if graph.does_hamiltonian_cycle_exist():
    print("BFS:")
    graph.bfs(starting_node)
    print("\nDFS:")
    graph.dfs(starting_node)
    print("\nMinimum spanning tree:")
    graph.minimum_spanning_tree(starting_node)
    print("\nGreedy search:")
    graph.greedy_search(starting_node)
else:
    print("\nRoute is impossible! - There is no hamiltonian cycle.")
if graph.is_route_possible(s_node, e_node):
    print("\nBidirectional search:")
    graph.bidirectional_search(s_node, e_node)
else:
    print("Bidirectional search is impossible! - starting or ending node has no edges")
