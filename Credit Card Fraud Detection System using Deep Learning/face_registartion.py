import tkinter as tk
#from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import cv2
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("800x700+300+30" )
root.title("Registration Form")
root.resizable(False,False)
# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('im1.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)





# frame_alpr = tk.LabelFrame(root, text=" --About us-- ", width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#7CCD7C")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=550, y=200)

# label_l2 = tk.Label(root, text="___ Registration Form ___",font=("Times New Roman", 30, 'bold'),
#                     background="black", fg="white", width=67, height=2)
# label_l2.place(x=0, y=90)


#frame_alpr = tk.LabelFrame(root, text=" --Register-- ", width=600, height=650, bd=5, font=('times', 14, ' bold '),fg="black",bg="grey")
#frame_alpr.grid(row=0, column=0, sticky='nw')
#frame_alpr.place(x=100, y=30)

######################### Registration form #####################################################################

Fulllname = tk.StringVar()
card_card = tk.IntVar()
Pin_no = tk.StringVar()
Address = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.StringVar()
# age = tk.IntVar()
Email = tk.StringVar()
#Gender = tk.StringVar()
otp = tk.IntVar()

# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT, password TEXT)")
db.commit()






def insert():
    fname = Fulllname.get()
    card = card_card.get()
    pin_no = Pin_no.get()
    add = Address.get()
    mobile = Phoneno.get()
    gender = var.get()
    email = Email.get()

    # with sqlite3.connect('evaluation.db') as db:
    #     c = db.cursor() 

    # # Find Existing username if any take proper action
    # find_user = ('SELECT * FROM user_reg WHERE Gender = ?')
    # c.execute(find_user, [(Voter_ID.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showinfo("Message", "please enter valid name")
    elif (card == ""):
        ms.showinfo("Message", "Please Enter Card No")
        
    elif (Pin_no == ""):
        ms.showinfo("Message", "Please Enter valid Pin No")
    elif (add == ""):
         ms.showinfo("Message", "Please Enter valid Address")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    
    elif (email == "") or (a == False):
            ms.showinfo("Message", "Please Enter valid email")
            
    
    elif (gender == False):
        ms.showinfo("Message", "Please Enter gender")
   
    
   
 
    else:
            conn = sqlite3.connect('evaluation.db')
            with conn:
                            cursor = conn.cursor()
                            cursor.execute(
                                'INSERT INTO user_reg(Fullname, Card_No, Pin_No, Address, Phone_No, Email_id, Gender) VALUES(?,?,?,?,?,?,?)',
                                (fname, card , pin_no, add, mobile, email, gender))

                            conn.commit()
                            db.close()
                            ms.showinfo('Success!', 'Account Created Successfully !')
                            root.destroy()
            
           


l1 = tk.Label(root, text="Registration Form", font=("verdana", 30, "bold"), bg="Black", fg="white")
l1.place(x=190, y=50)

# that is for label1 registration

l2 = tk.Label(root, text="Full Name :", width=12, font=("verdana", 15, "bold"), bg="snow")
l2.place(x=130, y=150)
t1 = tk.Entry(root, textvar=Fulllname, width=20, font=('', 15))
t1.place(x=330, y=150)
# that is for label 2 (full name)

l9 = tk.Label(root, text="Card No :", width=12, font=("verdana", 15, "bold"), bg="snow")
l9.place(x=130, y=200)
t9 = tk.Entry(root, textvar=card_card, width=20, font=('', 15))
t9.place(x=330, y=200)

l3 = tk.Label(root, text="Pin No :", width=12, font=("verdana", 15, "bold"), bg="snow")
l3.place(x=130, y=250)
t2 = tk.Entry(root, textvar=Pin_no,show="*", width=20, font=('', 15))
t2.place(x=330, y=250)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(root, text="Address :", width=12, font=("verdana", 15, "bold"), bg="snow")
l5.place(x=130, y=300)
t4 = tk.Entry(root, textvar=Address, width=20, font=('', 15))
t4.place(x=330, y=300)
# that is for email address


# phone number
l7 = tk.Label(root, text="Phone_No :", width=12, font=("verdana", 15, "bold"), bg="snow")
l7.place(x=130, y=350)
t6 = tk.Entry(root, textvar=Phoneno, width=20, font=('', 15))
t6.place(x=330, y=350)

l8 = tk.Label(root, text="Email:", width=12, font=("verdana", 15, "bold"), bg="snow")
l8.place(x=130, y=400)
t6 = tk.Entry(root, textvar=Email, width=20, font=('', 15))
t6.place(x=330, y=400)

l7 = tk.Label(root, text="Gender :", width=12, font=("verdana", 15, "bold"), bg="snow")
l7.place(x=130, y=450)
# gender
tk.Radiobutton(root, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value="Male").place(x=330,
                                                                                                                y=450)
tk.Radiobutton(root, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value="Female").place(
    x=450, y=450)


# l9 = tk.Label(window, text="Satate :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
# l9.place(x=130, y=500)
# t9 = tk.Entry(window, textvar=carno, width=20, font=('', 15), show="*")
# t9.place(x=330, y=500)

def Create_database():
            
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        cap = cv2.VideoCapture(0)
        
    #    id = input('enter user id')
        id=entry2.get()
        
        sampleN=0;
        
        while 1:
        
            ret, img = cap.read()
        
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        
            for (x,y,w,h) in faces:
        
                sampleN=sampleN+1;
        
                cv2.imwrite("faceData/User."+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
                cv2.waitKey(100)
        
            cv2.imshow('img',img)
        
            cv2.waitKey(1)
        
            if sampleN > 40:
        
                break
        
        cap.release()
        entry2.delete(0,'end')
        cv2.destroyAllWindows()
        root.destroy()
        from subprocess import call
        call(["python", "train.py"])
 
    
        
            
      
            

button1 = tk.Button(root, text="Create Face Data", command=Create_database,width=15, height=1, font=('verdana', 14, ' bold '),bg="dark slate gray",fg="white")
button1.place(x=130, y=600)
    
entry2=tk.Entry(root,bd=2,width=7)
entry2.place(x=350, y=610)
btn = tk.Button(root, text="Register", bg="red",font=("",16),fg="white", width=9, height=1, command=insert)
btn.place(x=260, y=520)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
root.mainloop()