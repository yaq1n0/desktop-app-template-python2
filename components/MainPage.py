""" MainPage class """

<<<<<<< Updated upstream
<<<<<<<< Updated upstream:components/MainPage.py
from lib.app_root import generate_fonts
from lib.functions import generate_grayscale_hex
from lib.widgets import AppFrame, AppLabel
========
from lib.preferences import *
from lib.functions import *
from lib.widgets import *
>>>>>>>> Stashed changes:lib/components/MainPage.py
=======
from lib.app_root import *
from lib.functions import *
from lib.widgets import *
>>>>>>> Stashed changes


class MainPage(object):
    """ MainPage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Main Page', 0.25, 0.10)
<<<<<<< Updated upstream
        self.titleLabel.configure(font=generate_fonts()['ExtraLargeBold'])
=======
        self.titleLabel.configure(font=fonts['ExtraLargeBold'])
>>>>>>> Stashed changes
        self.titleLabel.place(relwidth=0.50)
