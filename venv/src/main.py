from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import tkinter as tk
from tkinter import filedialog
from kivy.core.window import Window

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

    def save_paths(self, eclipsePath, notepadPath, vscodePath, screenManager,rootName):
        f = open("filePaths.txt", "w+")
        f.write("Eclipse="+eclipsePath+"\n")
        f.write("Notepad++=" + notepadPath + "\n")
        f.write("VSCode=" + vscodePath + "\n")
        f.close()
        print('File path saved')
        print(rootName)
        RootWidget.set_state(screenManager, rootName)


class PlayMenu(Screen):
    name = StringProperty('play_menu')

    def play_clicked(self):
        for i in range(20):
            self.ids.messages.add_widget(Button(text="play clicked", height='200sp'))
        self.h = i
        self.ids.messages.size = (1, self.h * 150)
        print('connect starting of alexa app here')

    def stop_clicked(self):
        print('disconnect alexa here')


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
                eclipsepath = f.readline().split('=')[1]
                notepadpath = f.readline().split('=')[1]
                vscodepath = f.readline().split('=')[1]
                self.root.ids.PathMenu.ids.pathInput.text = eclipsepath
                self.root.ids.PathMenu.ids.pathInput2.text = notepadpath
                self.root.ids.PathMenu.ids.pathInput3.text = vscodepath
        except Exception:
            print("file error")


root = tk.Tk()
root.withdraw()
if __name__ == '__main__':
    AlexaDevApp().run()