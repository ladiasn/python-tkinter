from tkinter import*
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title('Game')

bt = [
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 1, 1, 1, ' ', ' ',' '],
        [' ', ' ', ' ', 1, 1, 1, ' ', ' ',' '],
        [' ', 1, 1, 1, 1, 1, 1, 1, ' '],
        [' ', 1, 1, 1, 0, 1, 1, 1, ' '],
        [' ', 1, 1, 1, 1, 1, 1, 1, ' '],
        [' ', ' ', ' ', 1, 1, 1, ' ', ' ',' '],
        [' ', ' ', ' ', 1, 1, 1, ' ', ' ',' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    ]

img1 = ImageTk.PhotoImage(Image.open('img1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('img4.jpg'))

lb1 = Label(root, text='Peg Solitaire')
lb1.grid(row=0, column=0, columnspan=5)

frm1 = Frame(root)
frm1.grid(row=1, column=0, columnspan=5)

def check_finish():
    flag=False
    p =0
    for i in range(1,8):
        for j in range(1,8):
            if bt[i][j] ==0:
                p +=1
    flag1=False
    if p !=32:
        for i in range(1,8):
            for j in range(1,8):
                if bt[i][j]['image'] == f2:
                    if bt[i][j+1]['image']== f2 and bt[i][j+2]['image']== f1:
                        flag1=True
                    elif bt[i][j-1]['image']== f2 and bt[i][j-2]['image']== f1:
                        flag1=True
                    elif bt[i+1][j]['image']== f2 and bt[i+2][j]['image']== f1:
                        flag1=True
                    elif bt[i-1][j]['image']== f2 and bt[i-2][j]['image']== f1:
                        flag1=True

    else:
        flag=True

    if flag1==False:
        flag=True

    return flag


def disab():
        for r in range(1,3,1):
                for c in range(3,6,1):
                        bt[r][c].config(state=DISABLED)
        for r in range(3,6,1):
                for c in range(1,8,1):
                        bt[r][c].config(state=DISABLED)

        for r in range(6,8,1):
                for c in range(3,6,1):
                        bt[r][c].config(state=DISABLED)

def click(r,c):
        global p, fr, fc, sr, sc
        flag1 = False
        f = False
        if p == 0:
                if r == 2 and c == 4:
                        if bt[2][4]['image'] == f2 and bt[3][4]['image'] == f2 and bt[4][4]['image'] == f1:
                                flag1 = True
                elif r == 4 and c == 2:
                        if bt[4][2]['image'] == f2 and bt[4][3]['image'] == f2 and bt[4][4]['image'] == f1:
                                flag1 = True
                elif r == 4 and c == 6:
                        if bt[4][6]['image'] == f2 and bt[4][5]['image'] == f2 and bt[4][4]['image'] == f1:
                                flag1 = True
                elif r == 6 and c == 4:
                        if bt[6][4]['image'] == f2 and bt[5][4]['image'] == f2 and bt[4][4]['image'] == f1:
                                flag1 = True
                elif r == 3 and c == 2:
                        if bt[r][c]['image'] == f2 and bt[r][c + 1]['image'] == f2 and bt[r][c + 2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r + 1][c]['image'] == f2 and bt[r + 2][c]['image'] == f1:
                                flag1 = True
                elif r == 3 and c == 6:
                        if bt[r][c]['image'] == f2 and bt[r][c - 1]['image'] == f2 and bt[r][c - 2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r + 1][c]['image'] == f2 and bt[r + 2][c]['image'] == f1:
                                flag1 = True
                elif r == 5 and c == 2:
                        if bt[r][c]['image'] == f2 and bt[r][c + 1]['image'] == f2 and bt[r][c + 2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r - 1][c]['image'] == f2 and bt[r - 2][c]['image'] == f1:
                                flag1 = True
                elif r == 5 and c == 6:
                        if bt[r][c]['image'] == f2 and bt[r][c - 1]['image'] == f2 and bt[r][c - 2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r - 1][c]['image'] == f2 and bt[r - 2][c]['image'] == f1:
                                flag1 = True
                elif r==1 and c==3:
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                elif r==1 and c==4:
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                elif r==1 and c==5:
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                elif r==2 and c==3:
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                elif r==2 and c==5:
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                elif r==3 and c ==1:
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                elif r==4 and c==1:
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                elif r==5 and c==1:
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                elif r==7 and c==3:
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                elif r==7 and c==4:
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                elif r==7 and c==5:
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                elif r==6 and c==3:
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c+1]['image'] == f2 and bt[r][c+2]['image'] == f1:
                                flag1 = True
                elif r==6 and c==5:
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                elif r==3 and c==7:
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r+1][c]['image'] == f2 and bt[r+2][c]['image'] == f1:
                                flag1 = True
                elif r==4 and c==7:
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                elif r==5 and c==7:
                        if bt[r][c]['image'] == f2 and bt[r][c-1]['image'] == f2 and bt[r][c-2]['image'] == f1:
                                flag1 = True
                        if bt[r][c]['image'] == f2 and bt[r-1][c]['image'] == f2 and bt[r-2][c]['image'] == f1:
                                flag1 = True
                elif bt[r][c]['image'] == f2:
                        if bt[r - 1][c]['image'] == f2 and bt[r - 2][c]['image'] == f1:
                                flag1 = True
                        if bt[r + 1][c]['image'] == f2 and bt[r + 2][c]['image'] == f1:
                                flag1 = True
                        if bt[r][c - 1]['image'] == f2 and bt[r][c - 2]['image'] == f1:
                                flag1 = True
                        if bt[r][c + 1]['image'] == f2 and bt[r][c + 2]['image'] == f1:
                                flag1 = True

                if flag1 == True:
                        bt[r][c].config(image=img3)
                        fr = r
                        fc = c
                        p += 1

        else:
                sr = r
                sc = c

                if sr < fr and fc==sc:
                        if bt[r][c]['image'] == f1:
                                if abs(fr - sr) == 2 and bt[fr - 1][c]['image'] == f2:
                                        bt[fr][fc]['image'] = img1
                                        bt[fr - 1][fc]['image'] = img1
                                        bt[sr][fc]['image'] = img2
                                        p = 0
                                        f = check_finish()
                elif sr > fr and fc==sc:
                        if bt[r][c]['image'] == f1:
                                if abs(fr - sr) == 2 and bt[fr + 1][c]['image'] == f2:
                                        bt[fr][fc]['image'] = img1
                                        bt[fr + 1][fc]['image'] = img1
                                        bt[sr][fc]['image'] = img2
                                        p = 0
                                        f = check_finish()
                elif sc < fc and fr==sr:
                        if bt[r][c]['image'] == f1:
                                if abs(fc - sc) == 2 and bt[r][fc - 1]['image'] == f2:
                                        bt[fr][fc]['image'] = img1
                                        bt[fr][fc - 1]['image'] = img1
                                        bt[fr][sc]['image'] = img2
                                        p = 0
                                        f = check_finish()
                elif sc > fc and fr==sr:
                        if bt[r][c]['image'] == f1:
                                if abs(fc - sc) == 2 and bt[r][fc + 1]['image'] == f2:
                                        bt[fr][fc]['image'] = img1
                                        bt[fr][fc + 1]['image'] = img1
                                        bt[fr][sc]['image'] = img2
                                        p = 0
                                        f = check_finish()

                if f == True:
                        disab()
                        p = 0
                        for i in range(1, 8):
                                for j in range(1, 8):
                                        if bt[i][j]['image'] == f2:
                                                p += 1

                        if p == 1:
                                print('You WON!!!')
                                messagebox.showinfo(title='Message', message='Congratulations, O wins!')

                        else:
                                print(f"You lost, as left {p} pegs")
                                messagebox.showinfo(title='Message', message="You lost, as left " + str(p) + " pegs")


def reset():
        global p, f1, f2, f3, flag, f4
        flag = True
        p = 0
        for r in range(9):
                for c in range(9):
                        bt[r][c] = Button(frm1,padx=5, pady=5 )

        bt[1][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=1, column=3: click(row, column))
        bt[1][3].grid(row=1, column=3)
        bt[1][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=1, column=4: click(row, column))
        bt[1][4].grid(row=1, column=4)
        bt[1][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=1, column=5: click(row, column))
        bt[1][5].grid(row=1, column=5)

        bt[2][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=2, column=3: click(row, column))
        bt[2][3].grid(row=2, column=3)
        bt[2][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=2, column=4: click(row, column))
        bt[2][4].grid(row=2, column=4)
        bt[2][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=2, column=5: click(row, column))
        bt[2][5].grid(row=2, column=5)

        bt[3][1] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=1: click(row, column))
        bt[3][1].grid(row=3, column=1)
        bt[3][2] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=2: click(row, column))
        bt[3][2].grid(row=3, column=2)
        bt[3][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=3: click(row, column))
        bt[3][3].grid(row=3, column=3)
        bt[3][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=4: click(row, column))
        bt[3][4].grid(row=3, column=4)
        bt[3][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=5: click(row, column))
        bt[3][5].grid(row=3, column=5)
        bt[3][6] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=6: click(row, column))
        bt[3][6].grid(row=3, column=6)
        bt[3][7] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=3, column=7: click(row, column))
        bt[3][7].grid(row=3, column=7)

        bt[4][1] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=1: click(row, column))
        bt[4][1].grid(row=4, column=1)
        bt[4][2] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=2: click(row, column))
        bt[4][2].grid(row=4, column=2)
        bt[4][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=3: click(row, column))
        bt[4][3].grid(row=4, column=3)
        bt[4][4] = Button(frm1, image=img1, padx=5, pady=5, command=lambda row=4, column=4: click(row, column))
        bt[4][4].grid(row=4, column=4)
        bt[4][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=5: click(row, column))
        bt[4][5].grid(row=4, column=5)
        bt[4][6] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=6: click(row, column))
        bt[4][6].grid(row=4, column=6)
        bt[4][7] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=4, column=7: click(row, column))
        bt[4][7].grid(row=4, column=7)

        bt[5][1] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=1: click(row, column))
        bt[5][1].grid(row=5, column=1)
        bt[5][2] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=2: click(row, column))
        bt[5][2].grid(row=5, column=2)
        bt[5][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=3: click(row, column))
        bt[5][3].grid(row=5, column=3)
        bt[5][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=4: click(row, column))
        bt[5][4].grid(row=5, column=4)
        bt[5][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=5: click(row, column))
        bt[5][5].grid(row=5, column=5)
        bt[5][6] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=6: click(row, column))
        bt[5][6].grid(row=5, column=6)
        bt[5][7] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=5, column=7: click(row, column))
        bt[5][7].grid(row=5, column=7)

        bt[6][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=6, column=3: click(row, column))
        bt[6][3].grid(row=6, column=3)
        bt[6][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=6, column=4: click(row, column))
        bt[6][4].grid(row=6, column=4)
        bt[6][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=6, column=5: click(row, column))
        bt[6][5].grid(row=6, column=5)

        bt[7][3] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=7, column=3: click(row, column))
        bt[7][3].grid(row=7, column=3)
        bt[7][4] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=7, column=4: click(row, column))
        bt[7][4].grid(row=7, column=4)
        bt[7][5] = Button(frm1, image=img2, padx=5, pady=5, command=lambda row=7, column=5: click(row, column))
        bt[7][5].grid(row=7, column=5)

        btred = Button(frm1, image=img3)
        f1 = bt[4][4]['image']
        f2 = bt[2][4]['image']
        f3 = btred['image']


button_reset = Button(root, text='New Game', bg='darkcyan', padx=10, pady=10,command=reset)
button_reset.grid(row=3, column=2)

reset()
root.mainloop()