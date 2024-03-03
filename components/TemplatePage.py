""" TemplatePage class """

from core import generate_grayscale_hex, load_fonts
from ui import AppFrame, AppLabel


class TemplatePage(object):
    """ TemplatePage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Template Page', 0.25, 0.10)
        self.titleLabel.configure(font=load_fonts()['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)
