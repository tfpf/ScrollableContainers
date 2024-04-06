import contextlib
import importlib

with contextlib.suppress(ImportError):
    from ScrollableContainers._qt5 import ScrollableAreaQt5
with contextlib.suppress(ImportError):
    from ScrollableContainers._qt6 import ScrollableAreaQt6
with contextlib.suppress(ImportError):
    from ScrollableContainers._tk import ScrollableFrameTk
with contextlib.suppress(ImportError):
    from ScrollableContainers._wx import ScrollablePanelWx
