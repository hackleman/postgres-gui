import connect as postgres
import helper as guihelper
import tkinter as tk
from tkinter import ttk

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

        for Frame in (Index, Views, Create, Delete, Upload, Connection):

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

        button2 = ttk.Button(self, text="View", style='TButton', command=lambda: controller.show_frame(Views))
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


class Views(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        self.console = tk.StringVar()

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="View Stored Tables", font=fontstyle)
        label.pack(pady = 100, padx = 100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        # Text input area and Submission button
        textbox = tk.Text(self, height = 1, width = 25)
        label = ttk.Label(self, text="Find Table by Name")
        zonebutton = ttk.Button(self, text = "View Table by Zone Name", command = lambda: guihelper.getTable(self, textbox))
        output = ttk.Label(self, textvariable=self.console)
        label.pack()
        textbox.pack()
        zonebutton.pack(pady=15)
        output.pack(pady = 30)


        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)


class Create(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Create A Table", font=fontstyle)
        label.pack(pady = 100, padx = 100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        # Text input area and Submission button
        textbox = tk.Text(self, height = 1, width = 25)
        label = ttk.Label(self, text="Create Table by Name")
        label.pack()
        textbox.pack()
        zonebutton = ttk.Button(self, text = "Create", command = lambda: guihelper.getName(textbox))
        zonebutton.pack(pady=15)


        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)


class Upload(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Upload a table from CSV", font=fontstyle)
        label.pack(pady = 100, padx = 100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        # Text input area and Submission button
        textbox = tk.Text(self, height = 1, width = 25)
        label = ttk.Label(self, text="Upload a CSV file")
        label.pack()
        textbox.pack()
        zonebutton = ttk.Button(self, text = "Upload", command = lambda: guihelper.getName(textbox))
        zonebutton.pack(pady=15)


        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)


class Delete(tk.Frame):
    def __init__(self, parent, controller):

        # Setup Frame label and layout
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Delete A Table", font=fontstyle)
        label.pack(pady = 100, padx = 100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        # Text input area and Submission button
        textbox = tk.Text(self, height = 1, width = 25)
        label = ttk.Label(self, text="Delete Table by Name")
        label.pack()
        textbox.pack()
        zonebutton = ttk.Button(self, text = "Delete", command = lambda: guihelper.getName(textbox))
        zonebutton.pack(pady=15)



        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)

class Connection(tk.Frame):
    def __init__(self, parent, controller):
        
        # Setup Frame label and layout
        self.connectionstr = tk.StringVar()

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Set Connection Parameters", font=fontstyle)
        label.pack(pady = 50, padx = 100)
        bottom = tk.Frame(self)
        bottom.pack(side = 'bottom')

        # Text input area and Submission button
        self.host = tk.Text(self, height = 1, width = 25)
        hostLabel = ttk.Label(self, text="Host:")
        self.dbname = tk.Text(self, height = 1, width = 25)
        dbnameLabel = ttk.Label(self, text="Dbname: ")
        self.user = tk.Text(self, height = 1, width = 25)
        userLabel = ttk.Label(self, text="User:")
        self.password = tk.Text(self, height = 1, width = 25)
        passwordLabel = ttk.Label(self, text="Password:")
        self.port = tk.Text(self, height = 1, width = 25)
        portLabel = ttk.Label(self, text="Port (optional):")

        create = ttk.Button(self, text = "Submit", command = lambda: guihelper.getConfig(self))
        output = ttk.Label(self, textvariable=self.connectionstr)

        hostLabel.pack()
        self.host.pack()
        dbnameLabel.pack()
        self.dbname.pack()
        userLabel.pack()
        self.user.pack()
        passwordLabel.pack()
        self.password.pack()
        portLabel.pack()
        self.port.pack()

        create.pack(pady=25)
        output.pack()

        index = ttk.Button(bottom, text = "Back to Index", command = lambda: controller.show_frame(Index))
        index.pack(pady=15)

app = main()
app.mainloop()