from tkinter import *
import customtkinter
from tkinter.font import Font
from tkinter import filedialog
import pickle

def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)
def cross_item():
    my_list.itemconfig(my_list.curselection(),fg="#dedede")
    #rid of selection bar
    my_list.selection_clear(0,END)
def uncross_item():
    my_list.itemconfig(my_list.curselection(), fg="#464646")

    my_list.selection_clear(0,END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))

        else:
            count+=1

def save_list():
    file_name = filedialog.asksaveasfilename(initialdir="C:/GUI/data", title="Save File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'
        #delete crossed off items before saving
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))

            else:
                count+=1
    #get all stuff from list
    stuff = my_list.get(0,END)

    #open file
    output_file = open(file_name,'wb')

    #add stuff to file
    pickle.dump(stuff,output_file)

def open_list():
    file_name = filedialog.askopenfilename(initialdir="C:/GUI/data", title="Open File", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))
    if file_name:
        #delete currently opened list
        my_list.delete(0,END)

        #open file
        input_file = open(file_name, 'rb')
        
        #load data from the file
        stuff = pickle.load(input_file)

        # Output stuff to screen
        for item in stuff:
            my_list.insert(END, item)

def clear_list():
    my_list.delete(0,END)





#root
root = Tk()
root.title("To Do List")
root.geometry("500x500")

#Define Font
my_font = Font(family ="Comic Sans MS", size = 30, weight = "bold")

#Create Frame
frame = Frame(root)
frame.pack(pady = 10)

#Create list box
my_list = Listbox(frame, font = my_font, width = 25, height = 5, bg = "SystemButtonFace", bd = 0, fg = "#464646", highlightthickness=0, selectbackground="#a6a6a6", activestyle= "none" )

my_list.pack(side=LEFT, fill=BOTH)

#create dummy list
#stuff = ["do one task", "do another task", "Another one"]

#add dummy list to list box
#for item in stuff:
#    my_list.insert(END,item)

#create scrollbar
my_scrollbar = Scrollbar(frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

#Add scroll bar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Create entery box

my_entry = Entry(root, font=("Helvetica",24),width=24 )
my_entry.pack(pady=20)

#Buttom Frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#add some buttons
delete_button = Button(button_frame, text = "Delete Item", command=delete_item)
add_button = Button(button_frame, text = "Add Item", command=add_item)
cross_button = Button(button_frame, text = "Cross off Item", command=cross_item)
uncross_button = Button(button_frame, text = "Uncross Item", command=uncross_item)
delcrossed_button = Button(button_frame, text = "Delete crossed Item", command=delete_crossed)
delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3,padx=20)
delcrossed_button.grid(row=0, column=4)

#Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add items to menu
file_menu = Menu(my_menu, tearoff= False)
my_menu.add_cascade(label="File",menu=file_menu)

#dropdown items
file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Clear List", command=clear_list)

root.mainloop()