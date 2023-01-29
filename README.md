# Scrollable Frame for Tkinter
A scrollable frame which just works:tm:!

If you have developed GUI applications, you probably know the pain of designing a clean front-end only to find that
your application window is too large for your client's screen. Making the content scrollable is not straightforward, at
least in Tkinter. Especially not after you have already written a lot of code to draw the content.

You can use `ScrollableFrameTk` to reduce headaches. It automatically handles horizontal and vertical scrolling, and
doesn't break when the window is resized. If the window is wider than its contents, the latter will be horizontally
centred. Also, scrolling the mouse wheel vertically scrolls the window.

This project is not connected with [the `ScrollableFrame` PyPI package](https://pypi.org/project/ScrollableFrame/).

### TL;DR
Add widgets to the `frame` attribute of a `ScrollableFrameTk` object.
```python
import tkinter as tk

from ScrollableFrame.Tk import ScrollableFrameTk

root = tk.Tk()
scrollable_frame = ScrollableFrameTk(root)
for _ in range(100):
    tk.Label(scrollable_frame.frame, text='Label ' * 30).pack()

scrollable_frame.pack(expand=True, fill=tk.BOTH)
root.mainloop()
```

See also [`examples.py`](examples.py) for more.

`'<Button-4>'`, `'<Button-5>'` and `'<MouseWheel>'` are bound to all widgets using `bind_all` to handle mouse wheel
scroll events. Do not `unbind_all` (or `bind_all` another function to) these three sequences!
