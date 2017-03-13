import tkinter


class MyFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tkinter.Label()
        self.label.pack()
        self.button = tkinter.Button(
                                     text="Say hello",
                                     command=self.say_hello)
        self.button.pack()

    def say_hello(self):
        self.label.configure(text="Hello World!")


root = tkinter.Tk()
frame = MyFrame(root)
frame.mainloop()