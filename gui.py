"""GUI for the Josephus Problem and visualization of the circular linked list in every step."""
from tkinter import *
# from structures.linked_list import CircularSinglyLinkedList
# from structures.queue import Queue
# from josephus_problem.logics.josephus import josephus


class JosephusGUI:
    """GUI for the Josephus Problem."""
    def __init__(self):
        self.root = Tk()
        self.root.title("Josephus Problem")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="white")
        # self.root.iconbitmap("josephus_problem/gui/josephus.ico")
        # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        # self.create_widgets()
        # self.root.mainloop()



if __name__ == "__main__":
    JosephusGUI()
