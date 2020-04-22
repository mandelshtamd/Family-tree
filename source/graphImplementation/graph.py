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

    def get_children(self):
        return self.__children

    def get_father(self):
        return self.__father

    def get_mother(self):
        return self.__mother

    def get_spouse(self):
        return self.__spouse

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

    def get_person(self, name):
        """
        looking for a person by name and returns Node with him
        """
        for i in self.__children:
            if i.get_name == name:
                return i
            if i.get_person(name).get_name == name:
                return i.get_person(name)
        return None


class Graph(object):

    def __init__(self, root):
        self.__root = root

    def get_root(self):
        return self.__root

    def get_person(self, name):
        """
        looks for a person by name and returns Node with him
        """
        for i in self.__root.get_children():
            if i.get_name() == name:
                return i
        return None

    def add_child(self, name_to_whom, child):
        person = self.get_person(name_to_whom)
        person.add_child(child)

    def add_parent(self, name_to_whom, parent):
        person = self.get_person(name_to_whom)
        person.add_parent(parent)

    def add_spouse(self, name_to_whom, spouse):
        person = self.get_person(name_to_whom)
        person.add_spouse(spouse)
