from tkinter import *

window = Tk()
window.title("Ishita's GUI program")
window.minsize(100, 100)
# adding padding
window.config(padx=50, pady=50)

# entry
entry = Entry(width=10, bg="light green")
entry.grid(column=1, row=0)

# label
my_label = Label(text="Miles")
my_label.grid(column=2, row=0)

# label
my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)

# label
my_label = Label(text="Km")
my_label.grid(column=2, row=1)


# button
def button_clicked():
    label1.config(text=float(entry.get()) * 1.60934)


button = Button(text="calculate", command=button_clicked, bg="lavender")
button.grid(column=1, row=3)

label1 = Label(text=0)
label1.grid(column=1, row=1)
window.mainloop()
