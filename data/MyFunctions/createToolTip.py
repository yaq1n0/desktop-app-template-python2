# createToolTip function for ToolTip object


# code from 'https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python'
def CreateToolTip(widget, text):
    from data.MyClasses.ToolTip import ToolTip
    # initializing toolTip instance of ToolTip class
    toolTip = ToolTip(widget)

    # binding enter event to showtip method
    def enter(event):
        toolTip.showtip(text)

    # binding leave event to hidetip method
    def leave(event):
        toolTip.hidetip()

    # binging enter and leave
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
