# This is a program to create and menage a list of tasks

#Simple Checklist
from operator import length_hint
import tkinter
from tkinter.font import BOLD
from tkinter import END, ANCHOR

# Define window
root = tkinter.Tk()
root.title(" Simple Checklist")
root.iconbitmap("check.ico")
root.geometry("400x400")
root.resizable(0,0)

# Define colors and fonts
root_bg = "#8823eb"
my_font = ("Times New Roman", 12 , BOLD)
button_color = "#e2cff4"
root.config(bg = root_bg)

# Define functions
def add_item():
    """Add an individual item to the listbox"""
    added_item = str(input_field.get())
    my_listbox.insert(END,str(added_item))
    input_field.delete(0, END)

def remove_item():
    """Remove the selected (ANCHOR) item from the listbox"""
    my_listbox.delete(ANCHOR)

def clear_list():
    """Delete all items from the listbox"""
    my_listbox.delete(0,END)

def save_list():
    """Save the list to a simple txt file"""
    with open('checklist.txt', 'w') as f:
        list_tuple = my_listbox.get(0,END)
        for item in list_tuple:
            if item.endswith("\n"):
                f.write(item)
            else:
                f.write(item + "\n")

def open_list():
    """Open the list upon starting the program if there is one"""
    try:
        with open("checklist.txt", "r") as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return


# Define layout - układ | field - pole

# Define frames - ramki
input_frame = tkinter.Frame(root, bg= root_bg)
output_frame = tkinter.Frame(root, bg= root_bg)
button_frame = tkinter.Frame(root, bg = root_bg)

input_frame.pack()
output_frame.pack()
button_frame.pack()

# Define input_frame layout
input_field = tkinter.Entry(input_frame, width= 35, font = my_font, borderwidth=3)
add_button = tkinter.Button(input_frame, text = "Add Item", font = my_font, bg = button_color, borderwidth=2, command=add_item)

input_field.grid(row=0,column=0, padx = 10, pady = 10)
add_button.grid(row=0,column=1)

# Define output_frame layout
my_scrollbar = tkinter.Scrollbar(output_frame, bg = button_color)
my_listbox = tkinter.Listbox(output_frame, height= 15, width= 47, borderwidth= 3, font = my_font, yscrollcommand=my_scrollbar.set)
# Link scroolbar to listbox
my_scrollbar.config(command=my_listbox.yview)

my_scrollbar.grid(row=0,column=1, sticky="NS")
my_listbox.grid(row=0,column=0)



# Define button_frame layout
list_remove_button = tkinter.Button(button_frame, text = "Remove Item", borderwidth= 2, font= my_font, bg = button_color, command= remove_item)
list_clear_button = tkinter.Button(button_frame, text = "Clear List", borderwidth= 2, font= my_font, bg = button_color, command=clear_list)
save_button = tkinter.Button(button_frame, text = "Save List", borderwidth= 2, font= my_font, bg = button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text = "Quit", borderwidth= 2, font= my_font, bg = button_color, command=root.destroy)

list_remove_button.grid(row=0,column=0,padx=6,pady=7)
list_clear_button.grid(row=0,column=1,padx=6,pady=7)
save_button.grid(row=0,column=2,padx=6,pady=7)
quit_button.grid(row=0,column=3,padx=6,pady=7, ipadx=20)


# Open list if avialiable
open_list()

# Root main loop
root.mainloop()