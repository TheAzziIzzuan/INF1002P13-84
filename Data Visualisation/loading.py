from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import subprocess

root = Tk()
root.title("Loading...")
image = PhotoImage(file="Images/loading.png")

height = 430
width = 530

x = (root.winfo_screenwidth() // 2) - (width // 2)              # Retrieves width of the screen where the window will be displayed & // 2 is to get the middle of the screen
y = (root.winfo_screenheight() // 2) - (height // 2)            # Retrieves height of the screen where the window will be displayed // 2 is to get the middle of the screen


root.geometry('{}x{}+{}+{}'.format(width, height, x, y))        # set the size of the window and the position of the window, width x height + x position + y position


root.configure(background='#ffffff')


progress_label = Label(root, text="Loading...", font=("Arial", 12, "bold"), bg='#ffffff', fg='black')
progress_label.place(x=210, y=270)

bg_label = Label(root, image=image, bg='#ffffff')
bg_label.place(x=155, y=30)

progress = ttk.Style()                                          #  provides methods and properties that allow you to customize various aspects of ttk widgets
progress.theme_use('alt')                                       #  set the theme to alt


progress = Progressbar(root, orient=HORIZONTAL, length = 400, mode='determinate', style='Horizontal.TProgressbar')
progress.place(x=65, y=300)

def top():
    subprocess.Popen(['python', 'Data Visualisation\main.py'])              # subprocess.popen is used to open a subprocess and execute commands and the list is the command to be executed - python tells the os to use the default python interpreter to execute main.py
    root.destroy()

i = 0

def load():
    global i 
    if i <= 100:                                        # 100 times, in this case 100%
        txt = "Loading..." + (str(1*i) + "%")           #display the percentage of 1*i
        progress_label.config(text=txt)                 #update the label
        progress_label.after(600, load)                 #call the function after 600ms
        progress['value'] = 1*i                         #update the progress bar, 1*i is the percentage
        i += 10                                         #increment i + 10                      
    else:
        top()



load()
root.resizable(False, False) # prevent resizing of window
root.mainloop() 