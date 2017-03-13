import tkinter


def main():
    root = tkinter.Tk()
    label = tkinter.Label(root, text="Hello word!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()