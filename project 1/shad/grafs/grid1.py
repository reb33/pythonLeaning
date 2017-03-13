import tkinter


class MyFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        button1 = tkinter.Button(self,text="1")
        button1.grid(row=0, column=1)
        button2 = tkinter.Button(self,text="2")
        button2.grid(row=1, column=0, columnspan=2, sticky="nsew")
        button3 = tkinter.Button(self,text="3")
        button3.grid(row=1, column=2, rowspan=2)
        button4 = tkinter.Button(self,text="4")
        button4.grid(row=2, column=0)


root = tkinter.Tk()
frame = MyFrame(root)
frame.mainloop()