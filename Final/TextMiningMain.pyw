from tkinter import *
from FunctionFiles.MainFunctions import *

class TextMinerGUI(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.setupWidgets()

    def setupWidgets(self):
        # Top Menu bar
        self.menubar = Menu(self.master)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Ups", command=self.doNothing)
        self.menubar.add_cascade(label="File", menu=filemenu)
        self.parent.config(menu=self.menubar)

    def doNothing(self):
        pass


TextMiner = Tk()
TextMiner.title("TextMiner")
TextMiner.geometry("620x480")
TextMiner.resizable(False, False)
root = TextMinerGUI(TextMiner).grid()
TextMiner.mainloop()