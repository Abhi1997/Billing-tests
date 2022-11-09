from email.mime import application
from logging import root
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from turtle import left
from tkcalendar import*
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr
import pymysql

class ItemOrder:

    def __init__(self,root):
        self.root = root
        self.root.title("Order Billing system")
        self.root.geometry("1350x800+0+0")

        Milk = IntVar()
        Cake = IntVar()
        Apple = IntVar()
        Bread = IntVar()
        Cola = IntVar()
        Orange = IntVar()
        Total = IntVar()

        MilkCost = StringVar()
        CakeCost = StringVar()
        AppleCost = StringVar()
        BreadCost = StringVar()
        ColaCost = StringVar()
        OrangeCost = StringVar()
        TotalCost = StringVar()

        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()

        RootFrame = Frame(self.root,bd=10,width=1350, height=700, relief=RIDGE)
        RootFrame.grid()

        MainFrame = Frame(RootFrame,bd=9,width=1350, height=700,bg='cadet blue', relief=RIDGE)
        MainFrame.grid()

        TopFrame3 = Frame(MainFrame,bd=8,width=1340, height=500, relief=RIDGE)
        TopFrame3.grid()

        LeftFrame = Frame(TopFrame3,bd=5,width=1340, height=400,padx=2,bg='cadet blue', relief=RIDGE)
        LeftFrame.pack(side= LEFT)

        TopName = Frame(TopFrame3,bd=5,width=340, height=400,bg='cadet blue', relief=RIDGE)
        TopName.pack(side= TOP)
        TopButton = Frame(TopFrame3,bd=5,width=340, height=100,bg='cadet blue', relief=RIDGE)
        TopButton.pack(side= BOTTOM)

        LeftFrame2 = Frame(LeftFrame,bd=5,width=600, height=180,padx=2,bg='cadet blue', relief=RIDGE)
        LeftFrame2.pack(side= TOP)
        LeftFrame2s = Frame(LeftFrame,bd=5,width=600, height=180,padx=0, relief=RIDGE)
        LeftFrame2s.pack(side= BOTTOM)

        CalendarFrame = LabelFrame(LeftFrame2,bd=5,width=300, height=170,padx=2,font=('arial',12,'bold'),text="Calendar", relief=RIDGE)
        CalendarFrame.pack(side= LEFT)

        LeftFrame3Right = LabelFrame(LeftFrame2,bd=5,width=600, height=180,padx=2,font=('arial',12,'bold'),text="Order System", relief=RIDGE)
        LeftFrame3Right.pack(side= RIGHT)

##==============================Calendar==========================================================================================================================================
        cal = Calendar(CalendarFrame, selectmode ="day",day=11, month= 4, year=2022, date_pattern='dd-mm-yyyy',font=('arial',12,'bold'),padx=10)
        cal.grid(row=0,column=0,pady=15)

 #========================================Exit=============================================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Billing System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

##====================================================================================================================================================================================
        def Enable_Apple():
                if var1.get()==1:
                        self.SpApple.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var1.get()==0:
                        self.SpApple.config(state = DISABLED)
                        Apple.set("0")
                        AppleCost.set("")

        def AppleItem():
                global q
                q = round(float(Apple.get()))
                p = str('$%.2f'%(q*23))
                AppleCost.set(p)

##====================================================================================================================================================================================
        def Enable_Milk():
                if var2.get()==1:
                        self.SpMilk.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var2.get()==0:
                        self.SpMilk.config(state = DISABLED)
                        Milk.set("0")
                        MilkCost.set("")

        def MilkItem():
                global q
                q = round(float(Milk.get()))
                p = str('$%.2f'%(q*4))
                MilkCost.set(p)
##====================================================================================================================================================================================
        def Enable_Cake():
                if var3.get()==1:
                        self.SpCake.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var3.get()==0:
                        self.SpCake.config(state = DISABLED)
                        Cake.set("0")
                        CakeCost.set("")

        def CakeItem():
                global q
                q = round(float(Cake.get()))
                p = str('$%.2f'%(q*13))
                CakeCost.set(p)
##====================================================================================================================================================================================
        def Enable_Bread():
                if var4.get()==1:
                        self.SpBread.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var4.get()==0:
                        self.SpBread.config(state = DISABLED)
                        Bread.set("0")
                        BreadCost.set("")

        def BreadItem():
                global q
                q = round(float(Bread.get()))
                p = str('$%.2f'%(q*11))
                BreadCost.set(p)
##====================================================================================================================================================================================
        def Enable_Cola():
                if var5.get()==1:
                        self.SpCola.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var5.get()==0:
                        self.SpCola.config(state = DISABLED)
                        Cola.set("0")
                        ColaCost.set("")

        def ColaItem():
                global q
                q = round(float(Cola.get()))
                p = str('$%.2f'%(q*9))
                ColaCost.set(p)
