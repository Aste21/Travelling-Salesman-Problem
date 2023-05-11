from copy import copy
from random import randint
from math import *


def does_array_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            return False
    return True


def distance_towns(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def edge_in_edges(edge, edges):
    for edg in edges:
        if edg.start == edge.start and edg.end == edge.end and edg.distance == edge.distance:
            return True
    return False


class Edge:
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Node:
    def __init__(self, x, y, nr):
        self.x = x
        self.y = y
        self.edges = []
        self.nr = nr

    def add_edge(self, start, end):
        self.edges.append(Edge(start.nr, end.nr, distance_towns(start.x, start.y, end.x, end.y)))

    def get_edge_number(self, start, end):
        for i in range(len(self.edges)):
            if self.edges[i].start == start and self.edges[i].end == end:
                return i


class Route:
    def __init__(self, route: list, route_nr: list, distance):
        self.route = route
        self.route_nr = route_nr
        self.distance = distance


class Graph:
    def __init__(self):
        self.list = []
        self.size = 0
        self.number_of_edges = 0

    def does_it_already_exist(self, x, y):
        for node in self.list:
            if x == node.x and y == node.y:
                return True
        return False

    def does_hamiltonian_cycle_exist(self):
        for node in self.list:
            if len(node.edges) < 2:
                return False
        return True

    def is_route_possible(self, start, end):
        if len(self.list[start].edges) == 0 or len(self.list[end].edges) == 0:
            return False
        return True

    def generate_edges(self, node_nr):
        for node in self.list:
            if node.x != self.list[node_nr].x or node.y != self.list[node_nr].y:
                self.list[node_nr].add_edge(self.list[node_nr], node)
                node.add_edge(node, self.list[node_nr])
                self.number_of_edges += 1

    def add_node(self):
        while True:
            x = randint(-100, 100)
            y = randint(-100, 100)
            if not self.does_it_already_exist(x, y):
                self.list.append(Node(x, y, self.size))
                self.size += 1
                self.generate_edges(self.size - 1)
                return [x, y]

    def find_route_length(self, route):
        distance = 0
        for i in range(len(route) - 1):
            node_1 = self.list[int(route[i])]
            node_2 = self.list[int(route[i + 1])]
            distance += distance_towns(node_1.x, node_1.y, node_2.x, node_2.y)
        return distance

    def delete_random_edge(self):
        node_nr = randint(0, self.size - 1)
        if len(self.list[node_nr].edges) == 0:
            return
        edge_nr = randint(0, len(self.list[node_nr].edges) - 1)
        end_node_nr = self.list[node_nr].edges[edge_nr].end
        end_edge_nr = self.list[end_node_nr].get_edge_number(end_node_nr, node_nr)
        self.list[node_nr].edges.remove(self.list[node_nr].edges[edge_nr])
        self.list[end_node_nr].edges.remove(self.list[end_node_nr].edges[end_edge_nr])
        self.number_of_edges -= 1

    def delete_edges(self, node_nr):
        for i in range(self.size):
            for edge in self.list[i].edges:
                if edge.start == node_nr or edge.end == node_nr:
                    self.list[i].edges.remove(edge)
                    self.number_of_edges -= 1

    def del_node(self):
        self.delete_edges(self.size - 1)
        self.list.remove(self.list[self.size - 1])
        self.size -= 1

    def print_nodes(self):
        if self.size == 0:
            print("Graph is empty.")
        else:
            for i in range(self.size):
                print(f"Node Number: {i}, Node x = {self.list[i].x},  Node y = {self.list[i].y}")
                for edge in self.list[i].edges:
                    print(
                        f"edge start: {edge.start},  edge end: {edge.end},  edge distance:  {round(edge.distance, 2)}")
                print("\n")

    def bfs(self, s):
        queue = []
        result = []
        queue.append(Route([self.list[s], ], [self.list[s].nr, ], 0))
        while len(queue) != 0:
            x = queue.pop(0)
            # print(x.route_nr)
            if len(self.list) == len(x.route):
                for edge in x.route[-1].edges:
                    if edge.end == self.list[s].nr:
                        result.append(Route(x.route + [self.list[s]], x.route_nr + [s], x.distance + edge.distance))
                        break
                x.route = []
            else:
                for edge in x.route[-1].edges:
                    if edge.end not in x.route_nr:
                        queue.append(
                            Route(x.route + [self.list[edge.end]], x.route_nr + [edge.end], x.distance + edge.distance))
        min_distance = 1000000
        min_route = []
        for route in result:
            if route.distance < min_distance:
                min_distance = route.distance
                min_route = route.route_nr
        for i in range(len(min_route)):
            min_route[i] = str(min_route[i])
        print(f"The best route is: {'->'.join(min_route)}\nIts length is {round(min_distance, 2)}")

    def dfs(self, s):
        queue = []
        result = []
        queue.append(Route([self.list[s], ], [self.list[s].nr, ], 0))
        while len(queue) != 0:
            x = queue.pop(-1)
            # print(x.route_nr)
            if len(self.list) == len(x.route):
                for edge in x.route[-1].edges:
                    if edge.end == self.list[s].nr:
                        result.append(Route(x.route + [self.list[s]], x.route_nr + [s], x.distance + edge.distance))
                        break
                x.route = []
            else:
                for edge in x.route[-1].edges:
                    if edge.end not in x.route_nr:
                        queue.append(
                            Route(x.route + [self.list[edge.end]], x.route_nr + [edge.end], x.distance + edge.distance))
        min_distance = 1000000
        min_route = []
        for route in result:
            if route.distance < min_distance:
                min_distance = route.distance
                min_route = route.route_nr
        for i in range(len(min_route)):
            min_route[i] = str(min_route[i])
        print(f"The best route is: {'->'.join(min_route)}\nIts length is {round(min_distance, 2)}")

    def minimum_spanning_tree(self, s):
        # prims algorithm -> dfs search
        min_tree = Graph()
        for i in range(len(self.list)):
            min_tree.list.append(Node(self.list[i].x, self.list[i].y, self.list[i].nr))
            min_tree.size += 1
        min_d = 100000
        min_e = -1
        for edge in self.list[s].edges:
            if edge.distance < min_d:
                min_d = edge.distance
                min_e = edge
        min_tree.list[s].edges.append(Edge(s, min_e.end, min_d))
        min_tree.list[min_e.end].edges.append(Edge(min_e.end, s, min_d))
        for i in range(len(min_tree.list) - 2):
            min_dist = 10000
            min_edge = -1
            for node in min_tree.list:
                if len(node.edges) > 0:
                    for edge in self.list[node.nr].edges:
                        if edge.distance < min_dist and not edge_in_edges(edge, min_tree.list[node.nr].edges):
                            if len(min_tree.list[edge.end].edges) == 0:
                                min_dist = edge.distance
                                min_edge = edge
            min_tree.list[min_edge.start].edges.append(Edge(min_edge.start, min_edge.end, min_edge.distance))
            min_tree.list[min_edge.end].edges.append(Edge(min_edge.end, min_edge.start, min_edge.distance))
        queue = [min_tree.list[s]]
        visited = [min_tree.list[s]]
        result = []
        while queue:
            x = queue.pop(-1)
            result.append(x)
            for edge in x.edges:
                if min_tree.list[edge.end] not in visited:
                    queue.append(min_tree.list[edge.end])
                    visited.append(min_tree.list[edge.end])
        result.append(min_tree.list[s])
        min_distance = 0
        for i in range(len(result) - 1):
            is_connected = False
            for edge in self.list[result[i].nr].edges:
                if edge.end == result[i + 1].nr:
                    min_distance += edge.distance
                    is_connected = True
                    break
            if not is_connected:
                print("Unable to calculate best route")
                return 0
        result_string = []
        for i in range(len(result)):
            result_string.append(str(result[i].nr))
        print(f"The best route is: {'->'.join(result_string)}\nIts length is {round(min_distance, 2)}")

    def greedy_search(self, s):
        route = [self.list[s]]
        distance = 0
        while len(route) != len(self.list):
            min_dist = 1000000
            min_edge = route[-1].edges[0]
            for edge in route[-1].edges:
                if edge.distance < min_dist and self.list[edge.end] not in route:
                    min_dist = edge.distance
                    min_edge = edge
            route.append(self.list[min_edge.end])
            distance += min_edge.distance
        is_end_connected = False
        for edge in route[-1].edges:
            if edge.end == s:
                route.append(self.list[s])
                distance += edge.distance
                is_end_connected = True
        if not is_end_connected:
            print("Unable to get a route using greedy search.")
            return 0
        for i in range(len(route)):
            route[i] = str(route[i].nr)
        print(f"The best route is: {'->'.join(route)}\nIts length is {round(distance, 2)}")

    def bidirectional_search(self, start, end):
        queue_s = [self.list[start]]
        queue_e = [self.list[end]]
        visited_s = [self.list[start]]
        visited_e = [self.list[end]]
        route_s = [[-1] for _ in range(len(self.list))]
        route_s[start] = [start]
        route_e = [[-1] * 1 for _ in range(len(self.list))]
        route_e[end] = [end]
        is_end = False
        connection_node = -1
        while (queue_s or queue_e) and not is_end:
            x = queue_s.pop()
            for edge in x.edges:
                if self.list[edge.end] not in visited_s:
                    queue_s.append(self.list[edge.end])
                    visited_s.append(self.list[edge.end])
                    route_s[edge.end] = copy(route_s[edge.start])
                    route_s[edge.end].append(edge.end)
            for node in visited_s:
                if node in visited_e:
                    is_end = True
                    connection_node = node
                    break
            if not is_end:
                x = queue_e.pop()
                for edge in x.edges:
                    if self.list[edge.end] not in visited_e:
                        queue_e.append(self.list[edge.end])
                        visited_e.append(self.list[edge.end])
                        route_e[edge.end] = copy(route_e[edge.start])
                        route_e[edge.end].append(edge.end)
                for node in visited_e:
                    if node in visited_s:
                        is_end = True
                        connection_node = node
                        break
        final_route = []
        for node_nr in route_s[connection_node.nr]:
            final_route.append(str(node_nr))
        for i in range(len(route_e[connection_node.nr]) - 2, -1, -1):
            final_route.append(str(route_e[connection_node.nr][i]))
        print(
            f"The shortest route between {start} and {end} is {'->'.join(final_route)} "
            f"and its length is {self.find_route_length(final_route)}")
