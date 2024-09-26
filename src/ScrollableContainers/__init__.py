import contextlib as _contextlib
import warnings as _warnings

with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt5 import ScrollableAreaQt5
with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt6 import ScrollableAreaQt6
with _contextlib.suppress(ImportError):
    from ScrollableContainers._tk import ScrollableFrameTk
with _contextlib.suppress(ImportError):
    from ScrollableContainers._wx import ScrollablePanelWx

_not_imported = {"ScrollableAreaQt5", "ScrollableAreaQt6", "ScrollableFrameTk", "ScrollablePanelWx"}.difference(dir())
if _not_imported:
    _warnings.warn(f"The following submodules could not be imported: {_not_imported}.", UserWarning, stacklevel=1)
