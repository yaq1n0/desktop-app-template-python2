""" PreferencesPage class """

from tkinter import END
from tkinter.messagebox import showinfo

from core import read_user_config, write_user_config, reload_default_config, load_fonts, generate_grayscale_hex
from ui import AppFrame, AppLabel, AppEntryBox, AppImageButton, AppToggleButton, generate_tk_image


class PreferencesPage(object):
    """ PreferencesPage class """

    def __init__(self, root):
        self.root = root

        self.createFrame()
        self.createTitle()
        self.createWidthEntry()
        self.createHeightEntry()
        self.createFontEntry()
        self.createFontSizeEntry()
        self.createToolTipToggle()
        self.createDevToggle()
        self.createResetButton()
        self.createSaveButton()

        self.setAll()

    def createFrame(self):
        self.mainFrame = AppFrame(self.root, generate_grayscale_hex(20))

    def createTitle(self):
        self.title_label = AppLabel(self.mainFrame, 'Modify Program Settings', 0.05, 0.05)
        self.title_label.configure(font=load_fonts()['ExtraLargeBold'])
        self.title_label.place(relwidth=0.9, relheight=0.05)

    def createWidthEntry(self):
        self.width_entry = AppEntryBox(self.mainFrame, 'Default Window Width (pixels)', 0.25, 0.20)
        self.width_entry.label.place(relwidth=0.90, relx=0.05)
        self.width_entry.place(relwidth=0.50, relheight=0.05)

    def createHeightEntry(self):
        self.height_entry = AppEntryBox(self.mainFrame, 'Default Window Height (pixels)', 0.25, 0.325)
        self.height_entry.label.place(relwidth=0.90, relx=0.05)
        self.height_entry.place(relwidth=0.50, relheight=0.05)

    def createFontEntry(self):
        self.font_entry = AppEntryBox(self.mainFrame, 'Font Name', 0.25, 0.450)
        self.font_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_entry.place(relwidth=0.50, relheight=0.05)

    def createFontSizeEntry(self):
        self.font_size_entry = AppEntryBox(self.mainFrame, 'Font Size (points)', 0.25, 0.575)
        self.font_size_entry.label.place(relwidth=0.90, relx=0.05)
        self.font_size_entry.place(relwidth=0.50, relheight=0.05)

    def createToolTipToggle(self):
        self.tooltips_button = AppToggleButton(self.mainFrame, 'Tooltips', 0.20, 0.70)

    def createDevToggle(self):
        self.dev_button = AppToggleButton(self.mainFrame, 'Developer', 0.60, 0.70)

    def createResetButton(self):
        self.reset_button = AppImageButton(self.mainFrame, generate_grayscale_hex(20),
                                           generate_tk_image('resources/images/reset.png', 48, 48),
                                           self.funcReset, 0.30, 0.85)
        self.reset_button.place(relwidth=0.14, relheight=0.07)

    def createSaveButton(self):
        self.save_button = AppImageButton(self.mainFrame, generate_grayscale_hex(20),
                                          generate_tk_image('resources/images/save.png', 48, 48),
                                          self.funcSave, 0.56, 0.85)
        self.save_button.place(relwidth=0.14, relheight=0.07)

    def clearALL(self):
        # clear all entries in GUI
        self.width_entry.delete(0, END)
        self.height_entry.delete(0, END)
        self.font_entry.delete(0, END)
        self.font_size_entry.delete(0, END)

    def setAll(self):
        # set all entries in GUI from imported vars from preferences.py
        self.clearALL()

        user_preferences = read_user_config()

        self.width_entry.insert(0, str(user_preferences['width']))
        self.height_entry.insert(0, str(user_preferences['height']))
        self.font_entry.insert(0, str(user_preferences['font']))
        self.font_size_entry.insert(0, str(user_preferences['font_size']))

        if user_preferences['tooltips'] == True:
            self.tooltips_button.func1()
        else:
            self.tooltips_button.func2()

        if user_preferences['dev'] == True:
            self.dev_button.func1()
        else:
            self.dev_button.func2()

    def checkAll(self):
        # checking that values are reasonable

        # check that numeric inputs are numeric
        numerics = [self.width_entry.get(), self.height_entry.get(), self.font_size_entry.get()]
        for numeric in numerics:
            if not numeric.isnumeric():
                raise Exception('You have entered a non-numeric in a field that only accepts numbers')

        # check that resolution is 16 by 9 and is a common resolution
        input_width = self.width_entry.get()
        input_height = self.height_entry.get()

        width_list = ['1280', '1920', '2560', '3840']
        height_list = ['720', '1080', '1440', '2160']

        if input_width not in width_list \
                or input_height not in height_list \
                or float(input_width) / float(input_height) != 16.0 / 9:
            raise Exception('You have selected an unexpected 16:9 resolution, this might cause unexpected errors')

        # if all the tests pass, return true
        return True

    def funcSave(self):
        # save and write to config
        if self.checkAll():
            new_user_preferences = {"width": int(self.width_entry.get()),
                                    "height": int(self.height_entry.get()),
                                    "font": self.font_entry.get(),
                                    "font_size": int(self.font_size_entry.get()),
                                    "tooltips": getattr(self.tooltips_button, 'enabled'),
                                    "dev": getattr(self.dev_button, 'enabled')
                                    }

            user_preferences = new_user_preferences.copy()

            write_user_config(user_preferences)

        showinfo('Settings Saved', 'Settings Saved, You might want to restart the program')

    def funcReset(self):
        # reset to defaults
        reload_default_config()
        self.setAll()

        showinfo('Defaults loaded', 'Defaults loaded, You might want to restart the program')
