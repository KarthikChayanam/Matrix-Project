from tkinter import *
import numpy as np


def clickme():

    global A
    A = np.array([[int(e11.get()),int(e12.get()),int(e13.get())],
        [int(e21.get()),int(e22.get()),int(e13.get())],
        [int(e31.get()),int(e32.get()),int(e33.get())]])

    mat = Label(root, text= A)
    mat.grid(row=5, column=1)

    print(A)


def sol_mat():
    
    X = np.linalg.solve(A,B)

    prr = Label(root, text=X)
    prr.grid(row=10,column=1)

    print(X)



def clickm2():

    global B
    B = np.array([int(b1.get()),int(b2.get()),int(b3.get())])

    mat1 = Label(root, text= B)
    mat1.grid(row=8, column=1)

    print(B)



root = Tk()

root.geometry("800x550")

intro = Label(root, text="Welcome to MY app")
intro.grid(row=0,column=1)

A = ([])
B = ([])


e11 = Entry(root)
e11.grid(row=1,column=0)

e12 = Entry(root)
e12.grid(row=1,column=1)

e13 = Entry(root)
e13.grid(row=1,column=2)

e21 = Entry(root)
e21.grid(row=2,column=0)

e22 = Entry(root)
e22.grid(row=2,column=1)

e23 = Entry(root)
e23.grid(row=2,column=2)

e31 = Entry(root)
e31.grid(row=3,column=0)

e32 = Entry(root)
e32.grid(row=3,column=1)

e33 = Entry(root)
e33.grid(row=3,column=2)


mybutton = Button(root, text="submit", command=clickme)
mybutton.grid(row=4,column=1)

b1 = Entry(root)
b1.grid(row=6,column=0)

b2 = Entry(root)
b2.grid(row=6,column=1)

b3 = Entry(root)
b3.grid(row=6,column=2)


solution = Button(root, text="submit2", command=clickm2)
solution.grid(row=7,column=1)

b_mat = Button(root, text="solution", command=sol_mat)
b_mat.grid(row=9,column=1)

root.mainloop()
