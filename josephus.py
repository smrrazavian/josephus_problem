"""Josephus problem: n people stand in a circle and are eliminated in k steps."""
from structures.linked_list import CircularSinglyLinkedList
from structures.queue import Queue


def josephus(n: int, k: int):
    """Returns the last person standing in the circle."""
    people = CircularSinglyLinkedList()
    stages = Queue()
    for person in range(1, n + 1):
        people.insert(person)
    current = people.head
    current_person = current.data
    while current_person != current.next.data:
        stages.enqueue(people)
        for temp in range(1, k+1):
            people.delete(current_person + temp)
        current = current.next
        current_person = current.data
    people.display()
    stages.enqueue(people)
    # return people


josephus(10, 2)
