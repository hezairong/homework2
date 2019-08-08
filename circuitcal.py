from tkinter import *

root = Tk()
root.title("电流计算器")

image_1 = PhotoImage(file = "电路图1.gif")
image_2 = PhotoImage(file = "电路图2.gif")

group = LabelFrame(root,text="请输入参数：",padx=20,pady=20)
group.pack(padx=10,pady=10)

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()

def test(content):
    return content.isdigit()

label1 = Label(group,text = "R1(Ω): ").grid(row = 0,column = 0)
label2 = Label(group,text = "R2(Ω): ").grid(row = 1,column = 0)
label3 = Label(group,text = "R3(Ω): ").grid(row = 2,column = 0)
label4 = Label(group,text = "R4(Ω): ").grid(row = 3,column = 0)
label5 = Label(group,text = "U(V): ").grid(row = 4,column = 0)
label6 = Label(group,text ="电流值(A): ").grid(row =6,column = 0)

e1 = Entry(group,textvariable = v1,validate='key',\
           validatecommand=()).grid(row = 0,column = 2)
e2 = Entry(group,textvariable = v2,validate='key',\
           validatecommand=()).grid(row = 1,column = 2)
e3 = Entry(group,textvariable = v3,validate='key',\
           validatecommand=()).grid(row = 2,column = 2)
e4 = Entry(group,textvariable = v4,validate='key',\
           validatecommand=()).grid(row = 3,column = 2)
e5 = Entry(group,textvariable = v5,validate='key',\
           validatecommand=()).grid(row = 4,column = 2)

def calculate1():
    Rd1 = eval(v2.get())+eval(v3.get())+eval(v4.get())
    R1_23 = eval(v2.get())*eval(v3.get())/Rd1
    R1_24 = eval(v2.get())*eval(v4.get())/Rd1
    R1_34 = eval(v3.get())*eval(v4.get())/Rd1
    Rp1 = ((eval(v1.get())+R1_23)*R1_34)/(R1_23+R1_34+eval(v1.get()))
    U1 = eval(v5.get())
    result = '{:.3f}'.format(U1/(Rp1+R1_24))
    v6.set(result)

def calculate2():
    Rd2 = eval(v1.get())+eval(v2.get())+eval(v3.get())
    R2_13 = (eval(v1.get())*eval(v3.get()))/Rd2
    R2_12 = (eval(v1.get())*eval(v2.get()))/Rd2
    R2_23 = (eval(v2.get())*eval(v3.get()))/Rd2
    Rp2 = ((eval(v4.get())+R2_12)*R2_23)/(eval(v4.get())+R2_12+R2_23)
    U2 = eval(v5.get())
    result = '{:.3f}'.format(U2/(Rp2+R2_13))
    v6.set(result)

Button(group,text='choice1',image=image_1,\
       compound='right',command=calculate1).grid(row=5,column=0)  
Button(group,text='choice2',image=image_2,\
       compound='right',command=calculate2).grid(row=5,column=1)

e6 = Entry(group,textvariable = v6,\
           state = 'readonly').grid(row=6,column=2)


Button(root,text="Quit",command=root.quit).pack(anchor=E)

mainloop()
