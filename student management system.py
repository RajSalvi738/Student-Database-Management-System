from tkinter import *
import tkinter.messagebox as messagebox
import stdDatabase

global sd

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT DATABSE MANAGEMENT SYSTEM")
        self.root.geometry("1350x7000+0+0")
        self.root.config(bg="cadet blue")

        stdID = StringVar()
        firstName = StringVar()
        lastName = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        #___________________Function__________________

        def iExit():
            iExit = messagebox.askyesno("STUDENT DATABSE MANAGEMENT SYSTEM","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtstdID.delete(0,END)
            self.txtfirst.delete(0,END)
            self.txtlast.delete(0,END)
            self.txtDoB.delete(0,END)
            self.txtAge.delete(0,END)
            self.txtGender.delete(0,END)
            self.txtAddr.delete(0,END)
            self.txtMobile.delete(0,END)

        def addData():
            if(len(stdID.get()) != 0):
                stdDatabase.addStdRec(stdID.get(), firstName.get(), lastName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (stdID.get(), firstName.get(), lastName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in stdDatabase.display():
                studentlist.insert(END, row)

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)

            self.txtstdID.delete(0,END)
            self.txtstdID.insert(END, sd[1])
            self.txtfirst.delete(0,END)
            self.txtfirst.insert(END, sd[2])
            self.txtlast.delete(0,END)
            self.txtlast.insert(END, sd[3])
            self.txtDoB.delete(0,END)
            self.txtDoB.insert(END, sd[4])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END, sd[5])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END, sd[6])
            self.txtAddr.delete(0,END)
            self.txtAddr.insert(END, sd[7])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END, sd[8])
        
        def DeleteData():
            global sd
            if(len(stdID.get()) != 0):
                stdDatabase.deleteRec(sd[0])
                clearData()
                DisplayData()

        def SearchData():
            studentlist.delete(0, END)
            for row in stdDatabase.SearchData(stdID.get(), firstName.get(), lastName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                studentlist.insert(END, row)

        def update():
            if(len(stdID.get()) != 0):
                stdDatabase.addStdRec(stdID.get(), firstName.get(), lastName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                studentlist.delete(0, END)
                studentlist.insert(END, (stdID.get(), firstName.get(), lastName.get(), DoB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))
                
        #________________________Frame___________________

        MainFrame = Frame(self.root, bg="cadet blue")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8,bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="student database management system", bg="Ghost White")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20,bg="cadet blue", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLeft = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20,bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text="Student Info\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="Ghost White", relief=RIDGE, font=('arial', 20, 'bold'), text="Student Details\n")
        DataFrameRight.pack(side=RIGHT)

        #_____________________Lsbel snd entry______________________

        self.lblstdID = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Student ID", padx=2, pady=2, bg="Ghost White")
        self.lblstdID.grid(row=0, column=0, sticky=W)
        self.txtstdID = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=stdID, width=39)
        self.txtstdID.grid(row=0, column=1)

        self.lblfirst = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="First Name", padx=2, pady=2, bg="Ghost White")
        self.lblfirst.grid(row=1, column=0, sticky=W)
        self.txtfirst = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=firstName, width=39)
        self.txtfirst.grid(row=1, column=1)

        self.lbllast = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Last Name", padx=2, pady=2, bg="Ghost White")
        self.lbllast.grid(row=2, column=0, sticky=W)
        self.txtlast = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=lastName, width=39)
        self.txtlast.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Date of Birth", padx=2, pady=3, bg="Ghost White")
        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=DoB, width=39)
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Age", padx=2, pady=3, bg="Ghost White")
        self.lblAge.grid(row=4, column=0, sticky=W)
        self.txtAge = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Age, width=39)
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Gender", padx=2, pady=3, bg="Ghost White")
        self.lblGender.grid(row=5, column=0, sticky=W)
        self.txtGender = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Gender, width=39)
        self.txtGender.grid(row=5, column=1)

        self.lblAddr = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Address", padx=2, pady=3, bg="Ghost White")
        self.lblAddr.grid(row=6, column=0, sticky=W)
        self.txtAddr = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Address, width=39)
        self.txtAddr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLeft, font=('arial', 20, 'bold'), text="Mobile NO.", padx=2, pady=3, bg="Ghost White")
        self.lblMobile.grid(row=7, column=0, sticky=W)
        self.txtMobile = Entry(DataFrameLeft, font=('arial', 20, 'bold'), textvariable=Mobile, width=39)
        self.txtMobile.grid(row=7, column=1)

        #__________________ScrollBar and ListBox_____________________________

        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')

        studentlist = Listbox(DataFrameRight, width=41, height=20,font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)

        scrollbar.config(command=studentlist.yview)

        #_________________Button___________________________________
        
        self.btnAddDate = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=clearData)
        self.btnClear.grid(row=0, column=2)

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)
        self.btnDelete.grid(row=0, column=3)
        
        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=SearchData)
        self.btnSearch.grid(row=0, column=4)

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=update)
        self.btnUpdate.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)
        


if __name__ == "__main__":
    root = Tk()
    application = student(root)
    root.mainloop()
