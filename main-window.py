import tkinter
from tkinter import *
import os
from PIL import ImageTk, Image

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
    Button(screen1,text = 'Register', height = '1', width = '10', command = register).pack()

def admin_portal():
    global screen5
    screen5 = Toplevel(image_scree)
    screen5.geometry("500x350")
    screen5.title("Admin Portal")
    Label(screen5,text = "Admin Portal", bg = 'green', width = '300', height = '2', font = {"Calibri", 14,"Bold"}).pack()
    Label(screen5,text = '').pack()
    Button(screen5,text = 'Login', height = '1', width = '10', command = login).pack()
    Label(screen5,text = '').pack()    
    Button(screen5,text = 'Register', height = '1', width = '10', command = register).pack()

def voter_portal():
    global screen9
    screen9 = Toplevel(image_scree)
    screen9.geometry("500x350")
    screen9.title("Admin Portal")
    Label(screen9,text = "Voter Portal", bg = 'red', width = '300', height = '2', font = ("Calibri", 14)).pack()
    Label(screen9,text = '').pack()
    Button(screen9,text = 'Login', height = '1', width = '10', command = login).pack()
    Label(screen9,text = '').pack()    
    Button(screen9,text = 'Register', height = '1', width = '10', command = register).pack()

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

    photo1 = PhotoImage(file='admin.png')
    Button(
    image_scree,
    image=photo1,
    command=admin_portal,
    border=0,
    height=200,
    width=200,
    ).pack()

    photo2 = PhotoImage(file='voter.png')
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
