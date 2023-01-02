"""Josephus problem: n people stand in a circle and are eliminated in k steps."""
from structures.linked_list import CircularSinglyLinkedList
from structures.queue import Queue

def josephus(n:int, k:int):
    """Returns the last person standing in the circle."""
    people = CircularSinglyLinkedList()
    stages = Queue()
    for i in range(1, n + 1):
        people.insert(i)
    current = people.head
    while current.next != current:
        stages.enqueue(people)
        for _ in range(k - 1):
            current = current.next
        current.next = current.next.next
        current = current.next
    stages.enqueue(people)
    return current.data, stages
