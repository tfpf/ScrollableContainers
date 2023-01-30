# Scrollable containers which *just work*:tm:!

If you have developed GUI applications, you probably know the pain of designing a clean front-end only to find that
your application window is too large for your client's screen. Making the content scrollable is not straightforward (at
least in Tkinter). Especially not after you have already written a lot of code to draw the content.

You can use `ScrollableContainers` to reduce headaches. Run the following commands to install the package.

```shell
git clone https://github.com/tfpf/ScrollableContainers.git
cd ScrollableContainers
pip install .
```

## `ScrollableFrameTk`
A full implementation of a scrollable frame in Tkinter.
* Handles resize events correctly.
* Horizontally centres the contents if the window is wider.
* Supports scrolling with the mouse wheel and touchpad.
  * Scrolling the mouse or swiping vertically with two fingers on the touchpad triggers a vertical scroll.
  * Scrolling the mouse while holding down Shift or swiping horizontally with two fingers on the touchpad triggers a
    horizontal scroll.

### Usage
Add widgets to the `frame` attribute of a `ScrollableFrameTk` object. See
[`examples/examples_ScrollableFrameTk.py`](examples/examples_ScrollableFrameTk.py).

### Notes
`'<Button-4>'`, `'<Button-5>'` and `'<MouseWheel>'` are bound to all widgets using `bind_all` to handle mouse wheel
scroll events. Do not `unbind_all` (or `bind_all` another function to) these three sequences!

## `ScrollablePanelWx`
A thin wrapper around `wx.lib.scrolledpanel.ScrolledPanel`.
* Does everything the aforementioned class does.
* Horizontally centres the contents if the window is wider.

### Usage
Add widgets to the `panel` attribute of a `ScrollablePanelWx` object. See
[`examples/examples_ScrollablePanelWx.py`](examples/examples_ScrollablePanelWx.py).
