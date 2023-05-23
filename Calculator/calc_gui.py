from tkinter import*
from tkinter import messagebox


root = Tk()
root.title('Calculator')

bt= [
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' ',' '],
]

en1 = Entry(root, width=50, borderwidth=5)
en1.grid(row=0, column=0, columnspan=3)
en1.insert(0, ' ')

fr1 = Frame(root)
fr1.grid(row=2,column=1)

def clck(r):
    global p,flag
    if flag == False:
        cur = en1.get()
        en1.delete(0,END)
        en1.insert(0, str(cur)+str(r))
    else:
        if p==0:
            en1.delete(0, END)
            p += 1
            en1.insert(0, str(r))
        else:
            cur = en1.get()
            en1.delete(0, END)
            en1.insert(0, str(cur) + str(r))

def clckdiv():
    global first, math, flag, p
    first = en1.get()
    first = float(first)
    math = '/'
    en1.delete(0, END)
    en1.insert(0, str(first) + math)
    flag = True
    p = 0


def clckadd():
    global first ,math, flag,p
    first = en1.get()
    first = float(first)
    math = '+'
    en1.delete(0,END)
    en1.insert(0, str(first)+math)
    flag = True
    p=0

def clcksub():
    global first, math, flag, p
    first = en1.get()
    first = float(first)
    math = '-'
    en1.delete(0, END)
    en1.insert(0, str(first) + math)
    flag = True
    p = 0

def clckmult():
    global first, math, flag, p
    first = en1.get()
    first = float(first)
    math = '*'
    en1.delete(0, END)
    en1.insert(0, str(first) + math)
    flag = True
    p = 0


def clckres():
    second = en1.get()
    second = float(second)
    en1.delete(0,END)

    if math == '+':
        en1.insert(0,str(first + second))
    elif math == '-':
        k = first - second
        en1.insert(0,str(k))
    elif math == '*':
        en1.insert(0,'{:.2f}'.format(first * second))
    else:
        if second != 0:
            k = float(first / second)
            en1.insert(0, str('{:.2f}'.format(k)))
        else:
            en1.insert(0, 'no result')


def clckclear():
    en1.delete(0,END)



flag = False
bt[0][0] = Button(fr1,padx=35, pady=10, text='7', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(7))
bt[0][1] = Button(fr1,padx=35, pady=10, text='8', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(8))
bt[0][2] = Button(fr1,padx=35, pady=10, text='9', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(9))
bt[0][3] = Button(fr1,padx=36, pady=10, text='/ ', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command=clckdiv)

bt[1][0] = Button(fr1,padx=35, pady=10, text='4', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(4))
bt[1][1] = Button(fr1,padx=35, pady=10, text='5', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(5))
bt[1][2] = Button(fr1,padx=35, pady=10, text='6', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(6))
bt[1][3] = Button(fr1,padx=35, pady=10, text='* ', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= clckmult)

bt[2][0] = Button(fr1,padx=35, pady=10, text='1', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(1))
bt[2][1] = Button(fr1,padx=35, pady=10, text='2', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(2))
bt[2][2] = Button(fr1,padx=35, pady=10, text='3', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(3))
bt[2][3] = Button(fr1,padx=38, pady=10, text='-', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= clcksub)

bt[3][0] = Button(fr1,padx=37, pady=10, text=',', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck('.'))
bt[3][1] = Button(fr1,padx=35, pady=10, text='0', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= lambda : clck(0))
bt[3][2] = Button(fr1,padx=81, pady=10, text='+', font=('Comic Sans',11, 'bold'), fg='white', bg='black', command= clckadd)

bt[4][0] = Button(fr1,padx=65, pady=10, text='Clear', font=('Comic Sans',11, 'bold'), fg='white', bg='lime', command= clckclear)
bt[4][2] = Button(fr1,padx=81, pady=10, text='=', font=('Comic Sans',11, 'bold'), fg='white', bg='blue', command= clckres)



bt[0][0].grid(row=0,column=0)
bt[0][1].grid(row=0,column=1)
bt[0][2].grid(row=0,column=2)
bt[0][3].grid(row=0,column=3)

bt[1][0].grid(row=1,column=0)
bt[1][1].grid(row=1,column=1)
bt[1][2].grid(row=1,column=2)
bt[1][3].grid(row=1,column=3)

bt[2][0].grid(row=2,column=0)
bt[2][1].grid(row=2,column=1)
bt[2][2].grid(row=2,column=2)
bt[2][3].grid(row=2,column=3)

bt[3][0].grid(row=3,column=0)
bt[3][1].grid(row=3,column=1)
bt[3][2].grid(row=3, column=2, columnspan=2)

bt[4][0].grid(row=4, column=0, columnspan=2)
bt[4][2].grid(row=4, column=2, columnspan=2)





root.mainloop()
