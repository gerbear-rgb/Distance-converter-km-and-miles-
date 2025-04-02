import tkinter as tk
import ttkbootstrap as ttk

def convert_miles():
    mile_input = float(entry_val.get())
    km_output = f'{mile_input*1.609} km'
    output_string.set(km_output)

def convert_km():
    km_input = float(entry_val.get())
    mile_output = f'{km_input*0.621} miles'
    output_string.set(mile_output)

#window
root = ttk.Window(themename='journal')
root.title('Distance Converter')
root.geometry('425x150')

#title
title_label = ttk.Label(
    master=root,
    text='Miles to Kilometers',
    font='Calibri 24 bold'
)
title_label.pack()

#input field
input_frame = ttk.Frame(master=root)

entry_val=tk.StringVar()

entry = ttk.Entry(
    master=input_frame,
    textvariable=entry_val
)

miles_button = ttk.Button(
    master=input_frame,
    text="Convert to Km",
    command=convert_miles
)
km_button = ttk.Button(
    master=input_frame,
    text='Convert to miles',
    command=convert_km
)

entry.pack(side='left', padx=5)
miles_button.pack(side='left', padx=5)
km_button.pack(side='left', padx=5)
input_frame.pack(pady=10)

#output

output_string = tk.StringVar()

output_label = ttk.Label(
    master=root,
    text='Output',
    font='Calibri 24',
    textvariable=output_string
)

output_label.pack(pady=5)

#run
root.mainloop()