##====================================================================================================================================================================================
        def Enable_Orange():
                if var6.get()==1:
                        self.SpOrange.config(state = NORMAL)
                        self.calLabel.configure(text=cal.get_date())

                elif var6.get()==0:
                        self.SpOrange.config(state = DISABLED)
                        Orange.set("0")
                        OrangeCost.set("")

        def OrangeItem():
                global q
                q = round(float(Orange.get()))
                p = str('$%.2f'%(q*13))
                OrangeCost.set(p)

##====================================================================================================================================================================================
##make a message prompt for reset as well
        def Reset():
                var1.set(0)
                var2.set(0)
                var3.set(0)
                var4.set(0)
                var5.set(0)
                var6.set(0)
                var7.set(0)
                var8.set(0)
                var9.set(0)
                var10.set(0)

                self.SpApple.config(state = DISABLED)
                Apple.set("0")
                AppleCost.set("")

                self.SpMilk.config(state = DISABLED)
                Milk.set("0")
                MilkCost.set("")

                self.SpCake.config(state = DISABLED)
                Cake.set("0")
                CakeCost.set("")

                self.SpBread.config(state = DISABLED)
                Bread.set("0")
                BreadCost.set("")

                self.SpCola.config(state = DISABLED)
                Cola.set("0")
                ColaCost.set("")

                self.SpOrange.config(state = DISABLED)
                Orange.set("0")
                OrangeCost.set("")

                self.txtDetail.delete("1.0",END)

##====================================================================================================================================================================================
        def addData():
                sqlCon = pymysql.connect(host="127.0.0.1",port=3306, user="admin", password="admin",database="Billing_db")
                cur = sqlCon.cursor()
                cur.execute("Insert into Billing_db value(%s,%s,%s,%s,%s,%s)",(
                
                MilkCost.get() ,
                CakeCost.get() ,
                AppleCost.get() ,
                BreadCost.get() ,
                ColaCost.get() ,
                OrangeCost.get(),
                ))
                sqlCon.commit()
                Displaydata()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form","Record Entered Successfully")
                
        
        
##====================================================================================================================================================================================

        def Displaydata():
                sqlCon = pymysql.connect(host="127.0.0.1",port=3306, user="admin", password="admin",database="Billing_db")
                cur = sqlCon.cursor()
                cur.execute("Select * from Billing_db")
                result = cur.fetchall()
                if len(result) != 0:
                        self.ItemOrder_records.delete(*self.ItemOrder_records.get_children())
                        for row in result:
                                self.ItemOrder_records.insert('',END,values=row)
                        sqlCon.commit()
                        sqlCon.close()


##====================================================================================================================================================================================
        def Receipt():
                self.txtDetail.insert(END,'Item Name: \t\t'+('Number')+'\t'+('Cost of Item')+"\n")
                self.txtDetail.insert(END,'Apple Drink:\t\t'+str(Apple.get())+'\t'+(AppleCost.get())+"\n\n")
                self.txtDetail.insert(END,'Milk:\t\t'+str(Milk.get())+'\t'+(MilkCost.get())+"\n\n")
                self.txtDetail.insert(END,'Cake:\t\t'+str(Cake.get())+'\t'+(CakeCost.get())+"\n\n")
                self.txtDetail.insert(END,'Baked Bread:\t\t'+str(Bread.get())+'\t'+(BreadCost.get())+"\n\n")
                self.txtDetail.insert(END,'Cola:\t\t'+str(Cola.get())+'\t'+(ColaCost.get())+"\n\n")
                self.txtDetail.insert(END,'Orange Juice:\t\t'+str(Orange.get())+'\t'+(OrangeCost.get())+"\n\n")


##============================Check Button=================================================================================================================================================
        self.chkApple= Checkbutton(LeftFrame3Right, text="Apple Drink", onvalue=1,offvalue=0,variable=var1,font=('arial',16,'bold'),command= Enable_Apple).grid(row=0,column=0,sticky=W)

        self.SpApple= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Apple,state=DISABLED, command= AppleItem)
        self.SpApple.grid(row=0,column=1,pady=10)
        self.txtApple = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=AppleCost)
        self.txtApple.grid(row=0,column=2,padx=10)
##============================
        self.chkMilk= Checkbutton(LeftFrame3Right, text="Milk", onvalue=1,offvalue=0,variable=var2,font=('arial',16,'bold'),command= Enable_Milk).grid(row=1,column=0,sticky=W)

        self.SpMilk= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Milk,state=DISABLED, command= MilkItem)
        self.SpMilk.grid(row=1,column=1,pady=10)
        self.txtMilk = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=MilkCost)
        self.txtMilk.grid(row=1,column=2,padx=10)
##============================
        self.chkCake= Checkbutton(LeftFrame3Right, text="Cake", onvalue=1,offvalue=0,variable=var3,font=('arial',16,'bold'),command= Enable_Cake).grid(row=2,column=0,sticky=W)

        self.SpCake= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Cake,state=DISABLED, command= CakeItem)
        self.SpCake.grid(row=2,column=1,pady=10)
        self.txtCake = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=CakeCost)
        self.txtCake.grid(row=2,column=2,padx=10)
