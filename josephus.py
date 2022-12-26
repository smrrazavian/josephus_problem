"""Josephus problem: n people stand in a circle and are eliminated in k steps."""
from structures.linked_list import CircularSinglyLinkedList


def josephus(n:int, k:int):
    """Returns the last person standing in the circle."""
    people = CircularSinglyLinkedList()
    for i in range(1, n + 1):
        people.insert(i)
    current = people.head
    while current.next != current:
        for _ in range(k - 1):
            current = current.next
        current.next = current.next.next
        current = current.next
    return current.data

if __name__ == "__main__":
    print(josephus(41, 3))