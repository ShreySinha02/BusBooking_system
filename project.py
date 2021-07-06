from tkinter import *
from PIL import Image,ImageTk
import sqlite3
import tkinter.messagebox as messagebox
#splash screen code 
splash_root=Tk()
splash_root.title("SHREY 191B242 B7")
splash_root.geometry("400x400")
Label(splash_root,text="JAYPEE UNIVESITY OF ENGINEERING",bg="#D96D0F",fg="#F0B6CA",font=("bold",15)).pack()
Label(splash_root,text=" AND TECHNOLOGY",bg="#D96D0F",fg="#F0B6CA",font=("bold",15)).pack()
Label(splash_root,text="Shrey",bg="#949092",fg="#B20414",font=("bold",15)).pack(pady=5)
Label(splash_root,text="191B242",bg="#949092",fg="#B20414",font=("bold",15)).pack()
Label(splash_root,text="B7",bg="#949092",fg="#B20414",font=("bold",15)).pack()
splash_root.after(3000,splash_root.destroy)
splash_root.mainloop()
def fun():
    
    root=Tk()
    root.geometry('400x400')
    root.title("BUS BOOKING SYSTEM")
    head_frame=Frame(root,bg="#5F9EA0",borderwidth=10)
    head_frame.pack()
    head_label=Label(head_frame,text="BUS BOOKING SYSTEM",bg="#D8BFD8",font=("bold","20"))
    head_label.pack()
    img=Image.open("bus.jpg")
    photo=ImageTk.PhotoImage(img)
    photo_label=Label(root,image=photo)
    photo_label.pack()
    f1=Frame(root,bg="grey",borderwidth=5)
    f1.pack()
    #second window
    #Add bus
    def sec():#add bus function
        root.destroy()
        root1=Tk()


        root1.geometry('500x550')
        head_label2=Label(root1,text="BUS BOOKING SYSTEM",bg="#D8BFD8",font=("bold","20"))
        head_label2.config(anchor="center")
        head_label2.grid(row=0,column=4)
        img=Image.open("bus.jpg")
        photo1=ImageTk.PhotoImage(img)
        photo_label1=Label(root1,image=photo1)
        photo_label1.grid(row=1,column=4)
        #assinging data
        fullname=Label(root1,text="Full name").grid(row=3)
        contact=Label(root1,text="Conatct").grid(row=4)
        adress=Label(root1,text="Adress").grid(row=5)
        #making variable
        namevar=StringVar()
        contactvar=IntVar()
        adressvar=StringVar()
        #taking input
        nameentry=Entry(root1,textvariable=namevar).grid(row=3,column=4)
        contactentry=Entry(root1,textvariable=contactvar).grid(row=4,column=4)
        adressentry=Entry(root1,textvariable=adressvar).grid(row=5,column=4)
        #add detail function
        def add_detail():
            operator=Label(root1,text="Operator").grid(row=7)
            bustype=Label(root1,text="bus type").grid(row=8)
            from1=Label(root1,text="from").grid(row=9)
            to=Label(root1,text="to").grid(row=10)
            date=Label(root1,text="date").grid(row=11)
            deptime=Label(root1,text="dept ime").grid(row=12)
            arrtime=Label(root1,text="arr time").grid(row=13)
            fare=Label(root1,text="fare").grid(row=14)
            seat=Label(root1,text="seat").grid(row=15)
            #making variable
            operatorvar=StringVar()
            bustypevar=StringVar()
            fromvar=StringVar()
            tovar=StringVar()
            datevar=StringVar()
            depvar=StringVar()
            arrvar=StringVar()
            farevar=IntVar()
            seatvar=IntVar()
            #taking input
            operatorentry=Entry(root1,textvariable=operatorvar).grid(row=7,column=4)
            busentry=Entry(root1,textvariable=bustypevar).grid(row=8,column=4)
            fromentry=Entry(root1,textvariable=fromvar).grid(row=9,column=4)
            toentry=Entry(root1,textvariable=tovar).grid(row=10,column=4)
            dateentry=Entry(root1,textvariable=datevar).grid(row=11,column=4)
            depentry=Entry(root1,textvariable=depvar).grid(row=12,column=4)
            arrentry=Entry(root1,textvariable=arrvar).grid(row=13,column=4)
            fareentry=Entry(root1,textvariable=farevar).grid(row=14,column=4)
            seatentry=Entry(root1,textvariable=seatvar).grid(row=15,column=4)
            def save():
                name1=namevar.get()
                from1=fromvar.get()
                to1=tovar.get()
                date1=datevar.get()
                arr1=arrvar.get()
                fare1=farevar.get()
                seat1=seatvar.get()
                con=sqlite3.Connection('My_db')
                cur=con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS travel1(name text,from1 text,to1 text,date text,arr text,fare INTEGER,seat INTEGER)""")
                con.commit()
                cur.execute("INSERT INTO travel1 VALUES (?,?,?,?,?,?,?)",(name1,from1,to1,date1,arr1,fare1,seat1))
                con.commit()
                con.close()
                messagebox.showinfo("saved status","saved succesfully")
                root1.destroy()
                fun()
            Button(text="Save",width=10,bg="grey",fg="#B0E0E6",command=save).grid(row=16,column=4)
        Button(text="Add detail",width=10,bg="grey",fg="#B0E0E6",command=add_detail).grid(row=6,column=4)

        root1.mainloop()
    b1=Button(f1,bg="#F5FFFA",text="Add BUS",padx=4,pady=4,fg="#A9A9A9",command=sec)
    b1.pack(side=LEFT,padx=20)
    # b1.bind('<Button-1>',sec)

    #Search bus
    def search_bus():
        root.destroy()
        root2=Tk()
        root2.title('search bus')
        root2.geometry('500x550')
        head_label3=Label(root2,text="BUS BOOKING SYSTEM",bg="#D8BFD8",font=("bold","20"))
        head_label3.config(anchor="center")
        head_label3.grid(row=0,column=4)
        img=Image.open("bus.jpg")
        photo2=ImageTk.PhotoImage(img)
        photo_label2=Label(root2,image=photo2)
        photo_label2.grid(row=1,column=4)
        Bustype=Label(root2,text="Bus type").grid(row=2)
        Button(text="Bus type",bg="grey",fg="#B0E0E6").grid(row=2,column=4)
        from1=Label(root2,text="from").grid(row=3)
        to=Label(root2,text="to").grid(row=4)
        date=Label(root2,text="date").grid(row=5)

        fromvar=StringVar()
        tovar=StringVar()
        datevar=StringVar()

        fromentry=Entry(root2,textvariable=fromvar).grid(row=3,column=4)
        toentry=Entry(root2,textvariable=tovar).grid(row=4,column=4)
        dateentry=Entry(root2,textvariable=datevar).grid(row=5,column=4)
        def home():
            root2.destroy()
            fun()
        Button(text="Home",bg="grey",fg="#B0E0E6",command=home).grid(row=6)
        def search():
            con=sqlite3.Connection('My_db')
            cur=con.cursor()
            root2.destroy()
            root3=Tk()
            root3.geometry('500x400')
            head_label3=Label(root3,text="BUS BOOKING SYSTEM",bg="#D8BFD8",font=("bold","10"))
            head_label3.config(anchor="center")
            head_label3.grid(row=0)
            name=Label(root3,text="operator",font=('bold',"12"),padx=-5).grid(row=2,column=0)
            from2=Label(root3,text="from",font=('bold',"12"),padx=5).grid(row=2,column=1)
            to=Label(root3,text="to",font=('bold',"12"),padx=5).grid(row=2,column=2)
            dep=Label(root3,text="dep",font=('bold',"12"),padx=5).grid(row=2,column=3)
            arr=Label(root3,text="arr",font=('bold',"12"),padx=5).grid(row=2,column=4)
            fare=Label(root3,text="fare",font=('bold',"12"),padx=5).grid(row=2,column=5)
            seat=Label(root3,text="seat",font=('bold',"12"),padx=5).grid(row=2,column=6)
            #Button(text="book",bg="grey",fg="#B0E0E6").config(anchor="se")
            def book():
                messagebox.showinfo("book status","booked")
                root3.destroy()
                fun()
            Button(text="book",bg="grey",fg="#B0E0E6",command=book).grid(column=8,sticky='nw')
            fromv=fromvar.get()
            cur.execute("SELECT * FROM travel1 WHERE from1=(?)",(fromv,))#fetch from database
            store=cur.fetchall()
            con.close()
            print(store)
            num=3
            for i in store:
                print(i)
                n=1
                v=IntVar()
                name2=Label(root3,text=i[0]).grid(row=num)
                from2=Label(root3,text=i[1]).grid(row=num,column=1)
                to=Label(root3,text=i[2]).grid(row=num,column=2)
                dep=Label(root3,text=i[3]).grid(row=num,column=3)
                arr=Label(root3,text=i[4]).grid(row=num,column=4)
                fare=Label(root3,text=i[5]).grid(row=num,column=5)
                seat=Label(root3,text=i[6]).grid(row=num,column=6)
                radio=Radiobutton(root3,variable=v,value=n).grid(row=num,column=7)
                
                n+1
                num=num+1

            
        Button(text="Search",bg="grey",fg="#B0E0E6",command=search).grid(row=6,column=4)
        
    b2=Button(f1,bg="#F5FFFA",text="Search BUS",padx=4,pady=4,fg="#A9A9A9",command=search_bus)
    b2.pack(side=RIGHT,padx=20)
    def delete():
        con=sqlite3.Connection('My_db')
        cur=con.cursor()
        cur.execute("DELETE FROM travel1")
        con.commit()
    b3=Button(f1,bg="#F5FFFA",text="delete",padx=4,pady=4,fg="#A9A9A9",command=delete)
    b3.pack(side=RIGHT,padx=20)


    

    Label(root,text="Shrey",bg="#949092",fg="#B20414",font=("bold",15)).pack(pady=5)
    Label(root,text="191B242",bg="#949092",fg="#B20414",font=("bold",15)).pack()
    Label(root,text="B7",bg="#949092",fg="#B20414",font=("bold",15)).pack()
    root.mainloop()

fun()




