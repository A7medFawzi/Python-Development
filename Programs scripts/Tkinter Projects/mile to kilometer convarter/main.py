from tkinter import *

window = Tk()
window.title("Mile To Kilometer Converter")
window.config(padx=15,pady=15)


def mile_converter ():
    miles = miles_input.get()
    kilometter = round(float(miles) * 1.6)
    value = kilometer_value.config(text=f"{kilometter}")



miles_input = Entry(width=8)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

kilometer_value = Label(text="0")
kilometer_value.grid(column=1,row=1)

kilometer_label= Label(text="KM")
kilometer_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=mile_converter)
calculate_button.grid(column=1,row=2)






























window.mainloop()

