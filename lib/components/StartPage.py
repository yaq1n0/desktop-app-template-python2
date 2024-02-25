""" StartPage class """

# imports
import webbrowser

from lib.app_root import *
from lib.functions import *
from lib.widgets import *
from .DemoPage import DemoPage
from .MainPage import MainPage
from .PreferencesPage import PreferencesPage
from .TemplatePage import TemplatePage


class StartPage(object):
    """ StartPage class """
    main_generated = False
    demo_generated = False
    template_generated = False
    preferences_generated = False

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()
        self.createButtons()
        self.createCreditsLabel()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.titleLabel = AppLabel(self.mainFrame, 'Welcome!', 0.25, 0.10)
        self.titleLabel.configure(font=fonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)

    def createButtons(self):
        def placeholder():
            pass

        self.button1 = AppButton(self.mainFrame, 'Main', self.gotoMain, 0.25, 0.20)
        self.button2 = AppButton(self.mainFrame, 'Demo', self.gotoDemo, 0.25, 0.30)
        self.button3 = AppButton(self.mainFrame, 'Template', self.gotoTemplate, 0.25, 0.40)
        self.button4 = AppImageButton(self.mainFrame, generate_grayscale_hex(20),
                                      generate_tk_image('resources/preferences.png', 48, 48),
                                      self.gotoPreferences, 0.46, 0.60)

        self.button1.place(relwidth=0.50)
        self.button2.place(relwidth=0.50)
        self.button3.place(relwidth=0.50)
        self.button4.place(relwidth=0.08, relheight=0.08 * (16 / 9))

    def createCreditsLabel(self):
        credits_text = 'Created By: Yaqin Hasan'
        self.creditsLabel = AppButton(self.mainFrame, credits_text, self.gotoCreatorSite, 0.25, 0.80)
        self.creditsLabel.place(relwidth=0.50, relheight=0.10)

    def createMain(self):
        self.mainPage = MainPage(self.root)
        self.main_generated = True

    def createDemo(self):
        self.demoPage = DemoPage(self.root)
        self.demo_generated = True

    def createTemplate(self):
        self.templatePage = TemplatePage(self.root)
        self.template_generated = True

    def createPreferences(self):
        self.preferencesPage = PreferencesPage(self.root)
        self.preferences_generated = True

    def gotoMain(self):
        if not self.main_generated:
            self.createMain()

        self.mainPage.mainFrame.tkraise()

    def gotoDemo(self):
        if not self.demo_generated:
            self.createDemo()

        self.demoPage.mainFrame.tkraise()

    def gotoTemplate(self):
        if not self.template_generated:
            self.createTemplate()

        self.templatePage.mainFrame.tkraise()

    def gotoPreferences(self):
        if not self.preferences_generated:
            self.createPreferences()

        self.preferencesPage.mainFrame.tkraise()

    def gotoCreatorSite(self):
        url = "https://yaqinhasan.com"
        webbrowser.open(url, new=1, autoraise=True)
