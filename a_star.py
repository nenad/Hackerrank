__author__ = 'Nenad'



class Edge:
    node_1 = None
    node_2 = None
    distance = 0

    def __init__(self, node_1, node_2, distance):
        self.node_1 = node_1
        self.node_2 = node_2
        self.distance = distance

    def has_nodes(self, node_1, node_2):
        if (self.node_1 == node_1 and self.node_2 == node_2) or (self.node_1 == node_2 and self.node_2 == node_1):
            return True
        return False

class Node:
    x = 0
    y = 0
    name = ""
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def euclidean_distance(self, to_node):
        import math
        return math.sqrt((to_node.y - self.y) ** 2 + (to_node.x - self.x) ** 2)

    def __unicode__(self):
        return "{0} at ({1}, {2})".format(self.name, self.x, self.y)

    def __repr__(self):
        return "{0} at ({1}, {2})".format(self.name, self.x, self.y)

def get_all_nodes(edges):
    nodes = set()
    for edge in edges:
        nodes.add(edge.node_1)
        nodes.add(edge.node_2)

    return nodes

def get_neighbors(node, edges):
    neighbors = set()
    for edge in edges:
        if edge.node_1 == node:
            neighbors.add(edge.node_2)
        if edge.node_2 == node:
            neighbors.add(edge.node_1)
    return neighbors

def get_distance(node_1, node_2, edges):
    for edge in edges:
        if edge.has_nodes(node_1, node_2):
            return edge.distance
    return 0

# data added
tetovo = Node(1, 1, "Tetovo")
skopje = Node(1, 4, "Skopje")
debar = Node(0, 3, "Debar")
ohrid = Node(5, 1, "Ohrid")
struga = Node(5, 2, "Struga")
veles = Node(3, 5, "Veles")
bitola = Node(5, 5, "Bitola")
gevgelija = Node(5, 8, "Gevgelija")
pehcevo = Node(1, 8, "Pehcevo")
kicevo = Node(3, 1, "Kicevo")
kumanovo = Node(0, 6, "Kumanovo")

edges = []
edges.append(Edge(tetovo, skopje, 50))
edges.append(Edge(tetovo, kicevo, 60))
edges.append(Edge(tetovo, debar, 50))

edges.append(Edge(skopje, kumanovo, 45))
edges.append(Edge(skopje, veles, 60))

edges.append(Edge(veles, bitola, 80))
edges.append(Edge(veles, pehcevo, 45))
edges.append(Edge(veles, gevgelija, 90))

edges.append(Edge(kumanovo, pehcevo, 100))

edges.append(Edge(kicevo, ohrid, 70))
edges.append(Edge(kicevo, struga, 50))

edges.append(Edge(ohrid, struga, 10))
edges.append(Edge(debar, ohrid, 90))


def shortest_distance(start, end, edges):
    closed_set = []
    open_set = [start]
    came_from = {}

    all_nodes = get_all_nodes(edges)

    g_score = {}
    f_score = {}

    for node in all_nodes:
        g_score[node] = 999999
        f_score[node] = 999999

    heuristic_start_end = start.euclidean_distance(end)

    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic_start_end

    while len(open_set) != 0:
        current = None
        lowest = 999999.0

        # calculate f function to all nodes in the open list, pick the lowest one
        for node in open_set:
            f = f_score[node]
            # print "Node: {0} g_score = {1}, f_score = {2}".format(node, g_score[node], f_score[node])
            if f < lowest:
                current = node
                lowest = f

        # print "Current node: {0} g_score = {1}, f_score = {2}".format(current, g_score[current], f_score[current])

        # if we have the end node, return the path
        if current == end:
            return find_path(came_from, current)

        # remove the node from the open set, put it in the closed set
        open_set.remove(current)
        closed_set.append(current)

        neighbors = get_neighbors(current, edges)
        for n in neighbors:
            if n in closed_set:
                continue
            tentative_g_score = g_score[current] + get_distance(current, n, edges)

            if n not in open_set or tentative_g_score < g_score[n]:
                came_from[n] = current
                g_score[n] = tentative_g_score
                f_score[n] = g_score[n] + n.euclidean_distance(end)
                if n not in open_set:
                    open_set.append(n)
    return []


def find_path(path_nodes, current):

    total_path = []

    total_path.insert(0, current)
    while current in path_nodes:
        current = path_nodes[current]
        total_path.insert(0, current)

    return total_path

def calculate_total_distance(path):
    if len(path) <= 1:
        return 0

    total_distance = 0
    for i in range(0, len(path) - 1):
        node_1 = path[i]
        node_2 = path[i+1]
        total_distance += get_distance(node_1, node_2, edges)
    return total_distance

shortest = shortest_distance(tetovo, skopje, edges)
for node in shortest:
    print "{0} -> ".format(node.name),

print "End"
print calculate_total_distance(shortest)
