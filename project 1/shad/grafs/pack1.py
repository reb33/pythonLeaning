import tkinter


class MyFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        button1 = tkinter.Button(text="1")
        button1.pack(side="left", fill="y", expand=True)
        button2 = tkinter.Button(text="2")
        button2.pack(side="top")
        button3 = tkinter.Button(text="3")
        button3.pack(side="left")
        button4 = tkinter.Button(text="4")
        button4.pack(side="right")


root = tkinter.Tk()
frame = MyFrame(root)
frame.mainloop()