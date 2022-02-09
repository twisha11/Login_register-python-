from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import *
import pymysql
from tkinter import messagebox

class Log:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN")
        self.root.geometry("1350x700+0+0")
        # self.root.config(bg="#021e2f")

        # title=Label(self.root, text="Welcome", font=("times new roman",50,"bold"),bg="#04444a",fg="white")
        # title.pack(fill="x",pady=10)

        # -----background image----
        self.lbl_l = Label(self.root, bg="#22bbf2", bd=0)
        self.lbl_l.place(x=0, y=0, width=400, relheight=1)

        self.lbl_r = Label(self.root, bg="#021e2f", bd=0)
        self.lbl_r.place(x=400, y=0, relwidth=1, relheight=1)

        # ----frame login
        self.frame_log=Frame(self.root, bg="white")
        self.frame_log.place(x=300,y=100,width=900,height=500)

        self.lb=Label(self.frame_log,text="Login Here",bg="white",fg="#22bbf2",
                      font=("times new roman ",25,"bold"))
        self.lb.place(x=80,y=60)




        # --------
        self.lb = Label(self.frame_log, text="Email Address", bg="white",
                        font=("times new roman ", 14))
        self.lb.place(x=80, y=160)

        self.en = Entry(self.frame_log, font=("times new roman ", 14), bd=5)
        self.en.place(x=250, y=160)

        self.lb = Label(self.frame_log, text="Password", bg="white",
                        font=("times new roman ", 14))
        self.lb.place(x=80, y=240)

        self.en1 = Entry(self.frame_log, font=("times new roman ", 14), bd=5)
        self.en1.place(x=250, y=240)

        self.btn_log = Button(self.frame_log, text="Register NewUser ?",command=self.reg_win,
                              font=("times new roman ", 11, "bold"),fg="red", bg="white", bd=0)
        self.btn_log.place(x=250, y=280)

        self.btn_log1 = Button(self.frame_log, text="Forget password?", command=self.frg_pwd_win,
                              font=("times new roman ", 11, "bold"), fg="green", bg="white", bd=0)
        self.btn_log1.place(x=400, y=280)

        self.btn_log2 = Button(self.frame_log, text="LogIn", command=self.login1,
                              font=("times new roman ", 14,"bold") ,bg="#22bbf2" ,fg="white")
        self.btn_log2.place(x=250, y=350, width=130)



        # ---clock image---
        self.lbl=Label(self.root, bg="#1a1d21", bd=10)
        self.lbl.place(x=50, y=150, width=300, height=400)

        self.working()

    def reset(self):
        self.e5.current(0)
        self.e6.delete(0,END)
        self.e7.delete(0,END)
        self.en.delete(0,END)


    def frg_pwd(self):
        if self.e5.get() == "Select" or self.e6.get() == "" or self.e7.get() == "":
            messagebox.showerror("Error","Please Fill All Field", parent=self.root2)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="py_reg")
                cur = con.cursor()
                cur.execute("select * from reg where email=%s and question=%s and answer=%s", (self.en.get(),self.e5.get(),self.e6.get() ))
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Please Enter Correct Information",
                                         parent=self.root2)

                else:
                    cur.execute("update reg set password=%s where email=%s",(self.e7.get(), self.en.get()))
                    con.commit() # for update password in database
                    con.close()
                    messagebox.showinfo("Update Success","your password Update Sucessfully",parent=self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root2)

    def frg_pwd_win(self):
        if self.en.get() == "":
            messagebox.showerror("Error","please enter email address",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="py_reg")
                cur = con.cursor()
                cur.execute("select * from reg where email=%s",self.en.get())
                row = cur.fetchone()
                # print(row)
                if row == None:
                    messagebox.showerror("Error", "Please Enter Valid Email Address To Reset Your Password", parent=self.root)

                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x500+435+100")
                    self.root2.config(bg="white")
                    self.root2.focus_force()  # new root ne by-defult automatically focus krva mate used thai che
                    self.root2.grab_set()  # new root ni bahar click krvathi bndh na thai jai tena mate used thai che

                    self.fl1 = Label(self.root2, text="Security Quastions", fg="#04c40a", bg="white",
                                     font=('times new roman', 15, 'bold'))
                    self.fl1.place(x=60, y=60)

                    self.e5 = ttk.Combobox(self.root2, font=('times new roman', 12), state='readonly')
                    self.e5['values'] = ("Select", "Your Pet Name", "Your Birth Name", "Your Best Fried Name")
                    self.e5.current(0)
                    self.e5.place(x=60, y=100, width=280)

                    # --------------
                    self.fl2 = Label(self.root2, text="Answer", fg="#04c40a", bg="white",
                                     font=('times new roman', 15, 'bold'))
                    self.fl2.place(x=60, y=140)

                    self.e6 = Entry(self.root2, font=('times new roman', 15), bd=2)
                    self.e6.place(x=60, y=180, width=280)

                    self.fl3 = Label(self.root2, text="New Password", fg="#04c40a", bg="white",
                                     font=('times new roman', 15, 'bold'))
                    self.fl3.place(x=60, y=220)

                    self.e7 = Entry(self.root2, font=('times new roman', 15), bd=2)
                    self.e7.place(x=60, y=260, width=280)

                    self.btn_fg = Button(self.root2, text="Set New Password", font=('times new roman', 15, 'bold'),
                                         fg="#04c40a", relief=GROOVE, command=self.frg_pwd)
                    self.btn_fg.place(x=110, y=340)



            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    # ------switch to register page---
    def reg_win(self):
        self.root.destroy()
        import reg

    # ------------------------------

    def login1(self):
        if self.en.get() == "" or self.en1.get() == "":
            messagebox.showerror("Error","Please fill all the field",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="", database="py_reg")
                cur=con.cursor()
                cur.execute("select * from reg where email=%s and password=%s", (self.en.get(), self.en1.get()))
                row=cur.fetchone()
                 # print(row)
                if row == None:
                    messagebox.showerror("Error", "Username And Password are not Correct", parent=self.root)

                else:
                    a=row[1]
                    messagebox.showinfo("Welcome", f"hey {a}", parent=self.root)
                con.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to:{str(es)}", parent=self.root)

    def clock_img(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (25, 26, 25))
        draw = ImageDraw.Draw(clock)

        # ----for clock image
        bg=Image.open("img/w2.jpg")
        bg=bg.resize((300,300), Image.ANTIALIAS) # 'Image.ANTIALIAS' image clearing bagde na aena mate used thai che
        clock.paste(bg,(50,50)) # x thi 50 space lese and  y thi 50 space lese

        # formula for Rotate the clock

        # end_x=center_x-line_length * math.sin(angle_in_radiasion)
        # end_y=center_y+line_length * math.cos(angle_in_radiasion)


        # -----hour line image
        origin=200,200
        draw.line((origin, 200+40*sin(radians(hr)), 200-40*cos(radians(hr))), fill="green", width=4) # 240

        # -----Minute line image
        draw.line((origin, 200+60*sin(radians(min_)), 200-60*cos(radians(min_))), fill="red", width=4) # 260

        # -----second line image
        draw.line((origin, 200+70*sin(radians(sec_)), 200-70*cos(radians(sec_))), fill="orange", width=3) # 270
        draw.ellipse((195,195,210,210),fill="black")

        clock.save("img/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
         # print(h,m,s)

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        # print(hr,min_,sec_)
        self.clock_img(hr,min_,sec_)
        self.img = ImageTk.PhotoImage(file="img/clock_new.png")
        self.lbl.config(image=self.img)

        self.lbl.after(200,self.working)

root = Tk()
obj = Log(root)
root.mainloop()