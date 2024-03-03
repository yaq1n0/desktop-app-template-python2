""" generate ToolTip widget with text """

# imports
from ui.app_widgets import AppToolTip

"""code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse
-cursor-in-python"""


def bind_tooltip(widget, text):
    """ generate ToolTip widget with text """

    tooltip = AppToolTip(widget)

    def enter(event):
        tooltip.showtip(text)

    def leave(event):
        tooltip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
