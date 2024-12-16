from tkinter import *

root = Tk()

x = 0

def get_number(num):
    global x
    display.insert(x,num)
    x += 1



def get_operation(op):
    global x
    length = len(op)
    display.insert(x,op)
    x += length

def clear_all():
    display.delete(0,END)
    x = 0
    






display = Entry(root)
display.grid(row=1 , columnspan=6)

numbers = [1,2,3,4,5,6,7,8,9]

counter = 0
for i in range(3):
    for j in range(3):
        button_text = numbers[counter]
        button = Button(root , text = button_text , width=3 , height=3 , command=lambda text = button_text:get_number(text))
        button.grid(row=i+2 , column=j)
        counter+=1

button = Button(root , text="0" , height=3 , width=3 , command=lambda:get_number(0))
button.grid(row=5 , column=1)

operations = ["+" , "-" , "*" , "/" , "*3.14" , "%" , "(" , "**" ,")" , "**2"]

count = 0
for i in range(4):
    for j in range(3):
        if count < len(operations):
            op = operations[count]
            button = Button(root , text= op , width=3 , height=3  ,command= lambda text = op:get_operation(text))
            count += 1
            button.grid(row=i+2 , column=j + 6)

Button(root , text="AC" , width=3 , height=3 , command=lambda:clear_all()).grid(row = 5 , column=0)
Button(root , text="=" , width=3 , height=3).grid(row = 5 , column=2)


root.mainloop()
