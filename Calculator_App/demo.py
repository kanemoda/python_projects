from tkinter import *

root = Tk()
display = Entry(root)
display.grid(row=1 , columnspan=6)

counter = 1
for x in range(3):
    for y in range(3):
        button = Button(root , text = counter , width=3 , height=3)
        button.grid(row=x+2 , column=y)
        counter+=1

button = Button(root , text="0" , height=2 , width=2)
button.grid(row=5 , column=1)

operations = ["+" , "-" , "*" , "/" , "*3.14" , "%" , "(" , "**" ,")" , "**2"]

count = 0
for i in range(4):
    for j in range(3):
        if count < len(operations):
            button = Button(root , text= operations[count] , width=3 , height=3)
            count += 1
            button.grid(row=i+2 , column=j + 6)
root.mainloop()
