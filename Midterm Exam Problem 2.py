import tkinter as tk

def convert():
    # Get the length in centimeters from the entry widget
    length_cm = float(entry_cm.get())

    # Convert to meters and display in the entry widget
    length_m = length_cm / 100
    entry_m.delete(0, tk.END)
    entry_m.insert(0, str(length_m))

    # Convert to kilometers and display in the entry widget
    length_km = length_cm / 100000
    entry_km.delete(0, tk.END)
    entry_km.insert(0, str(length_km))

# Create the main window
window = tk.Tk()
window.title("Length Converter")

# Create the entry widget for centimeters
label_cm = tk.Label(window, text="Centimeters:")
label_cm.grid(row=0, column=0)
entry_cm = tk.Entry(window)
entry_cm.grid(row=0, column=1)

# Create the entry widget for meters
label_m = tk.Label(window, text="Meters:")
label_m.grid(row=1, column=0)
entry_m = tk.Entry(window)
entry_m.grid(row=1, column=1)

# Create the entry widget for kilometers
label_km = tk.Label(window, text="Kilometers:")
label_km.grid(row=2, column=0)
entry_km = tk.Entry(window)
entry_km.grid(row=2, column=1)

# Create the convert button
button_convert = tk.Button(window, text="Convert", command=convert)
button_convert.grid(row=3, column=0, columnspan=2)

window.mainloop()