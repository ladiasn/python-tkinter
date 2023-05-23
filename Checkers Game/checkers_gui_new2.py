from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image

root =Tk()
root.title('Checkers')


bt= [
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
        [' ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ]
1

imgblack = ImageTk.PhotoImage(Image.open('black.jpg'))
imgwhite = ImageTk.PhotoImage(Image.open('white.jpg'))
imgred = ImageTk.PhotoImage(Image.open('blackred.jpg'))
imgblue = ImageTk.PhotoImage(Image.open('blackblue.jpg'))
imgredcrown = ImageTk.PhotoImage(Image.open('redcrown.jpg'))
imgbluecrown = ImageTk.PhotoImage(Image.open('bluecrown.jpg'))



lb1 = Label(root, text='Checkers', font=('Comic Sans', 20))
lb1.grid(row=0, column=0, columnspan=5)

fr1 = Frame(root)
fr1.grid(row=1, column=0, columnspan=5)

lb2 = Label(root, text='Red plays',font=('Comic Sans', 15), bg='red')
lb2.grid(row=3, column=2)


def disab():
    for i in range(1, 9):
        for j in range(1, 9):
            bt[i][j].config(state=DISABLED)

def click(r,c):
        global flag, p, fr, fc, sr, sc, flagred, flagredcrown, flagblue, flagbluecrown

        #red plays
        if flag == True:
            print('red')

            if bt[r][c]['image'] == fred and flagred == False and flagredcrown == False:
                flag1 = False
                if r == 2:
                    if c >= 1 and c <= 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                    if c >= 2 and c <= 8:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                elif r >= 3 and r <= 8:
                    print('ok')
                    if c == 1:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) \
                                and bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    if c == 2:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) \
                                and bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    if c >= 3 and c <= 6:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) \
                                and bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) \
                                and bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    if c == 7:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) \
                                and bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    if c == 8:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) \
                                and bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True

                if flag1 == True:
                    print(111)
                    flagred = True
                    fr = r
                    fc = c

            # redcrown
            elif bt[r][c]['image'] == fredcrown and flagredcrown == False and flagred == False:
                print(33)
                flag1 = False
                if r == 1:
                    if c == 2:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 2:
                    if c == 1:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 3 or r == 5:
                    if c == 2:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 4 or r == 6:
                    if c == 1:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fblue or bt[r + 1][c + 1]['image'] == fbluecrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fblue or bt[r + 1][c - 1]['image'] == fbluecrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 7:
                    if c == 2:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                elif r == 8:
                    if c == 1:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fblue or bt[r - 1][c + 1]['image'] == fbluecrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fblue or bt[r - 1][c - 1]['image'] == fbluecrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True

                if flag1 == True:
                    flagredcrown = True
                    fr = r
                    fc = c

            elif bt[r][c]['image'] == fblack and flagred == True:
                print(2)
                if r < fr:
                    if abs(fr - r) == 1 and abs(fc - c) == 1:
                        if bt[fr][fc]['image'] == fred:
                            bt[fr][fc].config(image=imgblack)
                            bt[r][c].config(image=imgred)
                            flag = False
                            lb2.config(text='Blue plays')
                            lb2.config(bg='blue')
                            if r == 1:
                                bt[r][c].config(image=imgredcrown)
                            flagred = False
                            winner()
                    elif abs(fr - r) == 2 and abs(fc - c) == 2:
                        if fc >= 1 and fc <= 2:
                            if bt[fr - 1][fc + 1]['image'] == fblue or bt[fr - 1][fc + 1]['image'] == fbluecrown:
                                print(15)
                                bt[fr][fc].config(image=imgblack)
                                bt[r][c].config(image=imgred)
                                bt[fr - 1][fc + 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                if r == 1:
                                    bt[r][c].config(image=imgredcrown)
                                flagred = False
                                winner()
                        elif fc >= 3 and fc <= 6:
                            if c > fc:
                                if bt[fr - 1][fc + 1]['image'] == fblue or bt[fr - 1][fc + 1]['image'] == fbluecrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[r][c].config(image=imgred)
                                    bt[fr - 1][fc + 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    if r == 1:
                                        bt[r][c].config(image=imgredcrown)
                                    flagred = False
                                    winner()
                            else:
                                if bt[fr - 1][fc - 1]['image'] == fblue or bt[fr - 1][fc - 1]['image'] == fbluecrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[r][c].config(image=imgred)
                                    bt[fr - 1][fc - 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    if r == 1:
                                        bt[sr][sc].config(image=imgredcrown)
                                    flagred = False
                                    winner()
                        elif fc >= 7 and fc <= 8:
                            if bt[fr - 1][fc - 1]['image'] == fblue or bt[fr - 1][fc - 1]['image'] == fbluecrown:
                                print(100)
                                bt[fr][fc].config(image=imgblack)
                                bt[r][c].config(image=imgred)
                                bt[fr - 1][fc - 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                if r == 1:
                                    bt[r][c].config(image=imgredcrown)
                                flagred = False
                                winner()

            elif (bt[r][c]['image'] == fblack and flagredcrown == True):
                sr = r
                sc = c
                if abs(fr - sr) == 1 and abs(fc - sc) == 1:
                    if bt[fr][fc]['image'] == fredcrown:
                        bt[fr][fc].config(image=imgblack)
                        bt[sr][sc].config(image=imgredcrown)
                        flag = False
                        lb2.config(text='Blue plays')
                        lb2.config(bg='blue')
                        flagredcrown = False
                        winner()
                elif abs(fr - sr) == 2 and abs(fc - sc) == 2:
                    if fc >= 1 and fc <= 2:
                        if sr < fr:
                            if bt[fr - 1][fc + 1]['image'] == fblue or bt[fr - 1][fc + 1]['image'] == fbluecrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgredcrown)
                                bt[fr - 1][fc + 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                flagredcrown = False
                                winner()
                        else:
                            if bt[fr + 1][fc + 1]['image'] == fblue or bt[fr + 1][fc + 1]['image'] == fbluecrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgredcrown)
                                bt[fr + 1][fc + 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                flagredcrown = False
                                winner()
                    elif fc >= 3 and fc <= 6:
                        print(36)
                        if sr < fr:
                            if sc < fc:
                                if bt[fr - 1][fc - 1]['image'] == fblue or bt[fr - 1][fc - 1]['image'] == fbluecrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgredcrown)
                                    bt[fr - 1][fc - 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    flagredcrown = False
                                    winner()
                            else:
                                if bt[fr - 1][fc + 1]['image'] == fblue or bt[fr - 1][fc + 1]['image'] == fbluecrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgredcrown)
                                    bt[fr - 1][fc + 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    flagredcrown = False
                                    winner()
                        else:
                            if sc < fc:
                                print('noo')
                                if bt[fr + 1][fc - 1]['image'] == fblue or bt[fr + 1][fc - 1]['image'] == fbluecrown:
                                    print('no11')
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgredcrown)
                                    bt[fr + 1][fc - 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    flagredcrown = False
                                    winner()
                            else:
                                if bt[fr + 1][fc + 1]['image'] == fblue or bt[fr + 1][fc + 1]['image'] == fbluecrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgredcrown)
                                    bt[fr + 1][fc + 1].config(image=imgblack)
                                    flag = False
                                    lb2.config(text='Blue plays')
                                    lb2.config(bg='blue')
                                    flagredcrown = False
                                    winner()
                    elif fc >= 7 and fc <= 8:
                        if sr < fr:
                            if bt[fr - 1][fc - 1]['image'] == fblue or bt[fr - 1][fc - 1]['image'] == fbluecrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgredcrown)
                                bt[fr - 1][fc - 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                flagredcrown = False
                                winner()
                        else:
                            if bt[fr + 1][fc - 1]['image'] == fblue or bt[fr + 1][fc - 1]['image'] == fbluecrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgredcrown)
                                bt[fr + 1][fc - 1].config(image=imgblack)
                                flag = False
                                lb2.config(text='Blue plays')
                                lb2.config(bg='blue')
                                flagredcrown = False
                                winner()

        #blue plays
        elif flag == False:
            print('blue')

            if bt[r][c]['image'] == fblue and flagblue == False and flagbluecrown == False:
                flag1 = False
                if r == 7:
                    if c >= 1 and c <= 7:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                    if c >= 2 and c <= 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                elif r >= 1 and r <= 6:
                    print('ok1')
                    if c == 1:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) \
                                and bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                    if c == 2:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) \
                                and bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                    if c >= 3 and c <= 6:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) \
                                and bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) \
                                and bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                    if c == 7:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) \
                                and bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                    if c == 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) \
                                and bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True

                if flag1 == True:
                    print(122)
                    flagblue = True
                    fr = r
                    fc = c

            #bluecrown
            elif bt[r][c]['image'] == fbluecrown and flagbluecrown == False and flagblue == False:
                print(334)
                flag1 = False
                if r == 1:
                    if c == 2:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 2:
                    if c == 1:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 3 or r == 5:
                    if c == 2:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 4 or r == 6:
                    if c == 1:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c + 1]['image'] == fred or bt[r + 1][c + 1]['image'] == fredcrown) and \
                                bt[r + 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r + 1][c - 1]['image'] == fred or bt[r + 1][c - 1]['image'] == fredcrown) and \
                                bt[r + 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                elif r == 7:
                    if c == 2:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 4 or c == 6:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                    elif c == 8:
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                        if bt[r + 1][c - 1]['image'] == fblack:
                            flag1 = True
                elif r == 8:
                    if c == 1:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                    elif c == 3 or c == 5:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c + 1]['image'] == fred or bt[r - 1][c + 1]['image'] == fredcrown) and \
                                bt[r - 2][c + 2]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True
                    elif c == 7:
                        if bt[r - 1][c + 1]['image'] == fblack:
                            flag1 = True
                        if bt[r - 1][c - 1]['image'] == fblack:
                            flag1 = True
                        if (bt[r - 1][c - 1]['image'] == fred or bt[r - 1][c - 1]['image'] == fredcrown) and \
                                bt[r - 2][c - 2]['image'] == fblack:
                            flag1 = True

                if flag1 == True:
                    flagbluecrown = True
                    fr = r
                    fc = c

            elif bt[r][c]['image'] == fblack and flagblue == True:
                print('2b')
                if r > fr:
                    if abs(fr - r) == 1 and abs(fc - c) == 1:
                        if bt[fr][fc]['image'] == fblue:
                            bt[fr][fc].config(image=imgblack)
                            bt[r][c].config(image=imgblue)
                            flag = True
                            lb2.config(text='Red plays')
                            lb2.config(bg='red')
                            if r == 8:
                                bt[r][c].config(image=imgbluecrown)
                            flagblue = False
                            winner()
                    elif abs(fr - r) == 2 and abs(fc - c) == 2:
                        if fc >= 1 and fc <= 2:
                            if bt[fr + 1][fc + 1]['image'] == fred or bt[fr + 1][fc + 1]['image'] == fredcrown:
                                print(151)
                                bt[fr][fc].config(image=imgblack)
                                bt[r][c].config(image=imgblue)
                                bt[fr + 1][fc + 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                if r == 8:
                                    bt[r][c].config(image=imgbluecrown)
                                flagblue = False
                                winner()
                        elif fc >= 3 and fc <= 6:
                            if c > fc:
                                if bt[fr + 1][fc + 1]['image'] == fred or bt[fr + 1][fc + 1]['image'] == fredcrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[r][c].config(image=imgblue)
                                    bt[fr + 1][fc + 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    if r == 8:
                                        bt[r][c].config(image=imgbluecrown)
                                    flagblue = False
                                    winner()
                            else:
                                if bt[fr + 1][fc - 1]['image'] == fred or bt[fr + 1][fc - 1]['image'] == fredcrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[r][c].config(image=imgblue)
                                    bt[fr + 1][fc - 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    if r == 8:
                                        bt[r][c].config(image=imgbluecrown)
                                    flagblue = False
                                    winner()
                        elif fc >= 7 and fc <= 8:
                            if bt[fr + 1][fc - 1]['image'] == fred or bt[fr + 1][fc - 1]['image'] == fredcrown:
                                print(1001)
                                bt[fr][fc].config(image=imgblack)
                                bt[r][c].config(image=imgblue)
                                bt[fr + 1][fc - 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                if r == 8:
                                    bt[r][c].config(image=imgbluecrown)
                                flagblue = False
                                winner()

            elif (bt[r][c]['image'] == fblack and flagbluecrown == True):
                sr = r
                sc = c
                if abs(fr - sr) == 1 and abs(fc - sc) == 1:
                    if bt[fr][fc]['image'] == fbluecrown:
                        bt[fr][fc].config(image=imgblack)
                        bt[sr][sc].config(image=imgbluecrown)
                        flag = True
                        lb2.config(text='Red plays')
                        lb2.config(bg='red')
                        flagbluecrown = False
                        winner()
                elif abs(fr - sr) == 2 and abs(fc - sc) == 2:
                    if fc >= 1 and fc <= 2:
                        if sr < fr:
                            if bt[fr - 1][fc + 1]['image'] == fred or bt[fr - 1][fc + 1]['image'] == fredcrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgbluecrown)
                                bt[fr - 1][fc + 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                flagbluecrown = False
                                winner()
                        else:
                            if bt[fr + 1][fc + 1]['image'] == fred or bt[fr + 1][fc + 1]['image'] == fredcrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgbluecrown)
                                bt[fr + 1][fc + 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                flagbluecrown = False
                                winner()
                    elif fc >= 3 and fc <= 6:
                        print(369)
                        if sr < fr:
                            if sc < fc:
                                if bt[fr - 1][fc - 1]['image'] == fred or bt[fr - 1][fc - 1]['image'] == fredcrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgbluecrown)
                                    bt[fr - 1][fc - 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    flagbluecrown = False
                                    winner()
                            else:
                                if bt[fr - 1][fc + 1]['image'] == fred or bt[fr - 1][fc + 1]['image'] == fredcrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgbluecrown)
                                    bt[fr - 1][fc + 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    flagbluecrown = False
                                    winner()
                        else:
                            if sc < fc:
                                print('noo11111')
                                if bt[fr + 1][fc - 1]['image'] == fred or bt[fr + 1][fc - 1]['image'] == fredcrown:
                                    print('no11222')
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgbluecrown)
                                    bt[fr + 1][fc - 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    flagbluecrown = False
                                    winner()
                            else:
                                if bt[fr + 1][fc + 1]['image'] == fred or bt[fr + 1][fc + 1]['image'] == fredcrown:
                                    bt[fr][fc].config(image=imgblack)
                                    bt[sr][sc].config(image=imgbluecrown)
                                    bt[fr + 1][fc + 1].config(image=imgblack)
                                    flag = True
                                    lb2.config(text='Red plays')
                                    lb2.config(bg='red')
                                    flagbluecrown = False
                                    winner()
                    elif fc >= 7 and fc <= 8:
                        if sr < fr:
                            if bt[fr - 1][fc - 1]['image'] == fred or bt[fr - 1][fc - 1]['image'] == fredcrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgbluecrown)
                                bt[fr - 1][fc - 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                flagbluecrown = False
                                winner()
                        else:
                            if bt[fr + 1][fc - 1]['image'] == fred or bt[fr + 1][fc - 1]['image'] == fredcrown:
                                bt[fr][fc].config(image=imgblack)
                                bt[sr][sc].config(image=imgbluecrown)
                                bt[fr + 1][fc - 1].config(image=imgblack)
                                flag = True
                                lb2.config(text='Red plays')
                                lb2.config(bg='red')
                                flagbluecrown = False
                                winner()

def winner():

    pred =0
    pblue =0
    for i in range(1,9):
        for j in range(1,9):
            if bt[i][j]['image'] == fred or bt[i][j]['image'] == fredcrown:
                pred += 1
            if bt[i][j]['image'] == fblue or bt[i][j]['image'] == fbluecrown:
                pblue += 1

    if pred == 0 :
        messagebox.showinfo(title='Message', message='Bravo, Blue Won!')
        disab()

    if pblue == 0 :
        messagebox.showinfo(title='Message', message='Bravo, Red Won!')
        disab()

def reset():
        global fblack, fwhite, fblue, fred, p, flag, fredcrown, fbluecrown, flagred, flagredcrown, flagblue, flagbluecrown

        p=0
        flag = True
        flagred = False
        flagredcrown = False
        flagblue = False
        flagbluecrown = False
        bt[1][1] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[1][2] = Button(fr1, image=imgblue, command = lambda row=1, column=2: click(row,column))
        bt[1][3] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[1][4] = Button(fr1, image=imgblue, command = lambda row=1, column=4: click(row,column))
        bt[1][5] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[1][6] = Button(fr1, image=imgblue, command = lambda row=1, column=6: click(row,column))
        bt[1][7] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[1][8] = Button(fr1, image=imgblue, command = lambda row=1, column=8: click(row,column))

        bt[1][1].grid(row=1, column=1)
        bt[1][2].grid(row=1, column=2)
        bt[1][3].grid(row=1, column=3)
        bt[1][4].grid(row=1, column=4)
        bt[1][5].grid(row=1, column=5)
        bt[1][6].grid(row=1, column=6)
        bt[1][7].grid(row=1, column=7)
        bt[1][8].grid(row=1, column=8)

        bt[2][1] = Button(fr1, image=imgblue, command = lambda row=2, column=1: click(row,column))
        bt[2][2] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[2][3] = Button(fr1, image=imgblue, command = lambda row=2, column=3: click(row,column))
        bt[2][4] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[2][5] = Button(fr1, image=imgblue, command = lambda row=2, column=5: click(row,column))
        bt[2][6] = Button(fr1, image=imgwhite,state=DISABLED)
        bt[2][7] = Button(fr1, image=imgblue, command = lambda row=2, column=7: click(row,column))
        bt[2][8] = Button(fr1, image=imgwhite, state=DISABLED)

        bt[2][1].grid(row=2, column=1)
        bt[2][2].grid(row=2, column=2)
        bt[2][3].grid(row=2, column=3)
        bt[2][4].grid(row=2, column=4)
        bt[2][5].grid(row=2, column=5)
        bt[2][6].grid(row=2, column=6)
        bt[2][7].grid(row=2, column=7)
        bt[2][8].grid(row=2, column=8)

        bt[3][1] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[3][2] = Button(fr1, image=imgblue, command=lambda row=3, column=2: click(row, column))
        bt[3][3] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[3][4] = Button(fr1, image=imgblue, command=lambda row=3, column=4: click(row, column))
        bt[3][5] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[3][6] = Button(fr1, image=imgblue, command=lambda row=3, column=6: click(row, column))
        bt[3][7] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[3][8] = Button(fr1, image=imgblue, command=lambda row=3, column=8: click(row, column))

        bt[3][1].grid(row=3, column=1)
        bt[3][2].grid(row=3, column=2)
        bt[3][3].grid(row=3, column=3)
        bt[3][4].grid(row=3, column=4)
        bt[3][5].grid(row=3, column=5)
        bt[3][6].grid(row=3, column=6)
        bt[3][7].grid(row=3, column=7)
        bt[3][8].grid(row=3, column=8)

        bt[4][1] = Button(fr1, image=imgblack, command=lambda row=4, column=1: click(row, column))
        bt[4][2] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[4][3] = Button(fr1, image=imgblack, command=lambda row=4, column=3: click(row, column))
        bt[4][4] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[4][5] = Button(fr1, image=imgblack, command=lambda row=4, column=5: click(row, column))
        bt[4][6] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[4][7] = Button(fr1, image=imgblack, command=lambda row=4, column=7: click(row, column))
        bt[4][8] = Button(fr1, image=imgwhite, state=DISABLED)

        bt[4][1].grid(row=4, column=1)
        bt[4][2].grid(row=4, column=2)
        bt[4][3].grid(row=4, column=3)
        bt[4][4].grid(row=4, column=4)
        bt[4][5].grid(row=4, column=5)
        bt[4][6].grid(row=4, column=6)
        bt[4][7].grid(row=4, column=7)
        bt[4][8].grid(row=4, column=8)

        bt[5][1] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[5][2] = Button(fr1, image=imgblack, command=lambda row=5, column=2: click(row, column))
        bt[5][3] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[5][4] = Button(fr1, image=imgblack, command=lambda row=5, column=4: click(row, column))
        bt[5][5] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[5][6] = Button(fr1, image=imgblack, command=lambda row=5, column=6: click(row, column))
        bt[5][7] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[5][8] = Button(fr1, image=imgblack, command=lambda row=5, column=8: click(row, column))

        bt[5][1].grid(row=5, column=1)
        bt[5][2].grid(row=5, column=2)
        bt[5][3].grid(row=5, column=3)
        bt[5][4].grid(row=5, column=4)
        bt[5][5].grid(row=5, column=5)
        bt[5][6].grid(row=5, column=6)
        bt[5][7].grid(row=5, column=7)
        bt[5][8].grid(row=5, column=8)

        bt[6][1] = Button(fr1, image=imgred, command=lambda row=6, column=1: click(row, column))
        bt[6][2] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[6][3] = Button(fr1, image=imgred, command=lambda row=6, column=3: click(row, column))
        bt[6][4] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[6][5] = Button(fr1, image=imgred, command=lambda row=6, column=5: click(row, column))
        bt[6][6] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[6][7] = Button(fr1, image=imgred, command=lambda row=6, column=7: click(row, column))
        bt[6][8] = Button(fr1, image=imgwhite, state=DISABLED)

        bt[6][1].grid(row=6, column=1)
        bt[6][2].grid(row=6, column=2)
        bt[6][3].grid(row=6, column=3)
        bt[6][4].grid(row=6, column=4)
        bt[6][5].grid(row=6, column=5)
        bt[6][6].grid(row=6, column=6)
        bt[6][7].grid(row=6, column=7)
        bt[6][8].grid(row=6, column=8)

        bt[7][1] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[7][2] = Button(fr1, image=imgred, command=lambda row=7, column=2: click(row, column))
        bt[7][3] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[7][4] = Button(fr1, image=imgred, command=lambda row=7, column=4: click(row, column))
        bt[7][5] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[7][6] = Button(fr1, image=imgred, command=lambda row=7, column=6: click(row, column))
        bt[7][7] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[7][8] = Button(fr1, image=imgred, command=lambda row=7, column=8: click(row, column))

        bt[7][1].grid(row=7, column=1)
        bt[7][2].grid(row=7, column=2)
        bt[7][3].grid(row=7, column=3)
        bt[7][4].grid(row=7, column=4)
        bt[7][5].grid(row=7, column=5)
        bt[7][6].grid(row=7, column=6)
        bt[7][7].grid(row=7, column=7)
        bt[7][8].grid(row=7, column=8)

        bt[8][1] = Button(fr1, image=imgred, command=lambda row=8, column=1: click(row, column))
        bt[8][2] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[8][3] = Button(fr1, image=imgred, command=lambda row=8, column=3: click(row, column))
        bt[8][4] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[8][5] = Button(fr1, image=imgred, command=lambda row=8, column=5: click(row, column))
        bt[8][6] = Button(fr1, image=imgwhite, state=DISABLED)
        bt[8][7] = Button(fr1, image=imgred, command=lambda row=8, column=7: click(row, column))
        bt[8][8] = Button(fr1, image=imgwhite, state=DISABLED)

        bt[8][1].grid(row=8, column=1)
        bt[8][2].grid(row=8, column=2)
        bt[8][3].grid(row=8, column=3)
        bt[8][4].grid(row=8, column=4)
        bt[8][5].grid(row=8, column=5)
        bt[8][6].grid(row=8, column=6)
        bt[8][7].grid(row=8, column=7)
        bt[8][8].grid(row=8, column=8)


        fblack = bt[4][3]['image']
        fwhite = bt[1][3]['image']
        fred = bt[7][4]['image']
        fblue = bt[1][2]['image']

        bt[9][0] = Button(fr1, image=imgredcrown)
        bt[9][1] = Button(fr1, image=imgbluecrown)

        fredcrown = bt[9][0]['image']
        fbluecrown = bt[9][1]['image']

        lb2.config(bg='red')
        lb2.config(text='Red Plays')


button_reset = Button(root, text='New Game', bg='darkcyan', padx=10, pady=10,command=reset)
button_reset.grid(row=4, column=2)

reset()
root.mainloop()