#importing the requiremets modules

from cProfile import label
from tkinter import*
from PIL import Image, ImageTk
import cv2


display = Tk()
display.geometry('700x550')
display.title('Web Camera')

label = Label(display)
label.grid(row=10, column=90)
cap = cv2.VideoCapture(0)


def open_camera():
    
    try:
        cv2image = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2RGB)
        
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        label.imgtk = imgtk
        label.configure(image = imgtk)
        label.after(20, open_camera)
        
    except Exception as e:
        print(e)

open_camera()


display.mainloop()