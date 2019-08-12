from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
import tkinter as tk
from tkinter import filedialog
from kivy.core.window import Window

import message_processor
from datetime import timedelta

Window.size = (300,500)


class PathMenu(Screen):
    name = StringProperty('path_menu')

    def set_path(self, inputText):
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                file_path = filedialog.askopenfilename()
                inputText.text = file_path
            except Exception:
                inputText.text = "Error"

    def save_paths(self, eclipsePath, notepadPath, vscodePath, chromePath, githubPath, screenManager,rootName):

        print(eclipsePath)
        print(notepadPath)
        print(vscodePath)
        f = open("filePaths.txt", "w+")
        f.write("Eclipse="+eclipsePath+"\n")
        f.write("IntelliJ=" + notepadPath+ "\n")
        f.write("VSCode=" + vscodePath+ "\n")
        f.write("Chrome=" + chromePath+ "\n")
        f.write("GitHubDesktop=" + githubPath)
        f.close()
        print('File path saved')
        print(rootName)
        RootWidget.set_state(screenManager, rootName)


class PlayMenu(Screen):
    name = StringProperty('play_menu')
    message_number = 0

    def play_clicked(self, playButton):

        print('connect starting of alexa app here')
        if message_processor.getswitch():
            playButton.text = "Play"
            message_processor.switchoff(self)
            PlayMenu.message_number += 1
            self.ids.messages.add_widget(Label(text="Application stopped", height='50sp'))
            self.h = PlayMenu.message_number
            self.ids.messages.size = (1, self.h * 50)
        else:
            playButton.text = "Stop"
            message_processor.switchon(self)
            PlayMenu.message_number += 1
            self.ids.messages.add_widget(Label(text="Application has started", height='50sp'))
            self.h = PlayMenu.message_number
            self.ids.messages.size = (1, self.h * 50)

    def add_message(self, message):
        print('add message: '+ message)
        PlayMenu.message_number += 1
        # for i in range(20):
        #     self.ids.messages.add_widget(Label(text="play clicked", height='200sp'))
        # self.h = i
        self.ids.messages.add_widget(Label(text=message, height='50sp'))
        self.h = PlayMenu.message_number
        self.ids.messages.size = (1, self.h * 50)


class RootWidget(Widget):
    state = StringProperty('set_main_menu_state')
    screen_manager = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def on_state(self, instance, value):
        if value == 'path_menu':
            self.screen_manager.current = 'path_menu'

    def set_state(self, state):
        if state == 'path_menu':
            self.screen_manager.current = 'play_menu'
        if state == 'play_menu':
            self.screen_manager.current = 'path_menu'


class AlexaDevApp(App):

    def build(self):
        pass

    def on_start(self):
        try:
            f = open("filePaths.txt", "r")
            if f.mode == 'r':
                eclipsepath = f.readline().split('=')[1].splitlines()[0]
                intellijpath = f.readline().split('=')[1].splitlines()[0]
                vscodepath = f.readline().split('=')[1].splitlines()[0]
                chromepath = f.readline().split('=')[1].splitlines()[0]
                githubpath = f.readline().split('=')[1].splitlines()[0]
                self.root.ids.PathMenu.ids.pathInput.text = eclipsepath
                self.root.ids.PathMenu.ids.pathInput2.text = intellijpath
                self.root.ids.PathMenu.ids.pathInput3.text = vscodepath
                self.root.ids.PathMenu.ids.pathInput4.text = chromepath
                self.root.ids.PathMenu.ids.pathInput5.text = githubpath
        except Exception:
            print("file error")


root = tk.Tk()
root.withdraw()
if __name__ == '__main__':
    AlexaDevApp().run()