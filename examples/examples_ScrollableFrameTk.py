#! /usr/bin/python3 -B

import itertools
import tkinter as tk
import tkinter.ttk as ttk

from ScrollableContainers.Tk import ScrollableFrameTk

###############################################################################

def grid_of_widgets():
    root = tk.Tk()
    root.title('`ScrollableFrameTk` Demo')

    # Create a scrollable frame.
    scrollable_frame = ScrollableFrameTk(root)

    # Add widgets to the `frame` attribute of the scrollable frame, not to the
    # scrollable frame itself.
    dim = 10
    for (i, j) in itertools.product(range(dim), range(dim)):
        tk.Label(scrollable_frame.frame, text=f'Label\n({i}, {j})').grid(row=i, column=j, padx=10, pady=10)

    scrollable_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

###############################################################################

def single_widget():
    root = tk.Tk()
    root.geometry('600x200+50+50')
    root.title('`ScrollableFrameTk` Demo')

    scrollable_frame = ScrollableFrameTk(root)

    tk.Label(scrollable_frame.frame, text='big window, small label').pack()

    scrollable_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

###############################################################################

def entry_form_multiple():
    root = tk.Tk()
    root.title('`ScrollableFrameTk` Demo')

    labels = ('Name', 'Age', 'City', 'PIN', 'Occupation', 'Company', 'Profession')

    leftframe = ScrollableFrameTk(root)
    for (i, label) in enumerate(labels):
        tk.Label(leftframe.frame, text=label).grid(row=i, column=0, padx=10, pady=15)
        tk.Entry(leftframe.frame).grid(row=i, column=1, padx=10, pady=15)

    rightframe = ScrollableFrameTk(root)
    for (i, label) in enumerate(reversed(labels)):
        tk.Label(rightframe.frame, text=label).grid(row=i, column=0, padx=10, pady=15)
        tk.Entry(rightframe.frame).grid(row=i, column=1, padx=10, pady=15)

    leftframe.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
    rightframe.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT)
    root.mainloop()

###############################################################################

if __name__ == '__main__':
    grid_of_widgets()
    single_widget()
    entry_form_multiple()
