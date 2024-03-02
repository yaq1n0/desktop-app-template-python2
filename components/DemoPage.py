""" DemoPage class """

<<<<<<< Updated upstream
<<<<<<<< Updated upstream:components/DemoPage.py
from main import appState
from lib.functions import generate_grayscale_hex
from lib.widgets import AppFrame, AppLabel
========
from lib.preferences import *
from lib.functions import *
from lib.widgets import *
>>>>>>>> Stashed changes:lib/components/DemoPage.py
=======
from lib.app_root import *
from lib.functions import *
from lib.widgets import *
>>>>>>> Stashed changes


class DemoPage(object):
    """ DemoPage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Demo Page', 0.25, 0.10)
<<<<<<< Updated upstream
        self.titleLabel.configure(font=appState.fonts['ExtraLargeBold'])
=======
        self.titleLabel.configure(font=fonts['ExtraLargeBold'])
>>>>>>> Stashed changes
        self.titleLabel.place(relwidth=0.50)
