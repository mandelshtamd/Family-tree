class Data:
    def __init__(self):
        """Data constructor"""


class Node(object):
    def __init__(self, parent=None, data=None):
        self.parent = parent
        self.children = []
        self.data = data


class Tree(object):
    def __init__(self, root=None):
        self.root = root
