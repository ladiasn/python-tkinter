from tkinter import*
from PIL import ImageTk,Image
import random
from tkinter import messagebox

root = Tk()
root.title('Memory Game')

img1 = ImageTk.PhotoImage(Image.open('aetos.jpg'))
img2 = ImageTk.PhotoImage(Image.open('alien.jpg'))
img3 = ImageTk.PhotoImage(Image.open('alien2.jpg'))
img4 = ImageTk.PhotoImage(Image.open('bird.jpg'))
img5 = ImageTk.PhotoImage(Image.open('careta.jpg'))
img6 = ImageTk.PhotoImage(Image.open('cat.jpg'))
img7 = ImageTk.PhotoImage(Image.open('dog.jpg'))
img8 = ImageTk.PhotoImage(Image.open('eleph.jpg'))
img9 = ImageTk.PhotoImage(Image.open('hippo.jpg'))
img10 = ImageTk.PhotoImage(Image.open('monk.jpg'))
img11 = ImageTk.PhotoImage(Image.open('snake.jpg'))
img12 = ImageTk.PhotoImage(Image.open('tiger.jpg'))
img13= ImageTk.PhotoImage(Image.open('seagreen.jpg'))
img14= ImageTk.PhotoImage(Image.open('memorycards.jpg'))


lb1 = Label(root, padx=10, pady=10, image=img14)
lb1.grid(row=0,column=0, columnspan=3)


lb2 = Label(root,text='Round: ', font=('Cambria',13))
lb2.grid(row=1,column=0, columnspan=3)


bt = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]

bt1 = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]

def check(firstbt, secondbt,r,c,fr,fc):
    global flag,p
    act()
    p=0
    firstbt.grid(row=fr, column=fc)
    secondbt.grid(row=r, column=c)
    button_close = Button(root, text='Close Cards', bg='silver', padx=10, pady=10)
    button_close.grid(row=1, column=2)
    flag = True


def disab():
    for r1 in range(4):
        for c1 in range(6):
            bt[r1][c1].config(state=DISABLED)
            bt1[r1][c1].config(state=DISABLED)

def act():
    for r1 in range(4):
        for c1 in range(6):
            bt[r1][c1].config(state=ACTIVE)
            bt1[r1][c1].config(state=ACTIVE)

def clse():
    button_close = Button(root, text='Close Cards', bg='silver', padx=10, pady=10, state=DISABLED)
    button_close.grid(row=1, column=2)

def act1():
    button_close = Button(root, text='Close Cards', bg='silver', padx=10, pady=10, state=ACTIVE)
    button_close.grid(row=1, column=2)


def click(r,c):
    global p, tries
    global first, second, firstbt, secondbt, fr, fc, win, flag, sr, sc
    if p == 0:
        clse()
        bt1[r][c].grid_forget()
        firstbt = bt1[r][c]
        first = bt[r][c]['image']
        fr = r
        fc = c
        p += 1
    elif p == 1:
        act1()
        tries += 1
        lb2 = Label(root, text='Round: ' + str(tries), font=('Cambria', 13))
        lb2.grid(row=1, column=0, columnspan=3)
        bt1[r][c].grid_forget()
        secondbt = bt1[r][c]
        sr = r
        sc = c
        second = bt[r][c]['image']
        p += 1
        if second != first:
            #p = 0
            #flag = False
            button_close = Button(root, text='Close Cards', bg='yellow', padx=10, pady=10, command=lambda: check(firstbt, secondbt, r, c, fr, fc))
            button_close.grid(row=1, column=2)
        else:
            p = 0
            flag = True
            win += 1
            firstbt.grid_forget()
            secondbt.grid_forget()
            if win == 12:
                messagebox.showinfo(title='Message', message='Bravo, You won!')
    else:
        disab()
        messagebox.showinfo(title='Message', message='Close your cards please')
        p = 0
        # flag = True
        button_close = Button(root, text='Close Cards', bg='yellow', padx=10, pady=10,
                              command=lambda: check(firstbt, secondbt, sr, sc, fr, fc))
        button_close.grid(row=1, column=2)





frm1 = Frame(root, padx=30, pady=30)
frm1.grid(row=3,column=0, columnspan=3)


def rest():
    global p, list, flag, win, tries, button_close
    tries = 0
    lb2 = Label(root, text='Round: ' + str(tries), font=('Cambria', 13))
    lb2.grid(row=1, column=0, columnspan=3)
    win = 0
    p = 0
    list = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11]
    flag = True
    button_close = Button(root, text='Close Cards', bg='silver',padx=10, pady=10)
    button_close.grid(row=1, column=2)
    for r in range(4):
        for c in range(6):
            x = random.choice(list)
            if x==0:
                bt[r][c] = Label(frm1, padx=74, pady=61, image=img1)
                bt[r][c].grid(row=r,column=c)
            elif x==1:
                bt[r][c] = Label(frm1, padx=74, pady=61, image=img2)
                bt[r][c].grid(row=r,column=c)
            elif x==2:
                bt[r][c] = Label(frm1, padx=74, pady=61, image=img3)
                bt[r][c].grid(row=r,column=c)
            elif x==3:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img4)
                bt[r][c].grid(row=r,column=c)
            elif x==4:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img5)
                bt[r][c].grid(row=r,column=c)
            elif x==5:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img6)
                bt[r][c].grid(row=r,column=c)
            elif x==6:
                bt[r][c] =  Label (frm1, padx=74, pady=61, image=img7)
                bt[r][c].grid(row=r,column=c)
            elif x==7:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img8)
                bt[r][c].grid(row=r,column=c)
            elif x==8:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img9)
                bt[r][c].grid(row=r,column=c)
            elif x==9:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img10)
                bt[r][c].grid(row=r,column=c)
            elif x==10:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img11)
                bt[r][c].grid(row=r,column=c)
            elif x==11:
                bt[r][c] = Label (frm1, padx=74, pady=61, image=img12)
                bt[r][c].grid(row=r,column=c)
            list.remove(x)

    for r in range(4):
        for c in range(6):
            bt1[r][c]= Button(frm1,padx=74, pady=61, image= img13, command=lambda row=r, column=c: click(row, column))
            bt1[r][c].grid(row=r, column=c)






button_reset = Button(root, text='New Game', bg='darkcyan', padx=10, pady=10,command=rest)
button_reset.grid(row=1, column=0)

rest()
root.mainloop()