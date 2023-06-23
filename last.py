import tkinter as tk

def insert_line():
    text_box.insert("end", "\u2028")  # Insert the line separator character at the end of the text box

# Create the GUI window
window = tk.Tk()

# Create the text box
text_box = tk.Text(window)
text_box.pack()

# Create a button to insert the line
button = tk.Button(window, text="Insert Line", command=insert_line)
button.pack()

# Start the GUI event loop
window.mainloop()