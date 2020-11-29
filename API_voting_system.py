import tkinter
from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import simpledialog
import sqlite3 as sql
from tkinter import filedialog as fd
import csv
from candidate_registartion import Register

conn=sql.connect('main.db')
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS poll
                    (name)""")

def pollpage(): #page for polling
     def proceed():
        chose=choose.get()
        print(chose)
        command='update polling set votes=votes+1 where name=?'
        pd.execute(command,(chose,))
        pd.commit()
        messagebox.showinfo('Success!','You have voted')
     choose=StringVar()
     names=[]
     pd=sql.connect(screen01+'.db') #poll database
     pcursor=pd.cursor() #poll cursor
     pcursor.execute('select name from polling')
     data=pcursor.fetchall()
     for i in range(len(data)):
         data1=data[i]
         ndata=data1[0]
         names.append(ndata)
     print(names)
     ppage=Toplevel()
     ppage.geometry('300x300')
     ppage.title('Poll')


     Label(ppage,text='Vote for any one person!').grid(row=1,column=3)
     for i in range(len(names)):
         Radiobutton(ppage,text=names[i],value=names[i],variable=choose).grid(row=2+i,column=1)
     Button(ppage,text='Vote',command=proceed).grid(row=2+i+1,column=2)

def login_success2():
    global screen7
    screen7 = Toplevel()
    screen7.title("Login Successful")
    screen7.geometry("100x90")
    Label(screen7, text = 'Login Success', fg = 'green', font = ('Calibri', 11)).pack()
    Button(screen7, text = "OK", command = polls).pack()

def password_incorrect2():
    global screen4
    screen4 = Tk()
    screen4.title("Password Incorrect")
    screen4.geometry("140x90")
    Label(screen4, text = 'Incorrect Password', fg = 'red', font = ('Calibri', 11)).pack()
    Button(screen4, text = "OK", command = delete2).pack()

def user_not_found2():
    global screen4
    screen4 = Tk()
    screen4.title("User not Found")
    screen4.geometry("170x90")
    Label(screen4, text = 'Register First to Login', font = ('Calibri', 11)).pack()
    Button(screen4, text = "Register", command = register2).pack()

def register_user1():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info , "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen2, text = "Registration Successful !!", fg = 'blue', font = ('Calibri', 11)).pack()

def login_verify2():

    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success2()
        else:
            password_incorrect2()
    else:
        user_not_found2()

def register2():
    global screen2

    screen2 = Toplevel(image_scree)
    screen2.title("Register")
    screen2.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry
    global text_write
    global Aadhar
    global party_entry
    global party
    global age
    global age_in
    global name
    global naam

    username = StringVar()
    password = StringVar()
    Aadhar = StringVar()
    party = StringVar()
    naam = StringVar()
    Label(screen2, text = 'Please enter details below', font=('Calibri',11)).pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Username  ').pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    Label(screen2, text = 'Password  ').pack()
    password_entry = Entry(screen2, textvariable = password, show='*')
    password_entry.pack()
    Label(screen2, text="Enter your name").pack()
    name = Entry(screen2, textvariable = 'naam')
    name.pack()
    Label(screen2, text='Aadhar Number').pack()
    text_write = Entry(screen2, textvariable=(Aadhar))
    text_write.pack()
    Label(screen2, text='Party Name').pack()
    party_entry = Entry(screen2, textvariable='party')
    party_entry.pack()
    Label(screen2, text='Gender').pack()
    var = IntVar()
    Radiobutton(screen2, text="Male", variable=var, value=1).pack()
    Radiobutton(screen2, text="Female", variable=var, value=2).pack()
    Radiobutton(screen2, text="Others", variable=var, value=3).pack()
    Label(screen2, text='Age').pack()
    age_in = Entry(screen2, textvariable='age')
    age_in.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Register', width = 10, height = 1,bg='brown', command = register_user1).pack()

def login2():
    global screen3
    screen3 = Toplevel(image_scree)
    screen3.title("Login")
    screen3.geometry("500x350")
    Label(screen3, text = 'Please enter details below to login').pack()
    Label(screen3, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen3, text = 'Username * ').pack()
    username_entry1 = Entry(screen3, textvariable = username_verify)
    username_entry1.pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = 'Password * ').pack()
    password_entry1 = Entry(screen3, textvariable = password_verify)
    password_entry1.pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Login", width = 10, height = 1, command = login_verify2).pack()


def polls():
    def proceed():
        global screen01
        screen01=psel.get()
        if screen01=='-select-':
            return messagebox.showerror('Error','select poll')
        else:
            mpolls.destroy()
            pollpage()
    cursor.execute('Select name from poll')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    psel=StringVar()
    mpolls=Toplevel()
    mpolls.geometry('270x200')
    mpolls.title('Voting Program')
    Label(mpolls,text='Select Poll',font='Calibri 12 bold').grid(row=1,column=3)
    select=ttk.Combobox(mpolls,values=pollnames,state='readonly',textvariable=psel)
    select.grid(row=2,column=3)
    select.current(0)
    Button(mpolls,text='Proceed',command=proceed).grid(row=2,column=4)

def work_admin():
    def selpl(): #pollresults
        def results():
            sel=sele.get()  #selected option
            if sel=='-select-':
                return messagebox.showerror('Error','Select Poll')
            else:
                pl.destroy()
                def project():
                    names=[]
                    votes=[]
                    for i in range(len(r)):
                        data=r[i]
                        names.append(data[0])
                        votes.append(data[1])
                        plt.title('Poll Result')
                    plt.pie(votes,labels=names,autopct='%1.1f%%',shadow=True,startangle=140)
                    plt.axis('equal')
                    plt.show()

                res=Toplevel() #result-page
                res.geometry('300x300')
                res.title('Results!')
                Label(res,text='Here is the Result!',font='Helvetica 12 bold').grid(row=1,column=2)
                con=sql.connect(sel+'.db')
                pcursor=con.cursor()
                pcursor.execute('select * from polling')
                r=pcursor.fetchall() #data-raw
                for i in range(len(r)):
                    data=r[i]
                    Label(res,text=data[0]+': '+str(data[1])+' votes').grid(row=2+i,column=1)
                Button(res,text='Project Results',command=project).grid(row=2+i+1,column=2)


        cursor.execute('select name from poll')
        data=cursor.fetchall()
        pollnames=['-select-']
        for i in range(len(data)):
            data1=data[i]
            ndata=data1[0]
            pollnames.append(ndata)
        sele=StringVar()
        pl=Toplevel()
        pl.geometry('300x200')
        pl.title('Voting System')
        Label(pl,text='Select Poll',font='Helvetica 12 bold').grid(row=1,column=1)
        sel=ttk.Combobox(pl,values=pollnames,state='readonly',textvariable=sele)
        sel.grid(row=2,column=1)
        sel.current(0)
        Button(pl,text='Get Results',command=results).grid(row=2,column=2)


    def create():
        def proceed():
            global pcursor
            pname=name.get()
            can=cname.get()
            if pname=='':
                return messagebox.showerror('Error','Enter poll name')
            elif can=='':
                return messagebox.showerror('Error','Enter candidates')
            else:
                candidates=can.split(',')
                command='insert into poll (name) values (?);'
                cursor.execute(command,(pname,))
                conn.commit()
                pd=sql.connect(pname+'.db')
                pcursor=pd.cursor()
                pcursor.execute("""CREATE TABLE IF NOT EXISTS polling
                     (name TEXT,votes INTEGER)""")
                for i in range(len(candidates)):
                    command='insert into polling (name,votes) values (?, ?)'
                    data=(candidates[i],0)
                    pcursor.execute(command,data)
                    pd.commit()
                pd.close()
                messagebox.showinfo('Success','Poll Created')
                cr.destroy()

        name=StringVar()
        cname=StringVar()
        cr=Toplevel()
        cr.geometry('500x400')
        cr.title('Create a new poll')
        Label(cr,text='Enter Details',font='Calibri 12 bold').grid(row=1,column=2)
        Label(cr,text='Enter Poll name: ').grid(row=2,column=1)
        Entry(cr,width=30,textvariable=name).grid(row=2,column=2)
        Label(cr,text='Enter Candidates: ').grid(row=3,column=1)
        Entry(cr,width=45,textvariable=cname).grid(row=3,column=2)
        Button(cr,text='Proceed',command=proceed).grid(row=6,column=2)
    def selpl():
        def results():
            sel=sele.get()
            if sel=='-select-':
                return messagebox.showerror('Error','Select Poll')
            else:
                pl.destroy()
                def project():
                    names=[]
                    votes=[]
                    for i in range(len(r)):
                        data=r[i]
                        names.append(data[0])
                        votes.append(data[1])
                        plt.title('Poll Result')
                    plt.pie(votes,labels=names,autopct='%1.1f%%',shadow=True,startangle=140)
                    plt.axis('equal')
                    plt.show()

                res=Toplevel() #result-page
                res.geometry('300x300')
                res.title('Results!')
                Label(res,text='Here is the Result!',font='Calibri 12 bold').grid(row=1,column=2)
                con=sql.connect(sel+'.db')
                pcursor=con.cursor()
                pcursor.execute('select * from polling')
                r=pcursor.fetchall()
                for i in range(len(r)):
                    data=r[i]
                    Label(res,text=data[0]+': '+str(data[1])+' votes').grid(row=2+i,column=1)
                Button(res,text='Project Results',command=project).grid(row=2+i+1,column=2)


        cursor.execute('Select name from poll')
        data=cursor.fetchall()
        pollnames=['-select-']
        for i in range(len(data)):
            data1=data[i]
            ndata=data1[0]
            pollnames.append(ndata)
        sele=StringVar()
        pl=Toplevel()
        pl.geometry('300x200')
        pl.title('Voting System')
        Label(pl,text='Select Poll',font='Calibri 12 bold').grid(row=1,column=1)
        sel=ttk.Combobox(pl,values=pollnames,state='readonly',textvariable=sele)
        sel.grid(row=2,column=1)
        sel.current(0)
        Button(pl,text='Get Results',command=results).grid(row=2,column=2)

    def about():
        messagebox.showinfo('About',"Developed by MP's group for API hackathon")

    Main_window=Toplevel()
    Main_window.geometry('400x400')
    Main_window.title('Voting Program')
    Main_window['bg'] = 'grey'
    Label(Main_window,text='Welcome, What do you want to do?',font='Calibri 16 bold',bg='grey').pack()
    Button(Main_window,text='Create A Poll',command=create).pack()
    Label(Main_window,text=" ")
    Label(Main_window,text=" ")
    Button(Main_window,text='Poll Results',command=selpl).pack()
    Button(Main_window,text='About',command=about).pack()

def login_success1():
    global screen7
    screen7 = Toplevel()
    screen7.title("Login Successful")
    screen7.geometry("100x90")
    Label(screen7, text = 'Login Success', fg = 'green', font = ('Calibri', 11)).pack()
    Button(screen7, text = "OK", command = work_admin).pack()

def password_incorrect1():
    global screen4
    screen4 = Tk()
    screen4.title("Password Incorrect")
    screen4.geometry("140x90")
    Label(screen4, text = 'Incorrect Password', fg = 'red', font = ('Calibri', 11)).pack()
    Button(screen4, text = "OK", command = delete2).pack()

def user_not_found1():
    global screen4
    screen4 = Tk()
    screen4.title("User not Found")
    screen4.geometry("170x90")
    Label(screen4, text = 'Register First to Login', font = ('Calibri', 11)).pack()
    Button(screen4, text = "Register", command = register1).pack()

def login_verify1():

    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success1()
        else:
            password_incorrect1()
    else:
        user_not_found1()


def register1():
    global screen2

    screen2 = Toplevel(image_scree)
    screen2.title("Register")
    screen2.geometry("500x500")

    global username
    global password
    global username_entry
    global password_entry
    global text_write
    global Aadhar
    global party_entry
    global party
    global age
    global age_in
    global name
    global naam

    username = StringVar()
    password = StringVar()
    Aadhar = StringVar()
    party = StringVar()
    naam = StringVar()
    Label(screen2, text = 'Please enter details below', font=('Calibri',11)).pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Username  ').pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    Label(screen2, text = 'Password  ').pack()
    password_entry = Entry(screen2, textvariable = password, show='*')
    password_entry.pack()
    Label(screen2, text="Enter your name").pack()
    name = Entry(screen2, textvariable = 'naam')
    name.pack()
    Label(screen2, text='Aadhar Number').pack()
    text_write = Entry(screen2, textvariable=(Aadhar))
    text_write.pack()
    Label(screen2, text='Party Name').pack()
    party_entry = Entry(screen2, textvariable='party')
    party_entry.pack()
    Label(screen2, text='Gender').pack()
    var = IntVar()
    Radiobutton(screen2, text="Male", variable=var, value=1).pack()
    Radiobutton(screen2, text="Female", variable=var, value=2).pack()
    Radiobutton(screen2, text="Others", variable=var, value=3).pack()
    Label(screen2, text='Age').pack()
    age_in = Entry(screen2, textvariable='age')
    age_in.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Register', width = 10, height = 1,bg='brown', command = register_user).pack()

def login1():
    global screen3
    screen3 = Toplevel(image_scree)
    screen3.title("Login")
    screen3.geometry("500x350")
    Label(screen3, text = 'Please enter details below to login').pack()
    Label(screen3, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen3, text = 'Username * ').pack()
    username_entry1 = Entry(screen3, textvariable = username_verify)
    username_entry1.pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = 'Password * ').pack()
    password_entry1 = Entry(screen3, textvariable = password_verify)
    password_entry1.pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Login", width = 10, height = 1, command = login_verify1).pack()


def delete2():
    screen4.destroy()

def login_success():
    global screen4
    screen4 = Toplevel()
    screen4.title("Login Successful")
    screen4.geometry("100x90")
    Label(screen4, text = 'Login Success', fg = 'green', font = ('Calibri', 11)).pack()
    Button(screen4, text = "OK", command = delete2).pack()

def password_incorrect():
    global screen4
    screen4 = Tk()
    screen4.title("Password Incorrect")
    screen4.geometry("140x90")
    Label(screen4, text = 'Incorrect Password', fg = 'red', font = ('Calibri', 11)).pack()
    Button(screen4, text = "OK", command = delete2).pack()

def user_not_found():
    global screen4
    screen4 = Tk()
    screen4.title("User not Found")
    screen4.geometry("170x90")
    Label(screen4, text = 'Register First to Login', font = ('Calibri', 11)).pack()
    Button(screen4, text = "Register", command = register).pack()

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info , "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen2, text = "Registration Successful !!", fg = 'blue', font = ('Calibri', 11)).pack()

def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_incorrect()
    else:
        user_not_found()

def register():
    global screen2

    screen2 = Toplevel(image_scree)
    screen2.title("Register")
    screen2.geometry("500x350")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen2, text = 'Please enter details below').pack()
    Label(screen2, text = '').pack()
    Label(screen2, text = 'Username * ').pack()
    username_entry = Entry(screen2, textvariable = username)
    username_entry.pack()
    Label(screen2, text = 'Password * ').pack()
    password_entry = Entry(screen2, textvariable = password)
    password_entry.pack()
    Label(screen2, text = '').pack()
    Button(screen2, text = 'Register', width = 10, height = 1, command = register_user).pack()

def login():
    global screen3
    screen3 = Toplevel(image_scree)
    screen3.title("Login")
    screen3.geometry("500x350")
    Label(screen3, text = 'Please enter details below to login').pack()
    Label(screen3, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen3, text = 'Username * ').pack()
    username_entry1 = Entry(screen3, textvariable = username_verify)
    username_entry1.pack()
    Label(screen3, text = "").pack()
    Label(screen3, text = 'Password * ').pack()
    password_entry1 = Entry(screen3, textvariable = password_verify)
    password_entry1.pack()
    Label(screen3, text = "").pack()
    Button(screen3, text = "Login", width = 10, height = 1, command = login_verify).pack()

def candidate_portal():
    global screen1
    screen1 = Toplevel(image_scree)
    screen1.geometry("500x350")
    screen1.title("Candidate Portal")
    Label(screen1,text = "Candidate Portal", bg = 'grey', width = '300', height = '2', font = ("Calibri", 14)).pack()
    Label(screen1,text = '').pack()
    Button(screen1,text = 'Login', height = '1', width = '10', command = login).pack()
    Label(screen1,text = '').pack()
    Button(screen1,text = 'Register', height = '1', width = '10', command = register1).pack()

def admin_portal():
    global screen5
    screen5 = Toplevel(image_scree)
    screen5.geometry("500x350")
    screen5.title("Admin Portal")
    Label(screen5,text = "Admin Portal", bg = 'green', width = '300', height = '2', font = {"Calibri", 14,"Bold"}).pack()
    Label(screen5,text = '').pack()
    Button(screen5,text = 'Login', height = '1', width = '10', command = login1).pack()
    Label(screen5,text = '').pack()
    Button(screen5,text = 'Register', height = '1', width = '10', command = register).pack()


def voter_portal():
    global screen9
    screen9 = Toplevel(image_scree)
    screen9.geometry("500x350")
    screen9.title("Admin Portal")
    Label(screen9,text = "Voter Portal", bg = 'red', width = '300', height = '2', font = ("Calibri", 14)).pack()
    Label(screen9,text = '').pack()
    Button(screen9,text = 'Login', height = '1', width = '10', command = login2).pack()
    Label(screen9,text = '').pack()
    Button(screen9,text = 'Register', height = '1', width = '10', command = Register).pack()

# the main screen from which we are accessing all the portals
def image_screen():
    global image_scree
    image_scree=Tk()
    image_scree.geometry("1000x1000")
    image_scree.title("Elections")
    Label(text="Welcome", bg="orange", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="to", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="Elections", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    photo = PhotoImage(file="candidate.png")
    Button(
    image_scree,
    image=photo,
    command=candidate_portal,
    border=0,
    height=200,
    width=200,
    ).pack()

    photo1 = PhotoImage(file='Admin.png')
    Button(
    image_scree,
    image=photo1,
    command=admin_portal,
    border=0,
    height=200,
    width=200,
    ).pack()

    photo2 = PhotoImage(file='Vote.png')
    Button(
    image_scree,
    image=photo2,
    command=voter_portal,
    border=0,
    height=200,
    width=200,
    ).pack()

    image_scree.mainloop()

image_screen()