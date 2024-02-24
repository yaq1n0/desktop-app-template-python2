# <template> page class

# imports

from lib.components import *
from lib.widgets import AppFrame
from lib.functions import generate_grayscale_hex


class TemplatePage(object):
    def __init__(self, root):
        self.root = root

    def defaults(self):
        self.createFrame()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))
