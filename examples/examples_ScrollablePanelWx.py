#! /usr/bin/python3 -B

import itertools
import wx

from ScrollableContainers.Wx import ScrollablePanelWx

###############################################################################

def grid_of_widgets():
    app = wx.App()
    root = wx.Frame(None, title='`ScrollablePanelWx` Demo')

    # Create a scrollable panel.
    scrollable_panel = ScrollablePanelWx(root)

    # Add widgets to the `panel` attribute of the scrollable panel, not to the
    # scrollable panel itself.
    dim = 10
    grid_sizer = wx.GridSizer(dim, dim, 20, 20)
    for (i, j) in itertools.product(range(dim), range(dim)):
        grid_sizer.Add(wx.StaticText(scrollable_panel.panel, label=f'Label\n({i}, {j})'))

    scrollable_panel.panel.SetSizer(grid_sizer)
    scrollable_panel.SetupScrolling()
    root.Show()
    app.MainLoop()

###############################################################################

def single_widget():
    app = wx.App()
    root = wx.Frame(None, title='`ScrollablePanelWx` Demo', size=(600, 200))

    scrollable_panel = ScrollablePanelWx(root)

    wx.StaticText(scrollable_panel.panel, label='bing window, small label')

    scrollable_panel.SetupScrolling()
    root.Show()
    app.MainLoop()

###############################################################################

if __name__ == '__main__':
    grid_of_widgets()
    single_widget()
