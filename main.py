import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Freight Quote Tool")
root.geometry("720x480")

# Create a frame to hold the list of labels and entry boxes
frame = tk.Frame(root)
frame.pack(pady=20)

#Item template class
class Items():
    def __init__(self, item, weight):
        self.item = item
        self.weight = weight
        self.boxes={"v4kit": 0, "9x8x4": 0, "small": 0, "10x10x5": 0, "cube": 0, "square": 0, "v4master": 0, "6pak": 0, "9pak-3": 0, "9pak-6": 0, "9pak": 0, "samsungkit": 0, "connectkit": 0,  "samsung4pk": 0, "connectmast": 0}

#Define items, and update the boxes attribute (weight is rounded up per sku)
v4kit = Items("V4 Kit", 0.7)
v4kit.boxes.update({"v4kit": 1, "9x8x4": 4, "v4master": 20, "6pak": 42, "connectmast": 50})

v4kit_handheld = Items("V4 + Handheld", 3)
v4kit_handheld.boxes.update({"9x8x4": 1, "cube": 2, "9pak": 9, "9pak-6": 6, "9pak-3": 3})

v4kit_zpass = Items("V4 + Zpass", 3)
v4kit_zpass.boxes.update({"v4kit": 1, "9x8x4": 2, "6pak": 6, "9pak": 9, "9pak-6": 6, "9pak-3": 3})

v4kit_handheld_zpass = Items("V4kit + Handheld + Zpass", 5)
v4kit_handheld_zpass.boxes.update({"9x8x4": 1, "cube": 2, "9pak": 9, "9pak-6": 6, "9pak-3": 32})

tablet = Items("Tablet Kit", 4)
tablet.boxes.update({"samsungkit": 1, "samsung4pk": 4})

tablet_v4 = Items("Tablet + V4", 5)
tablet_v4.boxes.update({"samsungkit": 1, "samsung4pk": 4})

tablet_camera = Items("Tablet + Camera", 7)
tablet_camera.boxes.update({"connectkit": 1, "connectmast": 4})

tablet_camera_v4 = Items("Tablet + Camera + V4", 8)
tablet_camera_v4.boxes.update({"connectkit": 1, "connectmast": 4})

ztrak = Items("Ztrak", 0.5)
ztrak.boxes.update({"9x8x4": 24, "square": 80, "v4master": 136})

cards = Items("Cards", 0.01)
cards.boxes.update({"9x8x4": 600, "cube": 1200, "v4master": 2000})

items = []
items.append(v4kit)
items.append(v4kit_handheld)
items.append(v4kit_zpass)
items.append(v4kit_handheld_zpass)
items.append(tablet)
items.append(tablet_v4)
items.append(tablet_camera)
items.append(tablet_camera_v4)
items.append(ztrak)
items.append(cards)

class Boxes():  
    def __init__(self, template, weight, length=0, width=0, height=0):
        self.template = template
        self.weight = weight
boxes = []

#Define all of the box templates, add them to array
class Templates():
    def __init__(self, template, length, width, height):
        self.template = template
        self.length = length
        self.width = width
        self.height = height

templates = []
v4kittemplate = Templates("v4kit", 12, 2, 7)
templates.append(v4kittemplate)
ninetemplate = Templates("9x8x4", 9, 8, 4)
templates.append(ninetemplate)
smalltemplate = Templates("small", 10, 10, 4)
templates.append(smalltemplate)
tentemplate = Templates("10x10x5", 10, 10, 5)
templates.append(tentemplate)
cubetemplate = Templates("cube", 10, 10, 10)
templates.append(cubetemplate)
squaretemplate = Templates("square", 14, 14, 6)
templates.append(squaretemplate)
v4mastertemplate = Templates("v4master", 21, 12, 7)
templates.append(v4mastertemplate)
sixpaktemplate = Templates("6pak", 21, 11, 15)
templates.append(sixpaktemplate)
ninepaktemplate = Templates("9pak", 27, 10, 15)
templates.append(ninepaktemplate)
ninepak6template = Templates("9pak-6", 27, 10, 10)
templates.append(ninepak6template)
ninepakthreetemplate = Templates("9pak-3", 27, 10, 5)
templates.append(ninepakthreetemplate)
samsungkittemplate = Templates("samsungkit", 7, 11, 11)
templates.append(samsungkittemplate)
samsung4pktemplate = Templates("samsung4pk", 23, 15, 11)
templates.append(samsung4pktemplate)
connectkittemplate = Templates("connectkit", 12, 11, 8)
templates.append(connectkittemplate)
connectmasttemplate = Templates("connectmast", 22, 12, 16)
templates.append(connectmasttemplate)


# Create the labels and entry boxes
entries = {}
for item in items:
    row_frame = tk.Frame(frame)
    row_frame.pack(fill='x', pady=5)
    
    label = tk.Label(row_frame, text=item.item, width=20, anchor='w')
    label.pack(side='left', padx=10)
    
    entry = tk.Entry(row_frame, width=50)
    entry.pack(side='left', padx=10)
    
    entries[item.item] = entry

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create the 'Copy' button, initially grayed out
copy_button = tk.Button(button_frame, text="Copy")
copy_button.pack(side='left', padx=10)

# Create the 'Enter' button
enter_button = tk.Button(button_frame, text="Enter")
enter_button.pack(side='left', padx=10)


def on_enter():
    for box in reversed(boxes):
       boxes.remove(box)
    data = {item: entry.get() for item, entry in entries.items()}
    box_builder(data)

def string_builder(boxes):
    out = []
    for box in boxes:
        for template in templates:
            if box.template == template.template:
                outstring = f'{box.template}\t{template.length}\t{template.width}\t{template.height}\tINCH\t{box.weight}\tLB\n'
                out.append(outstring)
    return '\n'.join(out)

def do_copy():
    root.update()
    root.clipboard_clear()
    root.clipboard_append(string_builder(boxes))
    root.update()
    for box in reversed(boxes):
       boxes.remove(box)


# Update the buttonsto call their respective functions
enter_button.config(command=on_enter)
copy_button.config(command=do_copy)



#Create a list of boxes from user input
def box_builder(data):
    for sku in data:
        for item in items:
            if item.item == sku and data[sku] != "":
                smallest_box = ""
                for box in item.boxes:
                    print(item.boxes[box])
                    if int(data[sku]) >= item.boxes[box]  and item.boxes[box] != 0:
                        smallest_box = sku
                        
                print(smallest_box)
                for key in reversed(list(item.boxes.keys())):
                    largest_box = 0
                    # if largest_box < 


                    if int(data[sku]) >= item.boxes[key] and item.boxes[key] != 0:
                        
                        new_box = Boxes(key, (item.weight * item.boxes[key]))
                        print(f'Box: {new_box.template} Weight: {new_box.weight}')
                        boxes.append(new_box)
                        data[sku] = int(data[sku]) - item.boxes[key]
                        if data[sku] == 0:
                            print(f'Total number of boxes: {len(boxes)}')
                            string_builder(boxes)
                            break
                        else:
                            box_builder(data)

# Run the application
root.mainloop()
