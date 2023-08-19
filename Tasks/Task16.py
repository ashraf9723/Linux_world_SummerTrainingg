# Using Tkinter create a menubar

import tkinter as tk
from tkinter import messagebox

def on_about():
    messagebox.showinfo("About", "This is a simple menu example with 5 menus using Tkinter")

def on_exit():
    window.quit()

def on_menu1():
    messagebox.showinfo("Menu 1", "You clicked Menu 1")

def on_menu2():
    messagebox.showinfo("Menu 2", "You clicked Menu 2")

def on_menu3():
    messagebox.showinfo("Menu 3", "You clicked Menu 3")

def on_menu4():
    messagebox.showinfo("Menu 4", "You clicked Menu 4")

def on_menu5():
    messagebox.showinfo("Menu 5", "You clicked Menu 5")

# Create the main window
window = tk.Tk()
window.title("Python Menu Example")

# Create a menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create menus
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=on_exit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Menu 1", command=on_menu1)
edit_menu.add_command(label="Menu 2", command=on_menu2)

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Menu 3", command=on_menu3)

tools_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Menu 4", command=on_menu4)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Menu 5", command=on_menu5)
help_menu.add_command(label="About", command=on_about)

# Run the Tkinter event loop
window.mainloop()
