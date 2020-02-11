from tkinter import *
import sqlite3
from tkinter import messagebox


    

root = Tk()
root.geometry('300x300')
root.title("QUIZ")

var=IntVar()
Name=StringVar()
Registration_no=IntVar()
Section=StringVar()
Level=IntVar()
Answer=IntVar()


    
label_1 = Label(root,text="Name",font=("bold",10))
label_2 = Label(root,text="Registration No.",font=("bold",10))
label_3 = Label(root,text="Section",font=("bold",10))
label_4 = Label(root,text="Level",font=("bold",10))
entry_1 = Entry(root,textvar=Name)
entry_2 = Entry(root,textvar=Registration_no)
entry_3 = Entry(root,textvar=Section)
entry_4 = Entry(root)


label_1.grid(row=0,sticky=W)
label_2.grid(row=1,sticky=W)
label_3.grid(row=2,sticky=W)
label_4.grid(row=7,sticky=W)


entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)
entry_3.grid(row=2,column=1)


Radiobutton(root,text="Easy",padx = 5,variable=Level, value=1).place(x=40,y=90)
Radiobutton(root,text="Moderate",padx = 5,variable=Level, value=2).place(x=40,y=110)
Radiobutton(root,text="Hard",padx = 5,variable=Level, value=3).place(x=40,y=130)

def Exit():
    root.destroy()

