"""GUI for the Josephus Problem and visualization of the circular linked list in every step."""
import math
import tkinter as tk
from josephus import josephus

class JosephusCanvas():
    """Canvas Class for the Josephus Problem."""
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Josephus Problem")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.get_inputs().pack()
        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.pack()
        self.root.mainloop()
    
    def get_inputs(self) -> tk.LabelFrame:
        """Gets the inputs from the user."""
        frame = tk.LabelFrame(self.root, text="Inputs")
        frame.grid()
        n_label = tk.Label(frame, text="Number of people: ")
        n_label.grid(row=0, column=0)
        self.n_entry = tk.Entry(frame)
        self.n_entry.grid(row=0, column=1)
        k_label = tk.Label(frame, text="Elimination step: ")
        k_label.grid(row=1, column=0)
        self.k_entry = tk.Entry(frame)
        self.k_entry.grid(row=1, column=1)
        self.submit_button = tk.Button(frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=2, column=0, columnspan=2)
        return frame
    
    def submit(self) -> None:
        """Submits the inputs and starts the visualization."""
        self.n_entry.config(state="disabled")
        self.k_entry.config(state="disabled")
        self.submit_button.destroy()
        self.n = int(self.n_entry.get())
        self.k = int(self.k_entry.get())
        self.stages = josephus(self.n, self.k)
        self.draw_table()
    
    def draw_people(self, x: int, y: int, r: int, color: str, text: str) -> None:
        """Draws a circle on the canvas."""
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill=color)
        self.canvas.create_text(x, y, text=text, fill="white")
    
    def draw_table(self):
        while self.stages.size() != 0:
            people = self.stages.dequeue()
            people_count = len(people)
            r = self.detect_r(people_count)
            theta = 2 * math.pi / people_count
            for i in range(people_count):
                x = r * math.cos(i*theta)
                y = r * math.sin(i*theta)
                people_list = str(people).split(" ")
                person = people_list[i]
                self.draw_people(x, y, r, "blue", person)

    @staticmethod
    def detect_r(n:int) -> int:
        if n <= 20:
            r = 50
        elif n <= 50:
            r = 25
        else:
            r = 15
        return r
            

if __name__ == "__main__":
    JosephusCanvas()