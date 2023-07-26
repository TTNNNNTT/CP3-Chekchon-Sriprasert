from tkinter import *
import math

def leftclickButton(event):
    BMI = float(boxweight.get())/math.pow(float(boxheight.get())/100,2,)
    if BMI>30:
        labalresult.configure(text="อ้วนมาก")
    elif BMI <= 29.9 and BMI >= 25.0:
        labalresult.configure(text="อ้วน")
    elif BMI <= 24.9 and BMI >= 23.0:
        labalresult.configure(text="น้ำหนักเกิน")
    elif BMI <= 22.9 and BMI >= 18.6:
        labalresult.configure(text="น้ำหนักปกติ เหมาะสม")
    else:
        labalresult.configure(text="ผอมเกินไป")

MainWindow = Tk()
Labelheight = Label(MainWindow,text="ความสูง (cm.)",font=('Tahoma',15)).grid(row=0,column=0)
Labelweight = Label(MainWindow,text="น้ำหนัก (kg)",font=('Tahoma',15)).grid(row=1,column=0)
boxheight = Entry(MainWindow)
boxheight.grid(row=0,column=1)
boxweight = Entry(MainWindow)
boxweight.grid(row=1,column=1)

calbutton = Button(MainWindow,text="คำนวณ",font=('Tahoma',12))
calbutton.grid(row=2,column=0)
calbutton.bind('<Button-1>',leftclickButton)

labalresult = Label(MainWindow,text="ผลลัพธ์",font=('Tahoma',12))
labalresult.grid(row=2,column=1)
MainWindow.mainloop()