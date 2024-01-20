

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("GUI")
#------------------Frame----------------------
image2 =Image.open('im4.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


def window():
    root.destroy()
    from subprocess import call
    call(["python", "gui_main.py"])   

    

l1 = tk.Label(root, text="Person Identified Successfully !", font=("Verdana", 30, "bold"), bg="Black", fg="white")
l1.place(x=350, y=50)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=300, height=280, bd=5, font=('times', 14, ' bold '),bg="grey")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=600, y=300)
# #++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
# button1 = tk.Button(framed, text='Person Registration',width=15,bd=5,height=2,bg='dark blue',fg='white',command=reg,font='bold').place(x=80,y=30)
# button1 = tk.Button(framed, text='Person Verification',width=15,bd=5,height=2,bg='dark blue',fg='white',command=c,font='bold').place(x=80,y=100)


exit = tk.Button(root, text="Exit", command=window, width=15, bd=5,height=2, font=' bold ',bg="red",fg="white")
exit.place(x=80, y=650)

root.mainloop()
