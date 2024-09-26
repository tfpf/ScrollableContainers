import contextlib as _contextlib
import logging as _logging

def _get_logger(name: str | None = None, level: int = _logging.INFO, fmt: str = "\x1b\x5b90m%(asctime)s\x1b\x5bm \x1b\x5b36m%(name)s\x1b\x5bm:\x1b\x5b36m%(lineno)s\x1b\x5bm %(message)s", datefmt: str = "%F %T%z") -> _logging.Logger:
    """
    Create a logger (if not already created).

    :param name: Logger name.
    :param level: Logging level.
    :param fmt: Logging format.
    :param datafmt: Date format in ``fmt``.

    :return: Logger.
    """
    formatter =_logging.Formatter(fmt, datefmt)
    stream_handler = _logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger = _logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(stream_handler)
    return logger

_logger = _get_logger(__name__)

with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt5 import ScrollableAreaQt5
    _logger.info("Imported `ScrollableAreaQt5`.")
with _contextlib.suppress(ImportError):
    from ScrollableContainers._qt6 import ScrollableAreaQt6
with _contextlib.suppress(ImportError):
    from ScrollableContainers._tk import ScrollableFrameTk
with _contextlib.suppress(ImportError):
    from ScrollableContainers._wx import ScrollablePanelWx
