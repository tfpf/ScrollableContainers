#! /usr/bin/python3 -B

import itertools
import platform
import tkinter as tk
import tkinter.ttk as ttk

__all__ = ['ScrollableFrame']

###############################################################################

class ScrollableFrame(ttk.Frame):
    '''
Container with horizontal and vertical scrolling capabilities. Widgets must be
added to its `frame` attribute.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Scrollable canvas. This is the widget which actually manages
        # scrolling. Using the grid geometry manager ensures that the
        # horizontal and vertical scrollbars do not meet.
        self._canvas = tk.Canvas(self)
        self._canvas.bind_all('<Button-4>', self._on_mouse_scroll)
        self._canvas.bind_all('<Button-5>', self._on_mouse_scroll)
        self._canvas.bind_all('<MouseWheel>', self._on_mouse_scroll)
        self._canvas.bind('<Configure>', self._on_canvas_configure)
        self._canvas.grid(row=0, column=0, sticky=tk.NSEW)

        xscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self._canvas.xview)
        xscrollbar.grid(row=1, column=0, sticky=tk.EW)
        yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self._canvas.yview)
        yscrollbar.grid(row=0, column=1, sticky=tk.NS)
        self._canvas.configure(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = ttk.Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)
        self._on_frame_configure_id = self.frame.bind('<Configure>', self._on_frame_configure)

        # Initially, the vertical scrollbar is a hair below its topmost
        # position. Move it to said position. No harm in doing the equivalent
        # for the horizontal scrollbar.
        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

    ###########################################################################

    def _on_canvas_configure(self, event):
        '''
Called when the canvas is resized. If the canvas is wider than the frame it
contains, move the frame to the top centre. Otherwise, move it to the top left.

:param event: Configure event.
        '''

        (width, height) = (self.frame.winfo_width(), self.frame.winfo_height())
        x = (event.width - width) // 2
        if x < 0:
            self._canvas.coords(self._window, (0, 0))
            bbox = (0, 0, width, height)
        else:
            self._canvas.coords(self._window, (x, 0))
            bbox = (0, 0, event.width, height)
        self._canvas.configure(scrollregion=bbox)

    ###########################################################################

    def _on_frame_configure(self, event=None):
        '''
Called when the canvas is resized or scrolled. Set the scrollable region, and
then disable this callback, so that it does not interfere with the other
callback.

:param event: Configure event.
        '''

        bbox = self._canvas.bbox(tk.ALL)
        self._canvas.configure(scrollregion=bbox)
        self.frame.unbind('<Configure>', self._on_frame_configure_id)

    ###########################################################################

    def _on_mouse_scroll(self, event):
        '''
Handle mouse scroll events.

:param event: Scroll event.
        '''

        # If we are viewing the top of the container, we shouldn't be able to
        # scroll up. However, if the container has some empty space at the
        # bottom, scrolling up still works. Prevent that from happening by
        # checking the current view before changing it.
        topmost = self._canvas.yview()[0] == 0
        system = platform.system()
        if system == 'Linux':
            if event.num == 4 and not topmost:
                self._canvas.yview_scroll(-1, tk.UNITS)
            elif event.num == 5:
                self._canvas.yview_scroll(1, tk.UNITS)
        elif system == 'Darwin' and (event.delta <= 0 or event.delta > 0 and not topmost):
            self._canvas.yview_scroll(int(-1 * event.delta), tk.UNITS)
        elif system == 'Windows' and (event.delta <= 0 or event.delta > 0 and not topmost):
            self._canvas.yview_scroll(int(-1 * event.delta / 120), tk.UNITS)

###############################################################################

def main():
    '''
Demonstrate how to use a scrollable frame.
    '''

    root = tk.Tk()
    root.title('`ScrollableFrame` Demo')

    # Create a scrollable frame.
    scrollable_frame = ScrollableFrame(root)

    # Add widgets to the `frame` attribute of the scrollable frame, not to the
    # scrollable frame itself.
    dim = 10
    for (i, j) in itertools.product(range(dim), range(dim)):
        ttk.Label(scrollable_frame.frame, text=f'Label\n({i}, {j})').grid(row=i, column=j, padx=10, pady=10)

    scrollable_frame.pack(expand=True, fill=tk.BOTH)
    root.mainloop()

###############################################################################

if __name__ == '__main__':
    main()
