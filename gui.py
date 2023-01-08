"""GUI for the Josephus Problem and visualization of the circular linked list in every step."""
import math
import tkinter as tk
from josephus import josephus

class JosephusCanvas():
    """Canvas Class for the Josephus Problem."""
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.root = tk.Tk()
        self.root.title("Josephus Problem")
        self.root.geometry(f"{self.width}x{self.height + 200}")
        self.root.resizable(False, False)
        self.get_inputs().pack()
        self.canvas = tk.Canvas(self.root, width=self.width, height=self.height, bg="aliceblue")
        self.canvas.pack()
        self.root.mainloop()
    
    def get_inputs(self) -> tk.LabelFrame:
        """Gets the inputs from the user."""
        frame = tk.LabelFrame(self.root, text="Inputs", bg="aliceblue", foreground="teal")
        frame.grid()
        n_label = tk.Label(frame, text="Number of people: ", bg="aliceblue")
        n_label.grid(row=0, column=0)
        self.n_entry = tk.Entry(frame)
        self.n_entry.grid(row=0, column=1)
        k_label = tk.Label(frame, text="Elimination step: ", bg="aliceblue")
        k_label.grid(row=1, column=0)
        self.k_entry = tk.Entry(frame)
        self.k_entry.grid(row=1, column=1,)
        self.submit_button = tk.Button(frame, text="Submit", command=self.submit, fg="teal", bg="aliceblue")
        self.submit_button.grid(row=2, column=0, columnspan=2)
        self.reset_button = tk.Button(frame, text="Reset", command=self.reset, fg="teal", bg="aliceblue")
        self.reset_button.grid(row=3, column=0, columnspan=2)
        return frame
    
    def submit(self) -> None:
        """Submits the inputs and starts the visualization."""
        self.n_entry.config(state="disabled")
        self.k_entry.config(state="disabled")
        self.submit_button.config(state="disabled")
        self.n = int(self.n_entry.get())
        self.k = int(self.k_entry.get())
        self.stages = josephus(self.n, self.k)
        self.draw_table()
    
    def reset(self) -> None:
        """Resets the inputs."""
        self.n_entry.config(state="normal")
        self.k_entry.config(state="normal")
        self.submit_button.config(state="normal")
        self.canvas.delete("all")
        self.n_entry.delete(0, "end")
        self.k_entry.delete(0, "end")
    
    def draw_people(self, x: int, y: int, r: int, color: str, text: str) -> None:
        """Draws a circle on the canvas."""
        self.canvas.create_oval(x, y, x+r/2, y+r/2, fill="cadetblue")
        self.canvas.create_text(x+r/4, y+r/4, text=text, fill="black")
    
    def draw_table(self):
        """Draws the table on the canvas."""
        while self.stages.size() != 0:
            people = self.stages.dequeue()
            people_count = len(people)
            r = self.detect_r(people_count)[0]
            r_2 = self.detect_r(people_count)[2]
            theta = 2 * math.pi / people_count
            for i in range(people_count):
                x = self.width/2 +  r_2 * math.cos(i*theta) - r/2
                y = self.height/2 + r_2 * math.sin(i*theta) - r/2
                people_list = str(people).split(" ")
                person = people_list[i]
                self.draw_people(x, y, r, "SkyBlue3", person)
            self.root.update()
            time = self.detect_r(people_count)[1]
            self.root.after(time)
            if self.stages.size() != 0:
                self.canvas.delete("all")
        self.canvas.delete("all")
        self.canvas.create_oval(self.height/2-60, self.width/2-60, self.height/2+60, self.width/2+60, fill="gold")
        self.canvas.create_text(self.width/2, self.height/2, text=f"winner is {people}", fill="black")

    @staticmethod
    def detect_r(n:int) -> list:
        """Detects the radius of the circle."""
        if n <= 20:
            r = 100
            r_2 = 300
            time = 800
        elif n <= 50:
            r = 70
            r_2 = 350
            time = 1000
        else:
            r = 30
            r_2 = 325
            time = 2000
        metrics = [r, time, r_2]
        return metrics


if __name__ == "__main__":
    JosephusCanvas(800, 800)
