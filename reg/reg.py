from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox  # ttk provide us combo box
import pymysql   # for connect mysql


class Register:
    def __init__(self, root):
        self.root = root  # intializaion root
        self.root.title("Welcome")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("img/notebook.ico")

        #----bg image
        self.bg = Image.open("img/bg3.jpg")
        self.resize_image1 = self.bg.resize((1366, 768))       # (width,height)
        self.Img1 = ImageTk.PhotoImage(self.resize_image1)
        img_lable1 = Label(self.root, image=self.Img1)
        img_lable1.place(x=0, y=0)

        # -----side image
        self.image = Image.open("img/im1.jpg")
        self.resize_image = self.image.resize((300, 500))
        self.Img = ImageTk.PhotoImage(self.resize_image)
        img_lable = Label(self.root, image=self.Img)
        img_lable.place(x=130, y=100, width=300, height=500)
# ----------------------------------------------------------------------------------------------------------------------
        # -----frame
        self.frame = Frame(self.root, bg="white")
        self.frame.place(x=430, y=100, width=800, height=500)

        #-----title
        self.title=Label(self.frame, text="REGISTER HERE", fg="#04c40a", bg="white", font=('Algerian',25,'bold'))
        self.title.grid(row=0, column=0, padx=5, pady=20)

        # -----row1
        self.l1 = Label(self.frame, text="First Name", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l1.place(x=15, y=100)

        self.e1 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e1.place(x=15, y=130,width=250)

        # ------------
        self.l2 = Label(self.frame, text="Last Name", fg="#04c40a", bg="white",
                        font=('times new roman', 15, 'bold'))
        self.l2.place(x=300, y=100)

        self.e2 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e2.place(x=300, y=130,width=300)
        # -----------

        #-----row2
        self.l3 = Label(self.frame, text="Phone Number", fg="#04c40a", bg="white",
                        font=('times new roman', 15, 'bold'))
        self.l3.place(x=15, y=170)

        self.e3 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e3.place(x=15, y=200, width=250)

        # ----------
        self.l4 = Label(self.frame, text="Email", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l4.place(x=300, y=170)

        self.e4 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e4.place(x=300, y=200,width=300)
        # ----------

        # ----row3
        self.l5 = Label(self.frame, text="Security Quastions", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l5.place(x=15, y=240)

        self.e5 = ttk.Combobox(self.frame, font=('times new roman', 15), state='readonly')
        self.e5['values']=("Select","Your Pet Name","Your Birth Name","Your Best Fried Name")
        self.e5.current(0)
        self.e5.place(x=15, y=270, width=250)

        # --------------
        self.l6 = Label(self.frame, text="Answer", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l6.place(x=300, y=240)

        self.e6 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e6.place(x=300, y=270, width=300)
        # -------------

        #----
        self.l7 = Label(self.frame, text="Password", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l7.place(x=15, y=320)

        self.e7 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e7.place(x=15, y=350, width=250)

        # ------------
        self.l8 = Label(self.frame, text="Confirm Password", fg="#04c40a", bg="white", font=('times new roman', 15, 'bold'))
        self.l8.place(x=300, y=320)

        self.e8 = Entry(self.frame, font=('times new roman', 15, 'bold'), bd=3)
        self.e8.place(x=300, y=350, width=300)
        # --------------
        # ---chk
        self.chk_var = IntVar()
        self.chk = Checkbutton(self.frame, text="I Agree The Term & Conditions", variable=self.chk_var, font=('times new roman', 12),
                               bg="white", onvalue=1, offvalue=0)
        self.chk.place(x=15, y=400)
        # ----btn

        # self.btn_reg = ImageTk.PhotoImage(file="img/loginbtn.jpg")
        # self.btn_sub=Button(self.frame,image=self.btn_reg)
        # self.btn_sub.place(x=15, y=440)

        self.btn_reg = Button(self.frame, text="Register", font=('times new roman',15,'bold'),
                              relief=GROOVE, bg="#04c40a", command=self.reg_data)
        self.btn_reg.place(x=15, y=440, width=150)

        # ---login btn
        log_btn = Button(self.frame, text="Login here",bd=0, font=('times new roman', 15, 'bold'),
                         bg="white" , fg="#04c40a", command=self.log_win)
        log_btn.place(x=170, y=440)

# ----------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.e5.current(0)
        self.e6.delete(0, END)
        self.e7.delete(0, END)
        self.e8.delete(0, END)

    # -----regster page-----
    def reg_data(self):
        if self.e1.get()=="" or self.e3.get()=="" or self.e4.get()=="" or self.e5.get()=="Select" or self.e6.get()=="" or self.e7.get()=="" or self.e8.get()=="":
            messagebox.showerror("Error", "All Field are require", parent=self.root)
        elif self.e7.get() != self.e8.get():
            messagebox.showinfo("Password", "Password & Confirm Password Not Match", parent=self.root)
        elif self.chk_var.get() == 0:
            messagebox.showerror("Error", "Please Agree Terms & Conditions", parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost", user="root", password="",database="py_reg")
                cur=con.cursor()
                cur.execute("select * from reg where email=%s", self.e4.get())
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "Email Already Register", parent=self.root)
                else:
                    cur.execute(
                        "insert into reg(f_name, l_name, contact, email, question,answer, password) "
                        "values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.e1.get(),
                         self.e2.get(),
                         self.e3.get(),
                         self.e4.get(),
                         self.e5.get(),
                         self.e6.get(),
                         self.e7.get())
                        )
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Successfully Completed", parent=self.root)
                    self.clear()

            except Exception as es:
                messagebox.showerror("Error", f"Error Occure Due To: {str(es)}", parent=self.root)

    # --------------------------------------------------------------------------------------------

    # ---switch to login page
    def log_win(self):
        self.root.destroy()
        import log
    # -----------------------





root = Tk()

obj = Register(root)  # 'Register' class nu obj che

root.mainloop()
