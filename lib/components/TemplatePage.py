# <template> page class

# imports

from lib.MyClasses import *
from lib.MyFunctions import *


class TemplatePage(object):
    def __init__(self, root):
        self.root = root

    def defaults(self):
        self.createFrame()

    def createFrame(self):
        self.mainFrame = MyFrame(self.root, GrayScale(20))
