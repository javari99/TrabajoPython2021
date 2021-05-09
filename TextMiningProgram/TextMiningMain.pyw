
from os import path
from tkinter.constants import END, PROJECTING

from matplotlib.pyplot import tight_layout
from FunctionFiles.MainFunctions import *
import os
import json

import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk

import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class TextMiningUI:
    def __init__(self, master=None):
        # build ui
        self.dataDic = {}
        self.root = master
        self.MainFrame = ttk.Frame(master)
        self.frame1 = tk.Frame(self.MainFrame)
        self.tb_fileDirectory = tk.Entry(self.frame1)
        self.tb_fileDirectory.configure(exportselection='true', takefocus=False)
        _text_ = '''Choose file...'''
        self.tb_fileDirectory.delete('0', 'end')
        self.tb_fileDirectory.insert('0', _text_)
        self.tb_fileDirectory.grid(column='0', row='4')
        self.tb_fileDirectory.columnconfigure('0', pad='10')
        self.tb_fileDirectory.bind('<1>', self.callback, add='')

        self.l_Analysis = ttk.Label(self.frame1)
        self.l_Analysis.configure(font='{File analysis} 12 {bold underline}', text='File analysis')
        self.l_Analysis.grid(column='0', row='0', rowspan='3', sticky='ne')
        self.l_Analysis.rowconfigure('0', minsize='100', pad='0', weight='0')
        self.l_Analysis.columnconfigure('0', pad='10')

        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text='Choose file to scrap')
        self.label3.grid(column='0', row='3')
        self.label3.columnconfigure('0', pad='10')

        self.btn_analyze = ttk.Button(self.frame1, command=self.analyzeFile)
        self.btn_analyze.configure(compound='left', text='Analyze')
        self.btn_analyze.grid(column='0', columnspan='2', row='5')
        self.btn_analyze.rowconfigure('5', minsize='0', pad='10')
        self.btn_analyze.columnconfigure('0', pad='10')

        self.btn_loadFileBrowse = ttk.Button(self.frame1, command=self.loadBrowseButton)
        self.btn_loadFileBrowse.configure(text='Browse')
        self.btn_loadFileBrowse.grid(column='1', row='4')
        self.frame1.configure(height='200', width='200')
        self.frame1.grid(column='0', row='0')
        self.frame1.rowconfigure('0', pad='10')
        self.frame1.columnconfigure('0', pad='10')

        self.frame2 = tk.Frame(self.MainFrame)

        self.vScroll = ttk.Scrollbar(self.frame2)
        self.vScroll.configure(orient='vertical')
        self.vScroll.grid(column='1', row='1', rowspan='2', sticky='nse')
        self.vScroll.rowconfigure('1', pad='0')
        self.hScroll = ttk.Scrollbar(self.frame2)
        self.hScroll.configure(orient='horizontal')
        self.hScroll.grid(column='0', row='2', sticky='ew')

        self.treeview1 = ttk.Treeview(self.frame2, yscrollcommand=self.vScroll.set, xscrollcommand=self.hScroll.set)
        self.treeview1.grid(column='0', row='1', rowspan='1', sticky='nsew')
        self.treeview1.rowconfigure('1', pad='0')
        self.treeview1.columnconfigure('0', minsize='900', pad='0')

        self.label4 = ttk.Label(self.frame2)
        self.label4.configure(cursor='arrow', font='{All analyzed} 12 {bold underline}', text='All analyzed')
        self.label4.grid(column='0', row='0', sticky='n')
        self.label4.columnconfigure('0', minsize='900', pad='0')

        self.frame2.configure(height='200', width='200')
        self.frame2.grid(column='2', columnspan='1', row='0', rowspan='3', sticky='nsew')
        self.frame2.rowconfigure('0', pad='10')

        self.frame4 = tk.Frame(self.MainFrame)

        self.label5 = ttk.Label(self.frame4)
        self.label5.configure(cursor='arrow', takefocus=False, text='Export Selected to excell')
        self.label5.grid(column='0', row='0')
        self.label5.columnconfigure('0', pad='10')

        self.btn_saveFileBrowse = ttk.Button(self.frame4, command=self.saveBrowseButton)
        self.btn_saveFileBrowse.configure(text='Browse')
        self.btn_saveFileBrowse.grid(column='1', row='1')
        self.btn_saveFileBrowse.columnconfigure('1', pad='10')

        self.tb_saveDir = ttk.Entry(self.frame4)
        _text_ = '''choose target...'''
        self.tb_saveDir.delete('0', 'end')
        self.tb_saveDir.insert('0', _text_)
        self.tb_saveDir.grid(column='0', row='1')
        self.tb_saveDir.columnconfigure('0', pad='10')

        self.btn_save = ttk.Button(self.frame4, command=self.exportAsExcell)
        self.btn_save.configure(text='Export')
        self.btn_save.grid(column='0', columnspan='2', row='2')
        self.btn_save.rowconfigure('2', pad='10')
        self.btn_save.columnconfigure('0', pad='10')
        self.frame4.configure(height='200', width='200')
        self.frame4.grid(column='0', columnspan='1', row='2', rowspan='1')
        self.frame4.rowconfigure('0', pad='10')

        self.separator1 = ttk.Separator(self.MainFrame)
        self.separator1.configure(orient='vertical')
        self.separator1.grid(column='1', columnspan='1', row='0', rowspan='2', sticky='ns')

        self.separator2 = ttk.Separator(self.MainFrame)
        self.separator2.configure(orient='horizontal')
        self.separator2.grid(column='0', row='1', sticky='ew')
        """
        self.frame3 = ttk.Frame(self.MainFrame)
        self.canvas1 = FigureCanvasTkAgg(Figure(figsize=(6,5)),master=self.frame3)
        self.canvas1.grid(column='1', columnspan='2', row='1', sticky='nsew')
        self.btn_plot = ttk.Button(self.frame3, command=self.plotCostPerInvoice)
        self.btn_plot.configure(text='Plot')
        self.btn_plot.grid(column='0', columnspan='1', row='1')
        self.label1 = ttk.Label(self.frame3)
        self.label1.configure(font='{Plot cost per invoice} 12 {bold underline}', text='Plot cost per invoice')
        self.label1.grid(column='0', columnspan='3', row='0')
        self.frame3.configure(height='200', width='200')
        self.frame3.grid(column='0', columnspan='3', row='3', sticky='nsew')
        """

        self.frame3 = ttk.Frame(self.MainFrame)
        self.btn_plot = ttk.Button(self.frame3, command=self.plotCostPerInvoice)
        self.btn_plot.configure(text='Plot')
        self.btn_plot.grid(column='0', columnspan='1', row='1')
        self.label1 = ttk.Label(self.frame3)
        self.label1.configure(font='{Plot cost per date} 12 {bold underline}', text='Plot cost per date')
        self.label1.grid(column='0', columnspan='1', row='0')
        self.frame3.configure(height='200', width='200')
        self.frame3.grid(column='0', columnspan='1', row='3', sticky='nsew')
        self.frame6 = ttk.Frame(self.MainFrame)
        self.canvas = FigureCanvasTkAgg(Figure(figsize=(6,5)), master=self.frame6)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)
        self.frame6.configure(height='200', width='200')
        self.frame6.grid(column='1', columnspan='4', row='3', sticky='nsew')

        self.MainFrame.configure(height='720', width='1280')
        self.MainFrame.pack(side='top')

        # Main widget
        self.mainwindow = self.MainFrame

    def callback(self, event=None):
        pass

    def run(self):
        self.mainwindow.mainloop()

    def updateTreeView(self):
        self.treeview1.delete(*self.treeview1.get_children())

        _thisFileDirectory = os.path.dirname(__file__)
        rootDir = _thisFileDirectory
        analizedDir = os.path.join(rootDir, "AnalyzedInvoices")
        os.makedirs(analizedDir, exist_ok=True)
        directories = os.listdir(analizedDir)
        for directory in directories:
            item = self.treeview1.insert("", tk.END, text=directory)
            print(directory)
            for file in os.listdir(os.path.join(analizedDir, directory)):
                self.treeview1.insert(item, tk.END, text=file)
                path = os.path.join(analizedDir, directory) + "/"+file
                #print(f"\n\n{file}:\n\t{loadAnalyzedFile(path)}")
                self.dataDic[file] = loadAnalyzedFile(path)
    
    def analyzeFile(self):
        #try:
        print(self.tb_fileDirectory.get())
        analyzeJSON(self.tb_fileDirectory.get())
        self.updateTreeView()
        #except:
            #print("Error file not found")

    def loadBrowseButton(self):
        filename = tkinter.filedialog.askopenfilename()
        self.root.update()
        self.tb_fileDirectory.delete(0,END)
        self.tb_fileDirectory.insert(0,filename)

    def saveBrowseButton(self):
        filename = tkinter.filedialog.asksaveasfilename(defaultextension=".xlsx", initialfile="result")
        self.root.update()
        self.tb_saveDir.delete(0,END)
        self.tb_saveDir.insert(0,filename)

    def exportAsExcell(self):
        dic = {}
        for item in self.treeview1.selection():
            name = self.treeview1.item(item)["text"]
            if name in self.dataDic:
                dic[name] = self.dataDic[name]
        exportToExcel(dic, self.tb_saveDir.get())

    def plotCostPerInvoice(self):
        dic = {}
        for item in self.treeview1.selection():
            name = self.treeview1.item(item)["text"]
            if name in self.dataDic:
                dic[name] = self.dataDic[name]["PrecioTotal"]
        filenames = [el.replace(".json","") for el in dic.keys()]
        values = list(dic.values())
        dic = {"filenames": filenames, "Total":values}
        df = pd.DataFrame.from_dict(dic)
        figure = Figure(figsize=(6,5), tight_layout=True)
        ax = figure.subplots()
        sns.barplot(y="filenames", x="Total", data=df, ax=ax)
        self.canvas.figure = figure
        self.canvas.draw()

if __name__ == '__main__':

    import tkinter as tk
    root = tk.Tk()
    root.title("TextMiner")
    root.update()
    app = TextMiningUI(root)
    app.updateTreeView()
    app.run()






