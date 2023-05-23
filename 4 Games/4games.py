from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title('Python Game')

bt = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

imgblack = ImageTk.PhotoImage(Image.open('black1.jpg'))
imgred = ImageTk.PhotoImage(Image.open('red.jpg'))
imgyellow = ImageTk.PhotoImage(Image.open('yellow.jpg'))
img1 = ImageTk.PhotoImage(Image.open('1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('5.jpg'))
img6 = ImageTk.PhotoImage(Image.open('6.jpg'))
img7 = ImageTk.PhotoImage(Image.open('7.jpg'))
imgredpl = ImageTk.PhotoImage(Image.open('redpl1.jpg'))
imgyellowpl = ImageTk.PhotoImage(Image.open('yellowpl1.jpg'))
imggor = ImageTk.PhotoImage(Image.open('gor1.jpg'))
imggol = ImageTk.PhotoImage(Image.open('gol1.jpg'))

fr1 = Frame(root)
fr1.grid(row=1, column=1)

fr2 = Frame(root)
fr2.grid(row=3, column=1)

fr3 = Frame(root)
fr3.grid(row=2, column=1)

lb1 = Label(fr2, bg='black')
lb1.grid(row=0, column=0)

fr4 = Frame(root)
fr4.grid(row=6, column=1)

lbcol = Label(fr3, text='Choose a column', font=('Comic Sans', 20))
lbcol.grid(row=0, column=0, columnspan=3)

lbredpl = Label(fr2, image=imgredpl)
lbredpl.grid(row=0,column=0)

lbscorered = Label(fr2, text=0, bg='red', font=('Comic Sans',15))
lbscorered.grid(row=0, column=0)

lbchoice = Label(fr2, image=imggor)
lbchoice.grid(row=0,column=1)
lbchoice1 = Label(fr2, text='GO!', bg='yellow', font=('Comic Sans',15))
lbchoice1.grid(row=0, column=1)

lbyellowpl = Label(fr2, image=imgyellowpl)
lbyellowpl.grid(row=0,column=2)

lbscoryel = Label(fr2, text=0, bg='yellow', font=('Comic Sans',15))
lbscoryel.grid(row=0, column=2)

def winner(r,c, col):
    global rred, ryel
    if r<=2:
        if bt[r][c]['image'] == col and bt[r+1][c]['image'] == col and bt[r+2][c]['image'] == col and bt[r+3][c]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
    else:
        if bt[r][c]['image'] == col and bt[r-1][c]['image'] == col and bt[r-2][c]['image'] == col and bt[r-3][c]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')

    if c<=2:
        if bt[r][c]['image'] == col and bt[r][c+1]['image'] == col and bt[r][c+2]['image'] == col and bt[r][c+3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
    elif c>=4:
        if bt[r][c]['image'] == col and bt[r][c-1]['image'] == col and bt[r][c-2]['image'] == col and bt[r][c-3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
    else:
        if bt[r][c]['image'] == col and bt[r][c+1]['image'] == col and bt[r][c+2]['image'] == col and bt[r][c+3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
        if bt[r][c]['image'] == col and bt[r][c - 1]['image'] == col and bt[r][c - 2]['image'] == col and bt[r][c - 3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')

    if r<=2 and c<=3:
        if bt[r][c]['image'] == col and bt[r+1][c+1]['image'] == col and bt[r+2][c+2]['image'] == col and bt[r+3][c+3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
    if r<=2 and c>=3:
        if bt[r][c]['image'] == col and bt[r+1][c-1]['image'] == col and bt[r+2][c-2]['image'] == col and bt[r+3][c-3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')

    if r>=3 and c<=3:
        if bt[r][c]['image'] == col and bt[r-1][c+1]['image'] == col and bt[r-2][c+2]['image'] == col and bt[r-3][c+3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')
    if r>=3 and c>=3:
        if bt[r][c]['image'] == col and bt[r-1][c-1]['image'] == col and bt[r-2][c-2]['image'] == col and bt[r-3][c-3]['image'] == col:
            if col == colred:
                rred += 1
                lbscorered['text'] = rred
            else:
                ryel += 1
                lbscoryel['text'] = ryel
            #messagebox.showinfo(title='Message', message='Bravo!')

    closewin()

def closewin():
    p = 0
    for row in range(6):
        for col in range(7):
            if bt[row][col]['image'] == colour:
                p += 1
    if p==0:
        if rred > ryel:
            messagebox.showinfo(title='Message', message='Red WON')
        elif rred < ryel:
            messagebox.showinfo(title='Message', message='Yellows WON')
        else:
            messagebox.showinfo(title='Message', message='Tie')

def click(r,c):
    global flag, colyel, colred

    if flag == True:

        row = 5
        while True:
            if bt[row][c]['image'] == colour:
                bt[row][c]['image']= imgyellow
                colyel = bt[row][c]['image']
                winner(row,c, colyel)
                break
            else:
                row -=1
                if row == -1:
                    break

        lbchoice['image']=imggol
        lbchoice1['bg']='red'
        flag = False
    else:

        row = 5
        while True:
            if bt[row][c]['image'] == colour:
                bt[row][c]['image'] = imgred
                colred = bt[row][c]['image']
                winner(row, c, colred)
                break
            else:
                row -= 1
                if row == -1:
                    break
        lbchoice['image']=imggor
        lbchoice1['bg']='yellow'
        flag = True

def reset():
    global flag, colour, rred, ryel
    rred = 0
    ryel = 0
    lbscorered['text'] = rred
    lbscoryel['text'] = ryel
    flag =True
    bt[0][0] = Button(fr1, image=imgblack, command= lambda row=0, column=0: click(row,column))
    bt[0][1] = Button(fr1, image=imgblack, command= lambda row=0, column=1: click(row,column))
    bt[0][2] = Button(fr1, image=imgblack, command= lambda row=0, column=2: click(row,column))
    bt[0][3] = Button(fr1, image=imgblack, command= lambda row=0, column=3: click(row,column))
    bt[0][4] = Button(fr1, image=imgblack, command= lambda row=0, column=4: click(row,column))
    bt[0][5] = Button(fr1, image=imgblack, command= lambda row=0, column=5: click(row,column))
    bt[0][6] = Button(fr1, image=imgblack, command= lambda row=0, column=6: click(row,column))

    bt[0][0].grid(row=0, column=0)
    bt[0][1].grid(row=0, column=1)
    bt[0][2].grid(row=0, column=2)
    bt[0][3].grid(row=0, column=3)
    bt[0][4].grid(row=0, column=4)
    bt[0][5].grid(row=0, column=5)
    bt[0][6].grid(row=0, column=6)

    bt[1][0] = Button(fr1, image=imgblack, command= lambda row=1, column=0: click(row,column))
    bt[1][1] = Button(fr1, image=imgblack, command= lambda row=1, column=1: click(row,column))
    bt[1][2] = Button(fr1, image=imgblack, command= lambda row=1, column=2: click(row,column))
    bt[1][3] = Button(fr1, image=imgblack, command= lambda row=1, column=3: click(row,column))
    bt[1][4] = Button(fr1, image=imgblack, command= lambda row=1, column=4: click(row,column))
    bt[1][5] = Button(fr1, image=imgblack, command= lambda row=1, column=5: click(row,column))
    bt[1][6] = Button(fr1, image=imgblack, command= lambda row=1, column=6: click(row,column))

    bt[1][0].grid(row=1, column=0)
    bt[1][1].grid(row=1, column=1)
    bt[1][2].grid(row=1, column=2)
    bt[1][3].grid(row=1, column=3)
    bt[1][4].grid(row=1, column=4)
    bt[1][5].grid(row=1, column=5)
    bt[1][6].grid(row=1, column=6)

    bt[2][0] = Button(fr1, image=imgblack, command= lambda row=2, column=0: click(row,column))
    bt[2][1] = Button(fr1, image=imgblack, command= lambda row=2, column=1: click(row,column))
    bt[2][2] = Button(fr1, image=imgblack, command= lambda row=2, column=2: click(row,column))
    bt[2][3] = Button(fr1, image=imgblack, command= lambda row=2, column=3: click(row,column))
    bt[2][4] = Button(fr1, image=imgblack, command= lambda row=2, column=4: click(row,column))
    bt[2][5] = Button(fr1, image=imgblack, command= lambda row=2, column=5: click(row,column))
    bt[2][6] = Button(fr1, image=imgblack, command= lambda row=2, column=6: click(row,column))

    bt[2][0].grid(row=2, column=0)
    bt[2][1].grid(row=2, column=1)
    bt[2][2].grid(row=2, column=2)
    bt[2][3].grid(row=2, column=3)
    bt[2][4].grid(row=2, column=4)
    bt[2][5].grid(row=2, column=5)
    bt[2][6].grid(row=2, column=6)

    bt[3][0] = Button(fr1, image=imgblack, command= lambda row=3, column=0: click(row,column))
    bt[3][1] = Button(fr1, image=imgblack, command= lambda row=3, column=1: click(row,column))
    bt[3][2] = Button(fr1, image=imgblack, command= lambda row=3, column=2: click(row,column))
    bt[3][3] = Button(fr1, image=imgblack, command= lambda row=3, column=3: click(row,column))
    bt[3][4] = Button(fr1, image=imgblack, command= lambda row=3, column=4: click(row,column))
    bt[3][5] = Button(fr1, image=imgblack, command= lambda row=3, column=5: click(row,column))
    bt[3][6] = Button(fr1, image=imgblack, command= lambda row=3, column=6: click(row,column))

    bt[3][0].grid(row=3, column=0)
    bt[3][1].grid(row=3, column=1)
    bt[3][2].grid(row=3, column=2)
    bt[3][3].grid(row=3, column=3)
    bt[3][4].grid(row=3, column=4)
    bt[3][5].grid(row=3, column=5)
    bt[3][6].grid(row=3, column=6)

    bt[4][0] = Button(fr1, image=imgblack, command= lambda row=4, column=0: click(row,column))
    bt[4][1] = Button(fr1, image=imgblack, command= lambda row=4, column=1: click(row,column))
    bt[4][2] = Button(fr1, image=imgblack, command= lambda row=4, column=2: click(row,column))
    bt[4][3] = Button(fr1, image=imgblack, command= lambda row=4, column=3: click(row,column))
    bt[4][4] = Button(fr1, image=imgblack, command= lambda row=4, column=4: click(row,column))
    bt[4][5] = Button(fr1, image=imgblack, command= lambda row=4, column=5: click(row,column))
    bt[4][6] = Button(fr1, image=imgblack, command= lambda row=4, column=6: click(row,column))

    bt[4][0].grid(row=4, column=0)
    bt[4][1].grid(row=4, column=1)
    bt[4][2].grid(row=4, column=2)
    bt[4][3].grid(row=4, column=3)
    bt[4][4].grid(row=4, column=4)
    bt[4][5].grid(row=4, column=5)
    bt[4][6].grid(row=4, column=6)

    bt[5][0] = Button(fr1, image=imgblack, command= lambda row=5, column=0: click(row,column))
    bt[5][1] = Button(fr1, image=imgblack, command= lambda row=5, column=1: click(row,column))
    bt[5][2] = Button(fr1, image=imgblack, command= lambda row=5, column=2: click(row,column))
    bt[5][3] = Button(fr1, image=imgblack, command= lambda row=5, column=3: click(row,column))
    bt[5][4] = Button(fr1, image=imgblack, command= lambda row=5, column=4: click(row,column))
    bt[5][5] = Button(fr1, image=imgblack, command= lambda row=5, column=5: click(row,column))
    bt[5][6] = Button(fr1, image=imgblack, command= lambda row=5, column=6: click(row,column))

    bt[5][0].grid(row=5, column=0)
    bt[5][1].grid(row=5, column=1)
    bt[5][2].grid(row=5, column=2)
    bt[5][3].grid(row=5, column=3)
    bt[5][4].grid(row=5, column=4)
    bt[5][5].grid(row=5, column=5)
    bt[5][6].grid(row=5, column=6)

    lb60 = Label(fr1, image=img1)
    lb60.grid(row=6, column=0)
    lb61 = Label(fr1, image=img2)
    lb61.grid(row=6, column=1)
    lb62 = Label(fr1, image=img3)
    lb62.grid(row=6, column=2)
    lb63 = Label(fr1, image=img4)
    lb63.grid(row=6, column=3)
    lb64 = Label(fr1, image=img5)
    lb64.grid(row=6, column=4)
    lb65 = Label(fr1, image=img6)
    lb65.grid(row=6, column=5)
    lb66 = Label(fr1, image=img7)
    lb66.grid(row=6, column=6)

    colour = bt[5][6]['image']
    print(bt[5][6]['image'])
    lbchoice['image']=imggor
    lbchoice1['bg']= 'yellow'


btreset = Button(fr4, text='reset',bg='magenta', font=('Comic Sans',15),  command= reset)
btreset.grid(row=0, column=0)

reset()
root.mainloop()