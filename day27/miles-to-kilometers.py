import tkinter as tk


def to_kilometers():
    kilo = round(float(miles_input.get()), 4) * 1.609
    kilometers_input.delete(0, tk.END)
    kilometers_input.insert(tk.END, str(kilo))


def to_miles():

    miles = round(float(kilometers_input.get()), 4) / 1.609
    miles_input.delete(0, tk.END)
    miles_input.insert(tk.END, str(miles))


window = tk.Tk()
window.title("Convert Miles to Kilometers")


miles_label = tk.Label(text="Enter Miles:")
miles_label.grid(column=0, row=0)
miles_label.config(padx=50, pady=50, font=("Arial", 24, "bold"))


miles_input = tk.Entry()
miles_input.grid(column=1, row=0)
miles_input.config(font=("Arial", 22, "normal"))

kilometers_label = tk.Label(text="Enter Kilometers:")
kilometers_label.grid(column=0, row=1)
kilometers_label.config(padx=50, pady=50, font=("Arial", 24, "bold"))


kilometers_input = tk.Entry()
kilometers_input.grid(column=1, row=1)
kilometers_input.config(font=("Arial", 22, "normal"))

# buttons
convert_to_miles = tk.Button(
    text='Convert kilometers to miles', command=to_miles, font=('Georgia', 18, 'normal'))
convert_to_miles.grid(column=0, row=2)

convert_to_kilometers = tk.Button(
    text='Convert miles to kilometers', command=to_kilometers, font=('Georgia', 18, 'normal'))
convert_to_kilometers.grid(column=1, row=2)

window.mainloop()
