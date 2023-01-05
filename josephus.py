"""Josephus problem: n people stand in a circle and are eliminated in k steps."""
import copy
from structures.linked_list import CircularSinglyLinkedList
from structures.queue import Queue


def make_copy(queue: Queue, linked_list: CircularSinglyLinkedList) -> None:
    """Makes a copy of the linked list and enqueues it in the queue."""
    temp = copy.deepcopy(linked_list)
    queue.enqueue(temp)


def josephus(n: int, k: int) -> Queue:
    """Returns the last person standing in the circle."""
    if k == 1:
        raise ValueError("k cannot be 1.")
    people = CircularSinglyLinkedList()
    stages = Queue()
    for person in range(1, n + 1):
        people.insert(person)
    make_copy(stages, people)
    current = people.head
    last_eliminated = 0
    while current.next != current:
        for _ in range(k-2):
            current = current.next
        eliminated = current.next.data
        people.delete(eliminated)
        current = current.next
        if eliminated < last_eliminated:
            make_copy(stages, people)
        last_eliminated = eliminated
    else:
        make_copy(stages, people)
    return stages
