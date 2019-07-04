import sys, os
from sys import path

import tkinter as tk
from tkinter import ttk

path.append(path[0] + '\helpers')

import database as postgres
import guihelper as guihelper
import frame as frame

fontstyle = ("Helvetica", 18)

class main(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        # Set icons and title
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='./icons/now-black.ico')
        tk.Tk.wm_title(self, 'PostgreSQL Developer')

        # Setup frame layout for application
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Frame "Router" for use in the index
        self.frames = {}

        for Frame in (Index, View, Create, Delete, Upload, Connection):

            frame = Frame(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[Frame] = frame

        self.show_frame(Index)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class Index(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup frame layout
        self.connectionstr = tk.StringVar()

        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PostgreSQL Developer", font=fontstyle)
        label.pack(pady=80, padx=100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        button2 = ttk.Button(self, text="View", command=lambda: controller.show_frame(View))
        button3 = ttk.Button(self, text="Create", command=lambda: controller.show_frame(Create))
        button4 = ttk.Button(self, text="Delete", command=lambda: controller.show_frame(Delete))
        button5 = ttk.Button(self, text="Upload", command=lambda: controller.show_frame(Upload))
        test = ttk.Button(bottom, text="Test Connection", command=lambda: guihelper.connectionTest(self))
        output = ttk.Label(self, textvariable=self.connectionstr)
        editconn = ttk.Button(bottom, text="Edit Connection Details", command=lambda: controller.show_frame(Connection))
        defaultconn = ttk.Button(bottom, text="Use default connection", command=lambda: guihelper.setdefaultconfig(self))

        button2.pack(pady=5)
        button3.pack(pady=5)
        button4.pack(pady=5)
        button5.pack(pady=5)
        output.pack(pady = 50)

        test.pack(pady=(10, 10))
        editconn.pack(pady=(10, 10))
        defaultconn.pack(pady = (10, 100))

class View(tk.Frame):
    def __init__(self, parent, controller):

        self.console = tk.StringVar();
        tk.Frame.__init__(self, parent)
        frame.View(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class Create(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Create(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)

class Upload(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Upload(self, parent, controller)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)


class Delete(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        frame.Delete(self, parent)

        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')
        ttk.Button(bottom, text = "Back to vewx", command = lambda: controller.show_frame(Index)).pack(pady=15)
        
class Connection(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        self.connectionstr = tk.StringVar()

        tk.Frame.__init__(self, parent)       
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        frame.Connection(self, parent)

        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)

