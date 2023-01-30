#! /usr/bin/python3 -B

import wx
import wx.lib.scrolledpanel as scrolled

__all__ = ['ScrollablePanelWx']

###############################################################################

class ScrollablePanelWx(scrolled.ScrolledPanel):
    '''
Container with horizontal and vertical scrolling capabilities. Widgets must be
added to its `panel` attribute.
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # According to the documentation, a sizer is required to calculate the
        # minimum virtual size of the panel.
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.panel = wx.Panel(self)
        vbox.Add(self.panel, flag=wx.ALIGN_CENTRE)
        self.SetSizer(vbox)
