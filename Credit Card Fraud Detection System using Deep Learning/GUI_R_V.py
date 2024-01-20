import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from tkinter import messagebox as ms
from PIL import Image , ImageTk     
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 

##############################################+=============================================================

root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("GUI")


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('im5.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


#lbl = tk.Label(root, text="Credit Card Fraud Detection", font=('times', 40,' bold '), height=1, width=30,bg="Black",fg="indian red")
#lbl.place(x=330, y=5)

frame_alpr = tk.LabelFrame(root, text=" ", width=280, height=300, bd=5, font=('times', 15, ' bold ') )
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=50, y=300)

# frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
# frame_display.grid(row=0, column=0, sticky='nw')
# frame_display.place(x=330, y=100)
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 



# frame_display = tk.LabelFrame(root, text=" --Display-- ", width=700, height=550, bd=5, font=('times', 14, ' bold '),bg="#736AFF")
# frame_display.grid(row=0, column=0, sticky='nw')
# frame_display.place(x=330, y=100)


    
def registration():
    
##### tkinter window ######
    
    print("Registration")
    from subprocess import call
    call(["python", "registration.py"]) 



# def display():
    
# ##### tkinter window ######
    
#     print("Display")
#     from subprocess import call
#     call(["python", "display.py"]) 


    

   
    
def Test_database():
    flag=0
    recognizer = cv2.face.LBPHFaceRecognizer_create(1, 8, 8, 8, 100)
#    recognizer = cv2.face.FisherFaceRecognizer(0, 3000);
    
    recognizer.read('trainingdata.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    #iniciate id counter
    id = 0
    # names related to ids: example ==> Marcelo: id=1,  etc
    #names = ['None', 'Criminal person identified', 'Missing person', 'Criminal person identified', 'Criminal person identified', 'Missing person','Missing person'] 
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    while True:
        ret, img =cam.read()
#        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray,1.3,8,minSize = (int(minW), int(minH)))
#        faces = faceCascade.detectMultiScale( 
#            gray,
#            scaleFactor = 1.2,
#            minNeighbors = 5,
#            minSize = (int(minW), int(minH)),
#           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
            
            # If confidence is less them 100 ==> "0" : perfect match
            
            if (confidence < 50):
                #print(id)
                #name = names[id]
                id = id
                print(type(id))
                with open(r"id.txt", 'w') as f:
                  f.write(str(id))
                #name = names[id]
                #id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                
                         
                #cv2.putText(img,str(name),(x+5,y-5),font,1,(255,255,255),2)
                cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                # my_conn = sqlite3.connect('evaluation.db')
                # r_set=my_conn.execute("select * from registration where id =" + str(id) +"");
                cv2.putText(img,"Person Identified"+str(id),(x+5,y-5),font,1,(255,255,255),2)
                ms.showinfo('Success!', 'Person Identified Successfully !')
                # l1 = tk.Label(root, text="!!! ...Person Identified Successfully... !!!", font=("Times new roman", 30, "bold"), bg="Black", fg="white")
                # l1.place(x=400, y=450)
                root.destroy()
                from subprocess import call
                call(["python", "credit_verify.py"])   
                
           
                
                
                
          
                
            else:
#                print(confidence)
                 id = "unknown Person Identified"
                 confidence = "  {0}%".format(round(100 - confidence))
                
                 cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
                 cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)
                # ms.showinfo('Success!', 'Fraud Person Identified Successfully !')
                 l1 = tk.Label(root, text="Try again!", font=("Verdana", 30, "bold"), bg="Black", fg="white")
                 l1.place(x=200, y=450)
            
       

#        time.sleep(0.2)
        cv2.imshow('camera',img)

#        print(flag)
        if flag==10:
            flag=0
            cam.release()
            cv2.destroyAllWindows()

           
     
        # k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#        if k == 27:
#            break
        if cv2.waitKey(1) == ord('Q'):
            break
        #ms.showinfo("Person Identified","Person Identified Successfully !!")

    cam.release()
    cv2.destroyAllWindows()
        
        
# def ID():     
#     my_conn = sqlite3.connect('evaluation.db')
#     r_set=my_conn.execute("SELECT * FROM registration")
#     i=0 # row value inside the loop 
#     for student in r_set: 
#         for j in range(len(student)):
#             e =tk.Entry(root, width=10, fg='blue') 
#             e.grid(row=i, column=j) 
#             e.insert(END, student[j])
#         i=i+1
        
        
        
            
    


#################################################################################################################
def window():
    root.destroy()



# button1 = tk.Button(frame_alpr, text="Create Face Data", command=Create_database,width=15, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
# button1.place(x=10, y=100)

# button2 = tk.Button(frame_alpr, text="Train Face Data", command=Train_database, width=20, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
# button2.place(x=10, y=160)

button3 = tk.Button(frame_alpr, text="Face Verification", command=Test_database, width=20, height=1, font=('verdana', 12, ' bold '),bg="dark slate gray",fg="white")
button3.place(x=12, y=80)



# button4 = tk.Button(frame_alpr, text="Display All Records", command=ID,width=20, height=1,bg="yellow4",fg="white", font=('times', 15, ' bold '))
# button4.place(x=10, y=160)
# ##



exit = tk.Button(frame_alpr, text="Exit", command=window, width=20, height=1, font=('verdana', 12, ' bold '),bg="red",fg="white")
exit.place(x=12, y=200)



root.mainloop()