from tkinter import *

root = Tk()

x = 0

def get_number(num):
    global x
    display.insert(i,num)
    x += 1

def delete_number():
    global x
    if x > 0:
        display.delete(x - 1 , x)
        x -= 1

    






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

button = Button(root , text="0" , height=2 , width=2 , command=lambda:get_number(0))
button.grid(row=5 , column=1)

operations = ["+" , "-" , "*" , "/" , "*3.14" , "%" , "(" , "**" ,")" , "**2"]

count = 0
for i in range(4):
    for j in range(3):
        if count < len(operations):
            button = Button(root , text= operations[count] , width=3 , height=3)
            count += 1
            button.grid(row=i+2 , column=j + 6)
button = Button(root , text = "del" , width=3 , height=3 ,  command=delete_number)
button.grid(row= 5 , column= 8)
root.mainloop()
