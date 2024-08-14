#! /usr/bin/env python3

import itertools
import tkinter as tk
from tkinter import ttk

from ScrollableContainers import ScrollableFrameTk


class ExamplesScrollableFrameTk:
    def __init__(self):
        self.grid_of_widgets(tk.Tk())
        self.single_widget(tk.Toplevel())

    def grid_of_widgets(self, window):
        window.title("`ScrollableFrameTk` Demo")

        # Create a scrollable frame.
        scrollable_frame = ScrollableFrameTk(window)

        # Add widgets to the ``frame`` attribute of the scrollable frame, not
        # to the scrollable frame itself.
        dim = 10
        for i, j in itertools.product(range(dim), repeat=2):
            label = ttk.Label(scrollable_frame.frame, text=f"Label\n({i}, {j})")
            label.grid(row=i, column=j, padx=10, pady=10)

        scrollable_frame.pack(expand=True, fill=tk.BOTH)

    def single_widget(self, window):
        window.geometry("600x200+50+50")
        window.title("`ScrollableFrameTk` Demo")

        scrollable_frame = ScrollableFrameTk(window)

        label = ttk.Label(scrollable_frame.frame, text="big window, small label")
        label.pack()

        scrollable_frame.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    examples = ExamplesScrollableFrameTk()
    tk.mainloop()
