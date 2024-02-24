# start page class

# imports
from lib.components import *
from lib.widgets import AppFrame, AppLabel, AppButton, AppImageButton
from lib.functions import generate_grayscale_hex, generate_tk_geometry, generate_tk_image
from lib.app_root import fonts, user_preferences


class StartPage(object):
    FT_main = True
    FT_preferences = True

    def __init__(self, root):
        self.root = root

        self.defaults()

    def defaults(self):
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
        self.button2 = AppButton(self.mainFrame, 'Button2', placeholder, 0.25, 0.30)
        self.button3 = AppButton(self.mainFrame, 'Button3', placeholder, 0.25, 0.40)
        self.button4 = AppButton(self.mainFrame, 'Button4', placeholder, 0.25, 0.50)
        self.button5 = AppImageButton(self.mainFrame, generate_grayscale_hex(20),
                                      generate_tk_image('resources/preferences.png', 48, 48),
                                      self.gotoPreferences, 0.425, 0.65)

        self.button1.place(relwidth=0.50)
        self.button2.place(relwidth=0.50)
        self.button3.place(relwidth=0.50)
        self.button4.place(relwidth=0.50)
        self.button5.place(relwidth=0.15, relheight=0.075)

    def createCreditsLabel(self):
        credits_text = 'Created By: Yaqin Hasan'
        self.creditsLabel = AppLabel(self.mainFrame, credits_text, 0.25, 0.75)
        self.creditsLabel.configure(font=fonts['Default'], fg=generate_grayscale_hex(180))
        self.creditsLabel.place(relwidth=0.50, relheight=0.25)

    def createMain(self):
        self.mainPage = MainPage(self.root)

    def createPreferences(self):
        self.preferencesPage = PreferencesPage(self.root)

    def gotoMain(self):
        if self.FT_main:
            self.createMain()
            self.FT_main = False
        self.root.geometry(generate_tk_geometry(self.root, user_preferences['width'], user_preferences['height']))
        self.mainPage.mainFrame.tkraise()

    def gotoPreferences(self):
        if self.FT_preferences:
            self.createPreferences()
            self.FT_preferences = False

        self.preferencesPage.mainFrame.tkraise()
