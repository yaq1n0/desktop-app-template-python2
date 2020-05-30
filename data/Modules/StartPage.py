# start page class

# imports
from data.Modules.MainPage import MainPage
from data.Modules.PreferencesPage import PreferencesPage
from data.MyClasses.MyTkWidgets import MyFrame, MyLabel, MyButton
from data.MyFunctions.GrayScale import GrayScale
from data.MyFunctions.makeGeometry import makeGeometry
from data.MyVariables.MyFonts import MyFonts
from data.MyVariables.preferences import width as config_width
from data.MyVariables.preferences import height as config_height


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
        self.mainFrame = MyFrame(self.root, GrayScale(20))

    def createTitle(self):
        self.titleLabel = MyLabel(self.mainFrame, 'Welcome!', 0.25, 0.10)
        self.titleLabel.configure(font=MyFonts['ExtraLargeBold'])
        self.titleLabel.place(relwidth=0.50)

    def createButtons(self):
        def placeholder():
            pass

        self.button1 = MyButton(self.mainFrame, 'Main', self.gotoMain, 0.25, 0.20)
        self.button2 = MyButton(self.mainFrame, 'Button2', placeholder, 0.25, 0.30)
        self.button3 = MyButton(self.mainFrame, 'Button3', placeholder, 0.25, 0.40)
        self.button4 = MyButton(self.mainFrame, 'Settings', self.gotoPreferences, 0.25, 0.50)

        self.button1.place(relwidth=0.5)
        self.button2.place(relwidth=0.5)
        self.button3.place(relwidth=0.5)
        self.button4.place(relwidth=0.5)

    def createCreditsLabel(self):
        credits_text = 'Created By: Yaqin Hasan'
        self.creditsLabel = MyLabel(self.mainFrame, credits_text, 0.25, 0.75)
        self.creditsLabel.configure(font=MyFonts['Default'], fg=GrayScale(180))
        self.creditsLabel.place(relwidth=0.50, relheight=0.25)

    def createMain(self):
        self.mainPage = MainPage(self.root)

    def createPreferences(self):
        self.preferencesPage = PreferencesPage(self.root)

    def gotoMain(self):
        if self.FT_main:
            self.createMain()
            self.FT_main = False
        self.root.geometry(makeGeometry(self.root, config_width, config_height))
        self.mainPage.mainFrame.tkraise()

    def gotoPreferences(self):
        if self.FT_preferences:
            self.createPreferences()
            self.FT_preferences = False

        self.preferencesPage.mainFrame.tkraise()
