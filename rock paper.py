#ROCK PAPER SCISSOR
import tkinter as tk
import random
from PIL import ImageTk,Image
def screen():
    global score
    bg=ImageTk.PhotoImage(file='D:/PROJECT/Images/Background.png')
    tk.Label(root,image=bg).pack()
    b=tk.Button(root,image=p1,command=select1).place(x=150,y=95)
    b2=tk.Button(root,image=p2,command=select2).place(x=150,y=345)
    b3=tk.Button(root,image=p3,command=select3).place(x=150,y=580)
    lab=tk.Label(root,text='COMPUTER',font=('Jokerman',20),fg='black',bg='gainsboro')
    lab.place(x=960,y=30)
    lab=tk.Label(root,text='USER',font=('Jokerman',20),fg='black',bg='dark orange')
    lab.place(x=250,y=30)
    score=tk.Label(root,text='win: 0   loss:0',font=('Jokerman',20),fg='black',bg='light steel blue')
    score.place(x=900,y=700)
    exb=tk.Button(root,text='EXIT',font=('Jokerman',20),fg='black',bg='indian red',command=escape)
    exb.place(x=900,y=800)
    root.mainloop()
def escape():
    root.destroy()
def select3():
    global c,loss
    uv=tk.Toplevel()
    def eliminate():
        uv.destroy()
    uv.geometry("500x400+800+150")
    f=3
    k=random.randint(1,3)
    if k==1:
        uv.configure(bg='red')
        loss+=1
        pic=tk.Label(uv,image=p1).place(x=150,y=150)
        label=tk.Label(uv,text='computer wins...it chose rock:(',font=('Jokerman',20),fg='black',bg='white')
        button=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label.pack()
        button.pack()
    elif k==2:
        uv.configure(bg='cyan')
        c+=1
        pic2=tk.Label(uv,image=p2).place(x=150,y=150)
        label2=tk.Label(uv,text='YOU win...comuter chose paper:)',font=('Jokerman',20),fg='black',bg='white')
        button2=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label2.pack()
        button2.pack()
    else:
        uv.configure(bg='lemon chiffon')
        pic3=tk.Label(uv,image=p3).place(x=150,y=150)
        label3=tk.Label(uv,text='draw',font=('Jokerman',20),fg='black',bg='white')
        button3=tk.Button(uv,text='ok',font=15,command=eliminate)
        label3.pack()
        button3.pack()
def select2():
    global c,loss
    uv=tk.Toplevel()
    def eliminate():
        uv.destroy()
    uv.geometry("500x400+800+150")
    f=3
    k=random.randint(1,3)
    if k==1:
        c+=1
        uv.configure(bg='cyan')
        pic=tk.Label(uv,image=p1).place(x=150,y=150)
        label=tk.Label(uv,text='YOU win...computer chose rock:)',font=('Jokerman',20),fg='black',bg='white')
        button=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label.pack()
        button.pack()
    elif k==2:
        uv.configure(bg='lemon chiffon')
        pic2=tk.Label(uv,image=p2).place(x=150,y=150)
        label2=tk.Label(uv,text='draw',font=('Jokerman',20),fg='black',bg='white')
        button2=tk.Button(uv,text='ok',font=15,command=eliminate)
        label2.pack()
        button2.pack()
    else:
        loss+=1
        uv.configure(bg='red')
        pic3=tk.Label(uv,image=p3).place(x=150,y=150)
        label3=tk.Label(uv,text='computer wins...it chose scissor:(',font=('Jokerman',20),fg='black',bg='white')
        button3=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label3.pack()
        button3.pack()
def select1():
    global c,loss
    uv=tk.Toplevel()
    def eliminate():
        uv.destroy()
    uv.geometry("500x400+800+150")
    f=3
    k=random.randint(1,3)
    if k==1:
        uv.configure(bg='lemon chiffon')
        pic=tk.Label(uv,image=p1).place(x=150,y=150)
        label=tk.Label(uv,text='draw',font=('Jokerman',20),fg='black',bg='white')
        button=tk.Button(uv,text='ok',font=15,command=eliminate)
        label.pack()
        button.pack()
    elif k==2:
        loss+=1
        uv.configure(bg='red')
        pic2=tk.Label(uv,image=p2).place(x=150,y=150)
        label2=tk.Label(uv,text='computer wins...it chose paper:(',font=('Jokerman',20),fg='black',bg='white')
        button2=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label2.pack()
        button2.pack()
    else:
        c+=1
        uv.configure(bg='cyan')
        pic3=tk.Label(uv,image=p3).place(x=150,y=150)
        label3=tk.Label(uv,text='YOU win...computer chose scissor:)',font=('Jokerman',20),fg='black',bg='white')
        button3=tk.Button(uv,text='ok',font=15,command=eliminate)
        score['text']='win: '+str(c)+'  loss:'+ str(loss)
        label3.pack()
        button3.pack()
root=tk.Tk()
root.attributes('-fullscreen',True)
p1=ImageTk.PhotoImage(file='D:/PROJECT/rps/2.png')
p2=ImageTk.PhotoImage(file='D:/PROJECT/rps/OIP.png')
p3=ImageTk.PhotoImage(file='D:/PROJECT/rps/mm1.png')
c=0
loss=0
screen()
            
