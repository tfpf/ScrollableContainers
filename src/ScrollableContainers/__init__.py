import contextlib
import importlib

with contextlib.suppress(ImportError):
    from ScrollableContainers.Qt5 import ScrollableAreaQt5
with contextlib.suppress(ImportError):
    from ScrollableContainers.Qt6 import ScrollableAreaQt6
with contextlib.suppress(ImportError):
    from ScrollableContainers.Tk import ScrollableFrameTk
with contextlib.suppress(ImportError):
    from ScrollableContainers.Wx import ScrollablePanelWx
