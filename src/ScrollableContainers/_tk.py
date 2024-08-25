__all__ = ["ScrollableFrameTk"]

import platform
import tkinter as tk
from tkinter import ttk

_system = platform.system()


class ScrollableFrameTk(ttk.Frame):
    """
    Container with horizontal and vertical scrolling capabilities. Widgets must
    be added to its ``frame`` attribute. Constructor arguments are passed to
    the parent constructor.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Using the grid geometry manager ensures that the horizontal and
        # vertical scrollbars do not touch.
        self._xscrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self._xview)
        self._xscrollbar.bind("<Enter>", self._on_scrollbar_enter)
        self._xscrollbar.bind("<Leave>", self._on_scrollbar_leave)
        self._xscrollbar.grid(row=1, column=0, sticky=tk.EW)
        self._yscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self._yview)
        self._yscrollbar.bind("<Enter>", self._on_scrollbar_enter)
        self._yscrollbar.bind("<Leave>", self._on_scrollbar_leave)
        self._yscrollbar.grid(row=0, column=1, sticky=tk.NS)
        self._hide_scrollbars_id = None

        # Scrollable canvas. This is the widget which actually manages
        # scrolling. Initially, it will be above the scrollbars, so the latter
        # won't be visible.
        self._canvas = tk.Canvas(self)
        self._canvas.bind("<Configure>", self._on_canvas_configure)
        self._canvas.bind("<Enter>", self._on_canvas_enter)
        self._canvas.bind("<Leave>", self._on_canvas_leave)
        self._canvas.configure(xscrollcommand=self._xscrollbar.set, yscrollcommand=self._yscrollbar.set)
        self._canvas.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=tk.NSEW)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame = ttk.Frame(self._canvas)
        self._window = self._canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)
        self.frame.bind("<Configure>", self._on_frame_configure)
        self._on_frame_expose_id = self.frame.bind("<Expose>", self._on_frame_expose)

        # Initially, the vertical scrollbar is a hair below its topmost
        # position. Move it to said position. No harm in doing the equivalent
        # for the horizontal scrollbar.
        self._canvas.xview_moveto(0.0)
        self._canvas.yview_moveto(0.0)

    def _show_scrollbars(self):
        """
        Move the horizontal and vertical scrollbars above the scrollable
        canvas, effectively showing them.
        """
        self._xscrollbar.lift()
        self._yscrollbar.lift()

    def _hide_scrollbars(self):
        """
        Move the horizontal and vertical scrollbars below the scrollable
        canvas, effectively hiding them.
        """
        self._xscrollbar.lower()
        self._yscrollbar.lower()

    def _on_scrollbar_enter(self, _event: tk.Event | None = None):
        """
        Called when the mouse pointer enters a scrollbar. Cancel the callback
        which will hide the scollbars.

        :param _event: Enter event.
        """
        if self._hide_scrollbars_id:
            self.after_cancel(self._hide_scrollbars_id)

    def _on_scrollbar_leave(self, _event: tk.Event | None = None, ms: int = 1000):
        """
        Called when the mouse pointer leaves a scrollbar. Hide the horizontal
        and vertical scrollbars afer a delay.

        :param _event: Leave event.
        :param ms: Delay in milliseconds.
        """
        self._hide_scrollbars_id = self.after(ms, self._hide_scrollbars)

    def _peek_scrollbars(self):
        """
        Show the horizontal and vertical scrollbars briefly.
        """
        # Pretend that the mouse pointer entered and left a scrollbar to avoid
        # code repetition.
        self._on_scrollbar_enter()
        self._show_scrollbars()
        self._on_scrollbar_leave()

    def _xview(self, *args, width: int | None = None):
        """
        Called when a horizontal scroll is requested. Called by other callbacks
        (``_on_canvas_configure`` and ``_on_frame_configure``) whenever it is
        necessary to horizontally realign the contents of the canvas. Scroll
        the view only if the contents are not completely visible. Otherwise,
        move the scrollbar to such a position that they are horizontally
        centred.

        :param args: Passed to ``tkinter.Canvas.xview``.
        :param width: Width of the canvas.
        """
        if self._canvas.xview() != (0.0, 1.0):
            self._canvas.xview(*args)
        else:
            width = width or self._canvas.winfo_width()

            # To move the contents of the canvas to the centre, I call this
            # function with a negative argument. I don't know if this hack is
            # supported (because the Tcl/Tk manual pages say that it must be a
            # fraction between 0 and 1), but it works!
            self._canvas.xview_moveto((1 - width / self.frame.winfo_width()) / 2)

    def _yview(self, *args):
        """
        Called when a vertical scroll is requested. Scroll the view only if the
        contents are not completely visible.

        :param args: Passed to ``tkinter.Canvas.yview``.
        """
        if self._canvas.yview() != (0.0, 1.0):
            self._canvas.yview(*args)

    def _on_canvas_configure(self, event: tk.Event):
        """
        Called when the canvas is resized. Update the scrollable region.

        :param event: Configure event.
        """
        self._canvas.configure(scrollregion=self._canvas.bbox(tk.ALL))
        self._xview(tk.SCROLL, 0, tk.UNITS, width=event.width)

    def _on_frame_configure(self, _event: tk.Event | None = None):
        """
        Called when the frame is resized or the canvas is scrolled. Update the
        scrollable region.

        This method is necessary to handle updates which may occur after the
        GUI loop has started.

        :param _event: Configure event.
        """
        self._canvas.configure(scrollregion=self._canvas.bbox(tk.ALL))
        self._xview(tk.SCROLL, 0, tk.UNITS)

    def _on_frame_expose(self, _event: tk.Event | None = None):
        """
        Called when the frame becomes visible. Call ``_on_frame_configure`` and
        then disable this callback.

        This method is necessary because if a scrollable frame is put into,
        say, a notebook (as opposed to a toplevel window), and the canvas is
        wider than its contents, then (on Linux) the contents are not initially
        horizontally centred. (This issue is not observed on Windows, probably
        because its frame configure events work differently.) Hence, I try to
        centre the contents again upon an expose event.

        :param _event: Expose event.
        """
        self._on_frame_configure()
        self.frame.unbind("<Expose>", self._on_frame_expose_id)

    def _on_canvas_enter(self, _event: tk.Event | None = None):
        """
        Called when the mouse pointer enters the canvas. Set up vertical
        scrolling with the mouse wheel.

        :param _event: Enter event.
        """
        self.bind_all("<Button-4>", self._on_mouse_scroll)
        self.bind_all("<Button-5>", self._on_mouse_scroll)
        self.bind_all("<MouseWheel>", self._on_mouse_scroll)
        self._peek_scrollbars()

    def _on_canvas_leave(self, _event: tk.Event | None = None):
        """
        Called when the mouse pointer leaves the canvas. Unset vertical
        scrolling with the mouse wheel.

        :param _event: Leave event.
        """
        self.unbind_all("<Button-4>")
        self.unbind_all("<Button-5>")
        self.unbind_all("<MouseWheel>")

    def _on_mouse_scroll(self, event: tk.Event):
        """
        Called when the mouse wheel is scrolled or a two-finger swipe gesture
        is performed on the touchpad. Ask to scroll the view horizontally if
        the mouse wheel is scrolled with Shift held down (equivalent to a
        horizontal two-finger swipe) and vertically otherwise (equivalent to a
        vertical two-finger swipe).

        :param event: Scroll event.
        """
        # Select which method to call based on whether Shift was held down.
        # This is indicated by the LSB of the state.
        callee = self._xview if event.state & 1 else self._yview
        match _system:
            case "Linux" if event.num == 4:
                callee(tk.SCROLL, -1, tk.UNITS)
            case "Linux" if event.num == 5:
                callee(tk.SCROLL, 1, tk.UNITS)
            case "Darwin":
                callee(tk.SCROLL, -event.delta, tk.UNITS)
            case "Windows":
                callee(tk.SCROLL, -event.delta // 120, tk.UNITS)
            case _:
                message = f"event {event.num} on OS {_system!r} is not supported"
                raise ValueError(message)
        self._peek_scrollbars()
