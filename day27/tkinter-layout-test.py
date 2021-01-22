import tkinter

# make a event for the button


def button_clicked():
    # .get() get the value in the entry(myInput) an out ir as myLabel's text
    mylabel["text"] = myInput.get()


# new Tk instance
window = tkinter.Tk()

# create a title
window.title('My first GUI')

# set min-size of the gui
window.minsize(width=600, height=600)


# create a button widget
mybut = tkinter.Button(text="PUSH ME", padx=20,)
mybut.grid(column=0, row=0)

# The entry component (an input)
myInput = tkinter.Entry(relief='groove')
myInput.grid(column=1, row=1)


window.mainloop()
