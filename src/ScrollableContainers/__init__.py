import contextlib as _contextlib
from importlib.metadata import version as _version

__version__ = _version("ScrollableContainers")

with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt5 import ScrollableAreaQt5
with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt6 import ScrollableAreaQt6
with _contextlib.suppress(ImportError):
    from ScrollableContainers._tk import ScrollableFrameTk
with _contextlib.suppress(ImportError):
    from ScrollableContainers._wx import ScrollablePanelWx
