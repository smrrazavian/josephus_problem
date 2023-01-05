"""Josephus problem: n people stand in a circle and are eliminated in k steps."""
from structures.linked_list import CircularSinglyLinkedList
from structures.queue import Queue


def josephus(n: int, k: int):
    """Returns the last person standing in the circle."""
    if k == 1:
        raise ValueError("k cannot be 1.")
    people = CircularSinglyLinkedList()
    stages = Queue()
    for person in range(1, n + 1):
        people.insert(person)
    current = people.head
    while current.next != current:
        stages.enqueue(people)
        for _ in range(k-2):
            current = current.next
        people.delete(current.next.data)
        current = current.next
        # people.display()

    
    for i in range(stages.size()):
        print("Stage", i+1)
        borna = stages.dequeue()
        borna.display()
    # return people

josephus(10, 2)
