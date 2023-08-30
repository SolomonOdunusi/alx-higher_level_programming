#!/usr/bin/python3
"""
Classes that define a singly linked list
private instance attribute: data
def data(self)
data setter def data(self, value)
private instance attribute: next_node
def next_node(self)
"""


class Node:
    """A class that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes Node with a data and next_node"""
        """Args: data (int): data of Node"""
        """next_node (Node): next_node of Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets the data of the node"""
        """Args: value (int): data of Node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Gets the next_node of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Sets the next_node of the node"""
        """Args: value (Node): next_node of Node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        """Initializes SinglyLinkedList with a head"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position"""
        """Args: value (int): data of Node"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None:
                if current.next_node.data > value:
                    break
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns the string of linked list"""
        current = self.__head
        string = ""
        while current is not None:
            string += str(current.data) + "\n"
            current = current.next_node
        return (string[:-1])
