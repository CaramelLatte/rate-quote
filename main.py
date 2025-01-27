import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Sample Input Form")
root.geometry("720x480")

# Create a frame to hold the list of labels and entry boxes
frame = tk.Frame(root)
frame.pack(pady=20)

items = ["V4", "V4+2010", "V4+ZPass", "V4+2010+ZPass"]
entries = {}
for item in items:
    row_frame = tk.Frame(frame)
    row_frame.pack(fill='x', pady=5)
    
    label = tk.Label(row_frame, text=item, width=20, anchor='w')
    label.pack(side='left', padx=10)
    
    entry = tk.Entry(row_frame, width=50)
    entry.pack(side='left', padx=10)
    
    entries[item] = entry

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the 'Copy' button, initially grayed out
copy_button = tk.Button(button_frame, text="Copy", state='disabled')
copy_button.pack(side='left', padx=10)

# Create the 'Enter' button
enter_button = tk.Button(button_frame, text="Enter")
enter_button.pack(side='left', padx=10)

# Store the entry widgets in a dictionary




def on_enter():
    data = {item: entry.get() for item, entry in entries.items()}
    box_builder(data)

# Update the 'Enter' button to call the on_enter function
enter_button.config(command=on_enter)

#UNFINISHED RESUME WORKING HERE
def box_builder(data):
    v4 = 0
    handheld = 0
    zpass = 0
    for item in data:
        if item == "V4":
            v4 += 1
        print(item, data[item])

# Run the application
root.mainloop()
