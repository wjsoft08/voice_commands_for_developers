import kivy
import tkinter as tk
kivy.require("1.11.1")
from tkinter import filedialog
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size = (500,130)

class PathBoxLayout(BoxLayout):

    # Function called when equals is pressed
    def setpath(self, inputText):
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                file_path = filedialog.askopenfilename()
                inputText.text = file_path
            except Exception:
                inputText.text = "Error"

    def savepaths(self, eclipsePath, notepadPath, vscodePath):
        f = open("filePaths.txt", "w+")
        f.write("Eclipse="+eclipsePath+"\n")
        f.write("Notepad++=" + notepadPath + "\n")
        f.write("VSCode=" + vscodePath + "\n")
        f.close()
        print('File path saved')


class AlexaApp(App):

    def build(self):
        return PathBoxLayout()

    def on_start(self):
        f = open("filePaths.txt", "r")
        if f.mode == 'r':
            eclipsepath = f.readline().split('=')[1]
            notepadpath = f.readline().split('=')[1]
            vscodepath = f.readline().split('=')[1]
            self.root.ids.pathInput.text = eclipsepath
            self.root.ids.pathInput2.text = notepadpath
            self.root.ids.pathInput3.text = vscodepath


root = tk.Tk()
root.withdraw()
calcApp = AlexaApp()
calcApp.run()
