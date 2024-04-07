# Scrollable containers which *just work*!
If you have developed GUI applications, you probably know the pain of designing a clean front-end only to find that
your application window is too large for your client's screen. Making the content scrollable is not straightforward (at
least in Tkinter). Especially not after you have already written a lot of code to draw the content.

You can use `ScrollableContainers` to reduce headaches.
[It's available on PyPI!](https://pypi.org/project/ScrollableContainers/)

```shell
pip install ScrollableContainers
```

Scrollable containers are currently available for the following GUI toolkits.
* Tkinter
* wxPython
* PyQt5
* PyQt6

**This project is not sponsored or endorsed by, or connected with, any organisation or entity such as but not limited
to: the Tcl Core Team, the Python Software Foundation, the wxWidgets Team, the wxPython Team, the Qt Company and
Riverbank Computing.**

[![lint](https://github.com/tfpf/ScrollableContainers/actions/workflows/lint.yml/badge.svg)](https://github.com/tfpf/ScrollableContainers/actions/workflows/lint.yml)
[![install](https://github.com/tfpf/ScrollableContainers/actions/workflows/install.yml/badge.svg)](https://github.com/tfpf/ScrollableContainers/actions/workflows/install.yml)
[![build](https://github.com/tfpf/ScrollableContainers/actions/workflows/build.yml/badge.svg)](https://github.com/tfpf/ScrollableContainers/actions/workflows/build.yml)

# Tkinter
`ScrollableContainers.ScrollableFrameTk`: a comprehensive implementation of a scrollable frame, and the flagship class
of this project. (I wrote the other classes just for completeness.)

### Usage
Add widgets to the `frame` attribute of a `ScrollableFrameTk` object.
[See examples.](https://github.com/tfpf/ScrollableContainers/blob/main/examples/examples_ScrollableFrameTk.py)

### Features
* Handles resize events correctly.
* Supports scrolling with the mouse wheel and touchpad.
  * Scrolling the mouse wheel or swiping vertically with two fingers on the touchpad triggers a vertical scroll.
  * Scrolling the mouse wheel while holding down Shift or swiping horizontally with two fingers on the touchpad
    triggers a horizontal scroll.
* Horizontally centres the contents if the window is wider.

### Notes
`'<Button-4>'`, `'<Button-5>'` and `'<MouseWheel>'` are bound to all widgets using `bind_all` to handle mouse wheel
scroll events. Do not `unbind_all` (or `bind_all` another function to) these three sequences!

# wxPython
`ScrollableContainers.ScrollablePanelWx`: a thin wrapper around `wx.lib.scrolledpanel.ScrolledPanel`.

### Usage
Add widgets to the `panel` attribute of a `ScrollablePanelWx` object.
[See examples.](https://github.com/tfpf/ScrollableContainers/blob/main/examples/examples_ScrollablePanelWx.py)

### Features
* Does everything the wrapped class does.
* Horizontally centres the contents if the window is wider.

# PyQt5/PyQt6
`ScrollableContainers.ScrollableAreaQt5`/`ScrollableContainers.Qt6.ScrollableAreaQt6`: a thin wrapper around
`PyQt5.QtWidgets.QScrollArea`/`PyQt6.QtWidgets.QScrollArea`.

### Usage
Add widgets to the `area` attribute of a `ScrollableAreaQt5`/`ScrollableAreaQt6` object.
[See](https://github.com/tfpf/ScrollableContainers/blob/main/examples/examples_ScrollableAreaQt5.py)
[examples.](https://github.com/tfpf/ScrollableContainers/blob/main/examples/examples_ScrollableAreaQt6.py)

### Features
* Does everything the wrapped class does.
* Horizontally centres the contents if the window is wider.

---

In GTK, containers are widgets, so they can be aligned in other containers.

```Python
import itertools

import gi; gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)
window.set_default_size(256, 128)

scrolled_window = Gtk.ScrolledWindow()
window.add(scrolled_window)

grid = Gtk.Grid()
grid.set_halign(Gtk.Align.CENTER)
grid.set_row_spacing(20)
grid.set_column_spacing(20)
scrolled_window.add(grid)

dim = 10
for i, j in itertools.product(range(dim), repeat=2):
    label = Gtk.Label()
    label.set_label(f"Label\n({i}, {j})")
    grid.attach(label, j, i, 1, 1)

window.show_all()
Gtk.main()
```

Since horizontally centring the contents of a scrollable container is the primary function of this package, and GTK has
built-in functionality to achieve the same, no submodule for PyGObject is implemented here.
