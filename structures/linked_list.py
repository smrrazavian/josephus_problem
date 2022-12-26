"""Circular Singly Linked List implementation."""

class Node:
    """Node class."""
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    """Circular Singly Linked List class."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Inserts a node in the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, data):
        """Deletes a node from the linked list."""
        if self.head is None:
            print("List is empty.")
        elif self.head.data == data:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            while current.next != self.head:
                if current.next.data == data:
                    current.next = current.next.next
                current = current.next

    def display(self):
        """Displays the linked list."""
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            while current.next != self.head:
                print(current.data, end=" ")
                current = current.next
            print(current.data)
    