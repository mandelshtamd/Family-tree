class Node(object):

    def __init__(self, gender, name, father=None, mother=None, spouse=None):
        """
        initializes a node object
        gender, name are required
        gender = "male" or "female"
        father, mother, spouse are not required
        """
        self.__gender = gender
        self.__name = name
        self.__father = father
        self.__mother = mother
        self.__spouse = spouse
        self.__children = []

    def get_gender(self):
        return self.__gender

    def get_name(self):
        return self.__name

    def change_name(self, name):
        self.__name = name

    def add_child(self, child):
        if self.__gender == "male":
            self.__children.append(child)
            child.__father = self
            if self.__spouse is not None:
                self.__spouse.__children.append(child)
                child.__mother = self.__spouse

        if self.__gender == "female":
            self.__children.append(child)
            child.__mother = self
            if self.__spouse is not None:
                self.__spouse.__children.append(child)
                child.__father = self.__spouse

    def add_parent(self, parent):
        if self.__father is None and parent.__gender == "male":
            parent.add_child(self)
        if self.__mother is None and parent.__gender == "female":
            parent.add_child(self)


class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict is None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
