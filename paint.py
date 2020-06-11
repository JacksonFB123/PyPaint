from tkinter import *
from tkinter import messagebox as mbox
import turtle, time
version = '1.0'
canvas = turtle.Pen()
tk = Tk()
def _info(): 
    newWindow = Toplevel(tk) 
    newWindow.title("PyPaint Info")  
    newWindow.geometry("400x100") 
    Label(newWindow, text ='''- PyPaint -
- Version '''+version+''' -
- Made by Jackson Baker in 2020 -
A GUI Baced Painting Application written in Python using Tkinter.
For more info go to https://github.com/ and search "PyPaint".
(Just so you know, this program is in it's beta testing ''').pack()
def _forward():
    canvas.forward(10)
def _back():
    canvas.back(10)
def _left():
    canvas.left(45)
def _right():
    canvas.right(45)
def _down():
    canvas.pendown()
def _up():
    canvas.penup()
def _clear():
    canvas.reset()
btn1 = Button(tk, text='Forward', command=_forward)
btn2 = Button(tk, text='Backward', command=_back)
btn3 = Button(tk, text='Left', command=_left)
btn4 = Button(tk, text='Right', command=_right)
btn5 = Button(tk, text='Pen On', command=_down)
btn6 = Button(tk, text='Pen Off', command=_up)
btn7 = Button(tk, text='Reset Canvas', command=_clear)
btn8 = Button(tk, text='Program Info', command=_info)
def packall():
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    btn6.pack()
    btn7.pack()
    btn8.pack()
packall()
mbox.showinfo('PyPaint v'+version, 'Welcome to PyPaint v'+version+'!')
