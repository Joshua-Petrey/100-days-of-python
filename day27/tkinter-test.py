import tkinter

# new Tk instance
window = tkinter.Tk()

# create a title
window.title('My first GUI')

# set min-size of the gui
window.minsize(width=600, height=600)


# create a label
mylabel = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))
mylabel2 = tkinter.Label()

# pack label widget to display it (Packer is the geometry manager)
mylabel.pack()

# congi sets standard options()
mylabel2.config(font=('Georgia', 33, 'normal'))

# make a event for the button


def button_clicked():
    # .get() get the value in the entry(myInput) an out ir as myLabel's text
    mylabel["text"] = myInput.get()


# create a button widget
mybut = tkinter.Button(text="PUSH ME", padx=20, command=button_clicked)
mybut.pack()

# The entry component (an input)
myInput = tkinter.Entry(relief='groove')
myInput.pack()

# make a multiline text box
# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with. END is a property of tkinter
text.insert("0.0", "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()

# make radio buttons


def radio_used():
    print(selectedRadioValue.get())


selectedRadioValue = tkinter.IntVar()

radio1 = tkinter.Radiobutton(
    text='Option 1', value=1, variable=selectedRadioValue,  command=radio_used)
radio2 = tkinter.Radiobutton(
    text='Option 2', value=2, variable=selectedRadioValue,  command=radio_used)

radio1.pack()
radio2.pack()
# create a loop to keep window open

window.mainloop()
