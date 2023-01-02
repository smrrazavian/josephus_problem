"""Queue data structure."""

class Queue:
    """Queue class."""

    def __init__(self):
        """Initialize queue."""
        self.queue = []

    def enqueue(self, item):
        """Add item to queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove item from queue."""
        return self.queue.pop(0)

    def is_empty(self):
        """Check if queue is empty."""
        return self.queue == []

    def size(self):
        """Return size of queue."""
        return len(self.queue)

    def __str__(self):
        """Return string representation of queue."""
        return str(self.queue)
