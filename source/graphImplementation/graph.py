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
        """
        adds child to person, adds child to person`s spouse (if is not None)
        adds parents to this person
        """
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
        """
        if parent in None adds parent to this person
        adds this person as child to parent and his spouse (if is not None)
        """
        if self.__father is None and parent.__gender == "male":
            parent.add_child(self)
        if self.__mother is None and parent.__gender == "female":
            parent.add_child(self)

    def add_spouse(self, spouse):
        """
        adds spouse to person, adds new parent to children
        adds children to spouse
        """
        if self.__spouse is None:
            self.__spouse = spouse
            self.__spouse.__spouse = self
            if spouse.__gender == "male":
                for i in self.__children:
                    i.__father = spouse
            else:
                for i in self.__children:
                    i.__mother = spouse
            self.__spouse.__children = self.__children


class Graph(object):

    def __init__(self, root):
        self.__root = root


