from tkinter import *
root=Tk()

#---------SIZE OF CALCULATOR---------
root.geometry("400x500")
root.resizable(False,False) # here we fix the size

#----------TITLE---------------
root.title("Calculator By : S@tvik ")

#--------ENTRY BOX-------------------
entry_box=Entry(font="verdana 14 bold",bd=10,width=25,justify=RIGHT,bg="cadetblue")
entry_box.insert(0,'0')
entry_box.place(x=16,y=10)

#---------function-----------
def enterNumber(x):
    if entry_box.get()=='0':
        if x=='.':
            entry_box.insert(1,'.')
        else:
            entry_box.delete(0,"end")
            entry_box.insert(0,str(x))
    else:
        lenght=len(entry_box.get())
        entry_box.insert(lenght,str(x))

def enter_operator(x):
    if entry_box !=0:
        lenght=len(entry_box.get())
        all_text=entry_box.get()
        last_char=all_text[-1:]
        if last_char in ['+','-','/'] or all_text[-2:]=="**" :
            pass
        else:
            entry_box.insert(lenght,button_operator[x]['text'])

def clear_me():
    entry_box.delete(0,END)
    entry_box.insert(0,'0')

result=0
history=[]
def equal_me():
    content=entry_box.get()
    result=eval(content)
    entry_box.delete(0,END)
    entry_box.insert(0,result)
    history.append(content)
    history.reverse()
    status.configure(text="History : " + " | ".join(history[:5]),font='verdana 10 bold')


def delete_me():

    lenght=len(entry_box.get())
    entry_box.delete(lenght-1,END)
    if len==1:
        entry_box.insert(0,'0')
#----------BUTTONS---------------
button_numbers=[]
for i in range(10):
    button_numbers.append(Button(width=8,height=1,text=str(i),bd=6,command=lambda x=i:enterNumber(x)))

button_text=1
for i in range(3):
    for j in range(3):
        button_numbers[button_text].place(x=30+j*90,y=70+i*70)
        button_text +=1

button_zero=Button(width=21,height=1,text='0',bd=5,command=lambda x=0:enterNumber(x))
button_zero.place(x=30,y=280)

button_dot=Button(width=8,height=1,text='.',bd=5,font='times 10 bold',command=lambda x='.':enterNumber(x))
button_dot.place(x=210,y=280)

button_clear=Button(width=8,height=1,text='c',bd=5,command=clear_me)
button_clear.place(x=30,y=340)

button_del=Button(width=21,height=1,text='Del',bd=5,font='times 10 bold',command=delete_me)
button_del.place(x=210,y=340)

#---------operators-----------
button_operator=[]
for i in range(4):
    button_operator.append(Button(width=8,height=1,bd=6,command=lambda x=i: enter_operator(x)))

button_operator[0]["text"]="+"
button_operator[1]["text"]="-"
button_operator[2]["text"]="*"
button_operator[3]["text"]="/"

for i in range(4):
    button_operator[i].place(x=300,y=70+i*70)

button_equal=Button(width=8,height=1,bd=5,text='=',font='times 10 bold',command=equal_me)
button_equal.place(x=121,y=340)

#-----------history-----------

status=Label(root,text="History : ",relief=SUNKEN,height=3,anchor=W,bd=8,font='verdana 10 bold')
status.pack(side=BOTTOM,fill=X)

root.mainloop()
