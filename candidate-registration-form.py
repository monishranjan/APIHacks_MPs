from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image
from PIL import ImageTk


class Main_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting System")
        root.geometry("1080x720+0+0")
        Label(text = "New Candidate Registration", bg = 'grey', width = '300', height = '3', font = ("Elephant", 30, "bold")).pack()


        #===Registration Frame===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=200, y=115, width=700, height=500)

        title = Label(frame1, text = "REGISTER HERE", font = ("times new roman", 20, "bold"), bg = "white", fg = "green").place(x=50, y=30)

        #---------------Row 1
        
        f_name = Label(frame1, text = "First/Middle Name", font = ("Calibri", 17, "bold"), bg = "white", fg = "green").place(x=50, y=83)
        self.txt_fname = Entry(frame1, font = ("Calibri", 15), bg = "lightgray")
        self.txt_fname.place(x=50, y=111, width=250)
        
        l_name = Label(frame1, text = "Last Name", font = ("Calibri", 17, "bold"), bg = "white", fg = "green").place(x=370, y=83)
        self.txt_lname = Entry(frame1, font = ("Calibri", 15), bg = "lightgray")
        self.txt_lname.place(x=370, y=111, width=250)

        #---------------Row 2
        party_name = Label(frame1, text = "Party Name", font = ("Calibri", 17, "bold"), bg = "white", fg = "green").place(x=50, y=160)
        self.txt_partyname = Entry(frame1, font = ("Calibri", 15), bg = "lightgray")
        self.txt_partyname.place(x=50, y=191, width=250)
        
        #---------------Row 3
        username = Label(frame1, text = "Username", font = ("Calibri", 17, "bold"), bg = "white", fg = "green").place(x=50, y=237)
        self.txt_username = Entry(frame1, font = ("Calibri", 15), bg = "lightgray")
        self.txt_username.place(x=50, y=271, width=250)

        #---------------Row 4
        password = Label(frame1, text = "Password", font = ("Calibri", 17, "bold"), bg = "white", fg = "green").place(x=50, y=314)
        self.txt_password = Entry(frame1, font = ("Calibri", 15), bg = "lightgray")
        self.txt_password.place(x=50, y=351, width=250)

        #--------------Row 5
        btn1 = Button(frame1, text = 'Register', font = ('Calibri', 17, "bold"), bg = "grey", fg = "black", cursor="hand2", command = self.register_data).place(x=50, y=400)

        #--------------Row 6
        btn2 = Button(frame1, text = 'Login', font = ('Calibri', 17, "bold"), bg = "grey", fg = "black").place(x=200, y=400)

    def register_data(self):
        if self.txt_fname.get()=="" or  self.txt_lname.get()=="" or self.txt_partyname.get()=="" or self.txt_username.get()=="" or self.txt_password.get()=="":
            messagebox.showerror("Error", "All Fields are mandatory", parent=self.root)
        else:
            messagebox.showinfo("success", "Register Successful", parent=self.root)


root = Tk()
obj = Main_Window(root)
root.mainloop()
