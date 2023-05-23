from tkinter import*
from PIL import ImageTk,Image
import random
from tkinter import messagebox


root = Tk()
root.title('Rock-Scissors-Paper')
root.geometry('650x550')

imgpaper = ImageTk.PhotoImage(Image.open('paper1.JPG'))
imgscissor = ImageTk.PhotoImage(Image.open('scissor1.JPG'))
imgstone = ImageTk.PhotoImage(Image.open('rock1.JPG'))
imgerot = ImageTk.PhotoImage(Image.open('erot2.png'))
imgrsp = ImageTk.PhotoImage(Image.open('r-s-p-2.JPG'))
imgbg = ImageTk.PhotoImage(Image.open('bg.JPG'))
imgscore = ImageTk.PhotoImage(Image.open('score.JPG'))
imgplayer = ImageTk.PhotoImage(Image.open('player.JPG'))
imgcomputer = ImageTk.PhotoImage(Image.open('computer.JPG'))

lb0 = Label(root, image=imgbg)
lb0.place(x=0,y=0)


lbtitle = Label( image=imgrsp)
lbtitle.grid(row=0,column=0, columnspan=3)

fr1 = Frame(root)
fr1.grid(row=2, column=0)

fr2 = Frame(root)
fr2.grid(row=2, column=2)

fr3 = Frame(root)
fr3.grid(row=3, column=0)

fr4 = Frame(root)
fr4.grid(row=3, column=2)

fr5 = Frame(root)
fr5.grid(row=2, column=1)

lbplayer = Label(root, padx=20, pady=10, image=imgplayer, font=('Comic Sans',15))
lbplayer.grid(row=1, column=0)

lbversus= Label(root, text='Vs',font=('Comic Sans',15))
lbversus.grid(row=1, column=1)

lbpc = Label(root, padx=20, pady=10, image=imgcomputer, font=('Comic Sans',15))
lbpc.grid(row=1, column=2)


lbscore = Label (fr5, padx=10, pady=10, image=imgscore, font=('Comic Sans',15))
lbscore.grid(row=4, column=0,columnspan=3)

lbpl_point = Label(fr5, text=0,  font=('Comic Sans',15))
lbpl_point.grid(row=5, column=0)

lbpc_point = Label(fr5, text=0,  font=('Comic Sans',15))
lbpc_point.grid(row=5, column=2)

def clck(x11):
    global x1,x2
    if x11==0:
        lb1.config(image=imgpaper)
    elif x11==1:
        lb1.config(image=imgscissor)
    else:
        lb1.config(image=imgstone)

    x1 = x11
    list = [0, 1, 2]
    y = random.choice(list)

    if y == 0:
        lb2.config(image=imgpaper)
    elif y == 1:
        lb2.config(image=imgscissor)
    else:
        lb2.config(image=imgstone)

    x2 = y
    score(x1, x2)

def score(x1,x2):
    global rpl, rpc
    if x1 == 0 and x2 == 2:
        rpl += 1

    if x1 == 1 and x2 == 0:
        rpl += 1

    if x1 == 2 and x2 == 1:
        rpl += 1

    if x2 == 0 and x1 == 2:
        rpc += 1

    if x2 == 1 and x1 == 0:
        rpc += 1

    if x2 == 2 and x1 == 1:
        rpc += 1

    lbpl_point['text'] = rpl
    lbpc_point['text'] = rpc

    if rpl > rpc:
        lbpl_point['bg'] = 'yellow'
        lbpc_point['bg'] = 'white'
    elif rpc > rpl:
        lbpc_point['bg'] = 'yellow'
        lbpl_point['bg'] = 'white'
    else:
        lbpc_point['bg'] = 'white'
        lbpl_point['bg'] = 'white'


    if rpl ==5 :
        messagebox.showinfo(title='message', message='Player Won!')

    if rpc ==5 :
        messagebox.showinfo(title='message', message='Computer Won!')


def rest():
    global rpl, rpc
    rpl = 0
    rpc = 0
    lbpl_point['text'] = rpl
    lbpc_point['text'] = rpc
    lbpc_point['bg'] = 'white'
    lbpl_point['bg'] = 'white'
    lb1.config(image=imgerot)
    lb2.config(image=imgerot)
    messagebox.showinfo(title='message', message='Winner at 5 !')


def round():
    lb1.config(image=imgerot)
    lb2.config(image=imgerot)

#highlightbackground="blue", highlightthickness=2
lb1 = Label(fr1,width=200, height=270)
lb1.grid(row=0,column=0)

lb2 = Label(fr2,text="?",width=200, height=270)
lb2.grid(row=0,column=0)

btpaper = Button(fr3, text='Paper', font=('Comic Sans',15), borderwidth=5, relief="raised", command= lambda x=0: clck(x))
btpaper.grid(row=0, column=0)

btscissor = Button(fr3, text='Scissors',  font=('Comic Sans',15), borderwidth=5, relief="raised",command = lambda x=1: clck(x))
btscissor.grid(row=0, column=1)

btstone = Button(fr3, text='Rock' , font=('Comic Sans',15), borderwidth=5, relief="raised",command = lambda x=2: clck(x))
btstone.grid(row=0, column=2)

btrst = Button(root, bg='cyan', padx=15, pady=5, text='New Round', font=('Comic Sans',15), borderwidth=5, relief="raised", command = round)
btrst.grid(row=9, column=0)

btrstnew = Button(root, bg='orange', padx=15, pady=5, text='New Game', font=('Comic Sans',15), borderwidth=5, relief="raised", command = rest)
btrstnew.grid(row=9, column=2)

rest()
root.mainloop()