##============================
        self.chkBread= Checkbutton(LeftFrame3Right, text="Bread", onvalue=1,offvalue=0,variable=var4,font=('arial',16,'bold'), command= Enable_Bread).grid(row=3,column=0,sticky=W)

        self.SpBread= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Bread,state=DISABLED, command= BreadItem)
        self.SpBread.grid(row=3,column=1,pady=10)
        self.txtBread = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=BreadCost)
        self.txtBread.grid(row=3,column=2,padx=10)

##============================        
        self.chkCola= Checkbutton(LeftFrame3Right, text="Cola", onvalue=1,offvalue=0,variable=var5,font=('arial',16,'bold'), command= Enable_Cola).grid(row=4,column=0,sticky=W)

        self.SpCola= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Cola,state=DISABLED, command= ColaItem)
        self.SpCola.grid(row=4,column=1,pady=10)
        self.txtCola = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=ColaCost)
        self.txtCola.grid(row=4,column=2,padx=10)
##============================
        self.chkOrange= Checkbutton(LeftFrame3Right, text="Orange Drink", onvalue=1,offvalue=0,variable=var6,font=('arial',16,'bold'), command= Enable_Orange).grid(row=5,column=0,sticky=W)

        self.SpOrange= Spinbox(LeftFrame3Right,from_ =0, to=50,width=11,font=('arial',16,'bold'),textvariable=Orange,state=DISABLED, command= OrangeItem)
        self.SpOrange.grid(row=5,column=1,pady=10)
        self.txtOrange = Entry(LeftFrame3Right,font=('arial',12,'bold'),bd=5,width=30,justify='center',state= DISABLED,textvariable=OrangeCost)
        self.txtOrange.grid(row=5,column=2,padx=10)

        
##=============Scroll Bars===========================================================================================================================================================
        scroll_x=Scrollbar(LeftFrame2s, orient= HORIZONTAL)
        scroll_y=Scrollbar(LeftFrame2s, orient= VERTICAL)

        self.ItemOrder_records=ttk.Treeview(LeftFrame2s,height=12,columns=("AppleDrink","BakedBread","ColaDrink","OrangeDrink","MilkyBar","BrownCake"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.ItemOrder_records.heading("AppleDrink", text= "Apple Drink")
        self.ItemOrder_records.heading("BakedBread", text= "Baked Bread")
        self.ItemOrder_records.heading("ColaDrink", text= "Cola Drink")  
        self.ItemOrder_records.heading("OrangeDrink", text= "Orange Drink")
        self.ItemOrder_records.heading("MilkyBar", text= "Milky Bar")
        self.ItemOrder_records.heading("BrownCake", text= "Brown Cake")

        self.ItemOrder_records['show']='headings'
        
        
        self.ItemOrder_records.column("AppleDrink", anchor= 'center',width=180)
        self.ItemOrder_records.column("BakedBread", anchor= 'center',width=180)
        self.ItemOrder_records.column("ColaDrink", anchor= 'center',width=180)
        self.ItemOrder_records.column("OrangeDrink", anchor= 'center',width=180)
        self.ItemOrder_records.column("MilkyBar", anchor= 'center',width=180)
        self.ItemOrder_records.column("BrownCake", anchor= 'center',width=180)

        self.ItemOrder_records.pack(fill= BOTH, expand=1)
        self.ItemOrder_records.bind("<ButtonRelease-1>")
##====================================================================================================================================================================================

        self.calLabel = Label(TopName, text="",bg= 'cadetblue', font=('arial',12,'bold'))
        self.calLabel.grid(row=0,column=0)
        self.txtDetail = Text(TopName, font=('arial',12,'bold'),width=36,height=20,padx=2,pady=2)
        self.txtDetail.grid(row=1,column=0)
##====================================================================================================================================================================================
        self.btnCost=Button(TopButton, padx=16,bd=5,font=('arial',16,'bold'),width=9,height=2,text='Cost Of Item',command = Receipt).grid(row=0,column=0)
        
        self.btnDiSplay=Button(TopButton, padx=16,bd=5,font=('arial',16,'bold'),width=9,height=2,text='Display', command=addData).grid(row=0,column=1)

        self.btnReset=Button(TopButton, padx=16,bd=5,font=('arial',16,'bold'),width=9,height=2,text='Reset',command=Reset).grid(row=1,column=0)
        
        self.btnExit=Button(TopButton, padx=16,bd=5,font=('arial',16,'bold'),width=9,height=2,text='Exit',command=iExit).grid(row=1,column=1)

        
        
##====================================================================================================================================================================================

##====================================================================================================================================================================================


##====================================================================================================================================================================================

if __name__=='__main__':
    root = Tk()
    application = ItemOrder(root)
    root.mainloop()



 ##====================================================================================================================================================================================