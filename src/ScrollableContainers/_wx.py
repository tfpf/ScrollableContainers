__all__ = ["ScrollablePanelWx"]

import wx
from wx.lib.scrolledpanel import ScrolledPanel


class ScrollablePanelWx(ScrolledPanel):
    """
    Container with horizontal and vertical scrolling capabilities. Widgets must
    be added to its ``panel`` attribute. Constructor arguments are passed to
    the parent constructor.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # According to the documentation, a sizer is required to calculate the
        # minimum virtual size of the panel.
        vbox = wx.BoxSizer(wx.VERTICAL)
        self._panel = wx.Panel(self)
        vbox.Add(self._panel, flag=wx.ALIGN_CENTRE)
        self.SetSizer(vbox)

    @property
    def panel(self):
        return self._panel
