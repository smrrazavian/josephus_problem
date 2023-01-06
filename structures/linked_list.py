"""Circular Singly Linked List implementation."""

class Node:
    """Node class."""
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    """Circular Singly Linked List class."""
    def __init__(self) -> None:
        self.head = None

    def insert(self, data: int) -> None:
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

    def delete(self, data: int) -> None:
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

    def display(self) -> None:
        """Displays the linked list."""
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            print(current.data, end=" ")
            current = current.next
            while current != self.head:
                print(current.data, end=" ")
                current = current.next
            print()
    
    def __str__(self) -> str:
        """Returns the string representation of the linked list."""
        if self.head is None:
            return "List is empty."
        else:
            current = self.head
            string = str(current.data)
            current = current.next
            while current != self.head:
                string += " " + str(current.data)
                current = current.next
            return string
    
    def __repr__(self) -> str:
        """Returns the string representation of the linked list."""
        return self.__str__()
    
    def __len__(self) -> int:
        """Returns the length of the linked list."""
        if self.head is None:
            return 0
        current = self.head
        count = 1
        current = current.next
        while current != self.head:
            count += 1
            current = current.next
        return count