def database():
    b=var.get()
    name=Name.get()
    reg=Registration_no.get()
    sect=Section.get()
    level=Level.get()
    conn=sqlite3.connect("project.db")
   #conn.execute("create table new_data2(Name varchar(50),Registration_no varchar(50),Section varchar(50),Level varchar(50));")
    conn.execute("insert into new_data2(Name,Registration_no,Section,Level)values(?,?,?,?)",(name,reg,sect,level))
    conn.execute("select * from new_data2")
    conn.commit()
    a=Level.get()
    root.destroy()

    def save():
            answer=Answer.get()
            answer=int(answer)
            con=sqlite3.connect('project.db')
 #           con.execute("create table new_data3(Answer Int);")
            con.execute("insert into new_data3(Answer)values(?)",(answer))
            #con.execute("select * from new_data3")
            con.commit()
            

    if (a==0):
       messagebox()
       exit()
    else:
       print("DATA ENTERED")
 
        
        
    
    if (a==1):
        a1=Tk()
        a1.geometry('500x500')
        a1.title('Question Bank "Easy"')

        

        def Next():
            a1.destroy()
            a2=Tk()
            a2.geometry('500x500')
            a2.title('Question Bank "Easy"')

            namelabel_easy=Label(a2,text='welcome'' '+Name.get())
            namelabel_easy.grid(row=0,sticky=W)
            easylabel_1=Label(a2,text='Questions:',font=('bold',15))
            easylabel_1.grid(row=2,column=1)
            easylabel_2=Label(a2,text='2.Who is The President of Pakistan?',font=10)
            easylabel_2.grid(row=4,sticky=W)
        
            Radiobutton(a2,text="Shahid Afridi",padx = 5,variable=Answer, value=1).place(x=40,y=70)
            Radiobutton(a2,text="Mohammad Shahzad",padx = 5,variable=Answer, value=2).place(x=40,y=90)
            Radiobutton(a2,text="Imran Khan",padx = 5,variable=Answer,value=3).place(x=40,y=110)
            Radiobutton(a2,text="Nawaz ",padx = 5,variable=Answer, value=4).place(x=40,y=130)
        
            Button(a2,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
            Button(a2,text='Next',width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
            Button(a2,text='Save',width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
            Button(a2,text='End',command=lambda:a2.destroy(),width=15,bg='red',fg='blue',font=('bold')).place(x=200,y=250)
        

            
        namelabel_easy=Label(a1,text='welcome'' '+Name.get())
        namelabel_easy.grid(row=0,sticky=W)
        easylabel_1=Label(a1,text='Questions:',font=('bold',15))
        easylabel_1.grid(row=2,column=1)
        easylabel_2=Label(a1,text='1.Who is The Prime Minister of India?',font=10)
        easylabel_2.grid(row=4,sticky=W)
        
        Radiobutton(a1,text="Manmohan Singh",padx = 5,variable=Answer, value=1).place(x=40,y=70)
        Radiobutton(a1,text="Virat Kohli",padx = 5,variable=Answer, value=2).place(x=40,y=90)
        Radiobutton(a1,text="Narendra Modi",padx = 5,variable=Answer,value=3).place(x=40,y=110)
        Radiobutton(a1,text="Dhoni",padx = 5,variable=Answer, value=4).place(x=40,y=130)

        Button(a1,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
        Button(a1,text='Next',command=Next,width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
        Button(a1,text='Save',command=save,width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
        Button(a1,text='End',command=lambda:a1.destroy(),width=15,bg='red',fg='blue',font=('bold')).place(x=200,y=250)
    
        a1.mainloop()






        
    elif (a==2):
        a1=Tk()
        a1.title('Moderate')
        a1.geometry('500x500')
        moderatelabel_1=Label(a1,text='Questions:',font=('bold',15))
        moderatelabel_1.grid(row=0,column=1)


        moderatelabel_2=Label(a1,text='1.Who is The Captain of Indian Cricket Team?',font=10)
        moderatelabel_2.grid(row=4,sticky=W)

        Radiobutton(a1,text="Manmohan Singh",variable=Answer,padx = 5, value=1).place(x=40,y=70)
        Radiobutton(a1,text="Virat Kohli",variable=Answer,padx = 5, value=2).place(x=40,y=90)
        Radiobutton(a1,text="Narendra Modi",variable=Answer,padx = 5,value=3).place(x=40,y=110)
        Radiobutton(a1,text="Sachin Tendulkar",variable=Answer,padx = 5, value=4).place(x=40,y=130)
        def Next():
            a1.destroy()
            a2=Tk()
            a2.geometry('500x500')
            a2.title('Question Bank "Easy"')

            namelabel_easy=Label(a2,text='welcome'' '+Name.get())
            namelabel_easy.grid(row=0,sticky=W)
            easylabel_1=Label(a2,text='Questions:',font=('bold',15))
            easylabel_1.grid(row=2,column=1)
            easylabel_2=Label(a2,text='2.Value of "pi" is:',font=10)
            easylabel_2.grid(row=4,sticky=W)
        
            Radiobutton(a2,text="1.31",padx = 5,variable=Answer, value=1).place(x=40,y=70)
            Radiobutton(a2,text="3.33",padx = 5,variable=Answer, value=2).place(x=40,y=90)
            Radiobutton(a2,text="0.14",padx = 5,variable=Answer,value=3).place(x=40,y=110)
            Radiobutton(a2,text="3.14 ",padx = 5,variable=Answer, value=4).place(x=40,y=130)
        
            Button(a2,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
            Button(a2,text='Next',width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
            Button(a2,text='Save',command=save,width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
            Button(a2,text='End',command=lambda:a2.destroy(),width=15,bg='red',fg='blue',font=('bold')).place(x=200,y=250)
        
     
        Button(a1,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
        Button(a1,text='Next',command=Next,width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
        Button(a1,text='Save',width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
        Button(a1,text='End',width=15,bg='red',fg='blue',font=('bold'),command=lambda:a1.destroy()).place(x=200,y=250)
    

        a1.mainloop()
        
    else:
        a1=Tk()
        a1.title('Hard')
        a1.geometry('500x500')
        hardlabel_1=Label(a1,text='Questions:',font=('bold',15))
        hardlabel_1.grid(row=0,column=1)

        def end():
            a1.destroy()

        hardlabel_2=Label(a1,text='1.How many days are there in a week?',font=10)
        hardlabel_2.grid(row=4,sticky=W)

        Radiobutton(a1,text="four",padx = 5, value=1).place(x=40,y=70)
        Radiobutton(a1,text="zero",padx = 5, value=2).place(x=40,y=90)
        Radiobutton(a1,text="seven",padx = 5,value=3).place(x=40,y=110)
        Radiobutton(a1,text="one",padx = 5, value=4).place(x=40,y=130)

        def Next():
            a1.destroy()
            a2=Tk()
            a2.geometry('500x500')
            a2.title('Question Bank "Hard"')

            namelabel_easy=Label(a2,text='welcome'' '+Name.get())
            namelabel_easy.grid(row=0,sticky=W)
            easylabel_1=Label(a2,text='Questions:',font=('bold',15))
            easylabel_1.grid(row=2,column=1)
            easylabel_2=Label(a2,text='2.Value of "pi" is:',font=10)
            easylabel_2.grid(row=4,sticky=W)
        
            Radiobutton(a2,text="1.31",padx = 5,variable=Answer, value=1).place(x=40,y=70)
            Radiobutton(a2,text="3.33",padx = 5,variable=Answer, value=2).place(x=40,y=90)
            Radiobutton(a2,text="0.14",padx = 5,variable=Answer,value=3).place(x=40,y=110)
            Radiobutton(a2,text="3.14 ",padx = 5,variable=Answer, value=4).place(x=40,y=130)
        
            Button(a2,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
            Button(a2,text='Next',width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
            Button(a2,text='Save',command=save,width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
            Button(a2,text='End',command=lambda:a2.destroy(),width=15,bg='red',fg='blue',font=('bold')).place(x=200,y=250)
        
        Button(a1,text='Previous',width=15,bg='blue',fg='white',font=('bold')).place(x=50,y=200)
        Button(a1,text='Next',command=Next,width=15,bg='yellow',fg='red',font=('bold')).place(x=200,y=200)
        Button(a1,text='Save',command=save,width=15,bg='green',fg='yellow',font=('bold')).place(x=50,y=250)
        Button(a1,text='End',width=15,bg='red',fg='blue',font=('bold'),command=end).place(x=200,y=250)
    
        a1.mainloop()
def messagebox():

    from tkinter import messagebox
    messagebox.showinfo('Error','No Option Selected')



Button(root,text="Submit",command=database,width=20,bg='blue',fg='white').place(x=60,y=200)
        
b1=Button(root,text='Exit',command=Exit,width=20,bg='red',fg='white').place(x=60,y=250)

root.mainloop()
