#! /usr/bin/env python3

import itertools

import wx
from ScrollableContainers import ScrollablePanelWx


class ExamplesScrollablePanelWx:
    def __init__(self):
        self.grid_of_widgets(wx.Frame(None))
        self.single_widget(wx.Frame(None))

    def grid_of_widgets(self, window):
        window.SetTitle("`ScrollablePanelWx` Demo")

        # Create a scrollable panel.
        scrollable_panel = ScrollablePanelWx(window)

        # Add widgets to the ``panel`` attribute of the scrollable panel, not
        # to the scrollable panel itself.
        dim = 10
        grid_sizer = wx.GridSizer(dim, dim, 20, 20)
        for i, j in itertools.product(range(dim), repeat=2):
            text = wx.StaticText(scrollable_panel.panel, label=f"Label\n({i}, {j})")
            grid_sizer.Add(text)

        scrollable_panel.panel.SetSizer(grid_sizer)
        scrollable_panel.SetupScrolling()
        window.Show()

    def single_widget(self, window):
        window.SetTitle("`ScrollablePanelWx` Demo")
        window.SetSize(600, 200)

        scrollable_panel = ScrollablePanelWx(window)

        wx.StaticText(scrollable_panel.panel, label="big window, small label")

        scrollable_panel.SetupScrolling()
        window.Show()


if __name__ == "__main__":
    app = wx.App()
    examples = ExamplesScrollablePanelWx()
    app.MainLoop()
