""" generate ToolTip widget with text """


"""code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse
-cursor-in-python"""


def generate_ToolTip(widget, text):
    """ generate ToolTip widget with text """
    from lib.widgets.AppToolTip import ToolTip

    tooltip = ToolTip(widget)

    def enter(event):
        tooltip.showtip(text)

    def leave(event):
        tooltip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
