from fractions import Fraction as Fra
import numpy as np
import nums_from_string as nfs
import tkinter as tk
from tkinter.messagebox import *

def cal():
    x1,y1 = map(int,Ainput.get().split(","))
    x2,y2 = map(int,Binput.get().split(","))
    x3,y3 = map(int,Cinput.get().split(","))
    mab = ''
    mbc = ''
    mca = ''

    if((x1-x2) != 0):
        mab = (y1-y2) / (x1-x2)
    elif((x1-x2) == 0):
        mab = None

    if((x2-x3) != 0):
        mbc = (y2-y3) / (x2-x3)
    elif((x2-x3) == 0):
        mbc = None

    if((x3-x1) != 0):
        mca = (y3-y1) / (x3-x1)
    elif((x3-x1) == 0):
        mca = None

    if(mab == mbc == mca):
        tk.messagebox.showinfo("計算完成","三點共線不成圓")

    abCenterX = (x1+x2) / 2
    abCenterY = (y1+y2) / 2
    bcCenterX = (x2+x3) / 2
    bcCenterY = (y2+y3) / 2
    caCenterX = (x3+x1) / 2
    caCenterY = (y3+y1) / 2

    mab_prime = ''
    mbc_prime = ''
    mca_prime = ''
#----------------------------------------------------------------------------------#
    if(mab == None):
        mab_prime = 0
    elif(mab == 0):
        mab_prime = None
    elif(mab != 0):
        mab_prime = Fra(*(-mab**-1).as_integer_ratio())
#----------------------------------------------------------------------------------#
    if(mbc == None):
        mbc_prime = 0
    elif(mbc == 0):
        mbc_prime = None
    elif(mbc != 0):
        mbc_prime = Fra(*(-mbc**-1).as_integer_ratio())
#----------------------------------------------------------------------------------#
    if(mca == None):
        mca_prime = 0
    elif(mca == 0):
        mca_prime = None
    elif(mca != 0):
        mca_prime = Fra(*(-mca**-1).as_integer_ratio())
#----------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------#
    kab = ''
    kbc = ''
    kca = ''
    abCenter = ''
    bcCenter = ''
    caCenter= ''
    if(mab_prime == None):
        kab = abCenterX
        abCenter = [1,0]
    else:
        kab = abCenterX*-mab_prime.numerator + abCenterY*mab_prime.denominator
        abCenter = [-mab_prime.numerator,mab_prime.denominator]
#----------------------------------------------------------------------------------#
    if(mbc_prime == None):
        kbc = bcCenterX
        bcCenter = [1,0]
    else:
        kbc = bcCenterX*-mbc_prime.numerator + bcCenterY*mbc_prime.denominator
        bcCenter = [-mbc_prime.numerator,mbc_prime.denominator]
#----------------------------------------------------------------------------------#
    if(mca_prime == None):
        kca = caCenterX*1 + caCenterY*0
        caCenter = [1,0]
    else:
        kca = caCenterX*-mca_prime.numerator + caCenterY*mca_prime.denominator
        caCenter = [-mca_prime.numerator,mca_prime.denominator]
#----------------------------------------------------------------------------------#

    C = np.array([
        abCenter,
        bcCenter
    ])

    k = np.array([kab,kbc]).reshape(2,1)

    C_inv = np.linalg.inv(C)
    Q = C_inv.dot(k)
    Qx = nfs.get_nums(str(Q[0]))[0]
    Qy = nfs.get_nums(str(Q[1]))[0]

    rk = (((x1 - Qx)**2) + ((y1 - Qy)**2))
    ans = f'''    答案為
    圓心({Qx},{Qy}) 半徑√{rk} 
    圓方程式:(X-({Qx}))^2 + (Y-({Qy}))^2 = {rk}'''
    tk.messagebox.showinfo("計算完成",ans)
window = tk.Tk()
window.title('自動解圓方程v0.0.1')
window.geometry('380x150')
window.resizable(False, False)

Alabel = tk.Label(text="請輸入A點")
Alabel.place(x=0,y=0)
Blabel = tk.Label(text="請輸入B點")
Blabel.place(x=0,y=40)
Clabel = tk.Label(text="請輸入C點")
Clabel.place(x=0,y=80)

Ainput = tk.Entry(width=20)
Ainput.place(x=70,y=0)
Binput = tk.Entry(width=20)
Binput.place(x=70,y=40)
Cinput = tk.Entry(width=20)
Cinput.place(x=70,y=80)

Submit = tk.Button(text="計算",command=cal)
Submit.place(x=280,y=40)
window.mainloop()