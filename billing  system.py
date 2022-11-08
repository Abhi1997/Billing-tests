#writing a prgram?
#this might be touugher than i anticipated?
from logging import root
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time
import pyodbc
import pandas as pd

class Customer:


    def __init__(self,root):
        self.root = root
        self.root.title("All Billing System")
        self.root.geometry("1350x750+0+0")
        self.root.config(background = "papayawhip")


        F = Frame(self.root, bg= "papayawhip", bd=20, relief=RIDGE)
        F.grid()
        F1 = Frame(F, bd=14, width=1350, height=100, padx=10, relief=RIDGE, bg= "papayawhip")
        F1.grid(row=0, column=0 ,columnspan=4, sticky=W)
        F2 = Frame(F, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg= "lightsteelblue")
        F2.grid(row=1, column=0, sticky=W)
        F3 = Frame(F, bd=14, width=450, height=488, padx=10, relief=RIDGE, bg= "papayawhip")
        F3.grid(row=1, column=1, sticky=W)
        F4 = Frame(F, bd=14, width=460, height=488, padx=10, relief=RIDGE, bg= "lightsteelblue")
        F4.grid(row=1, column=2 ,columnspan=4, sticky=W)
        F5 = Frame(F4, bd=14, width=370, height=380, padx=10, relief=RIDGE, bg= "lightsteelblue")
        F5.grid(row=0, column=0, sticky=W)
        F6 = Frame(F4, bd=14, width=370, height=120, padx=10, relief=RIDGE, bg= "lightsteelblue")
        F6.grid(row=1, column=0 ,columnspan=4, sticky=W)

        Date1 = StringVar ()
        Time1 = StringVar()
        Date1.set(time.strftime("%d/%m/%y"))
        Time1.set(time.strftime("%I:%M %p"))
        time.sleep(1)

        #=============================================Content====================================================================================================================
        CustomerRef = StringVar()
        Fullname = StringVar()
        Address = StringVar()
        Company = StringVar()
        Pannumber = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Purchasedate = StringVar()
        Paymentdate = StringVar()
        Purchasetype = StringVar()
        Rate = StringVar()
        PaidTax= StringVar()
        Total = StringVar()
        GrandTotal = StringVar()

        CustomerRef.set(random.randint(15440, 9672842531))

        #======================================2nd box defination============================================================================================================
        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16  =IntVar()
        
        E_Item1 = StringVar()
        E_Item2 = StringVar()
        E_Item3 = StringVar()
        E_Item4 = StringVar()
        E_Item5 = StringVar()
        E_Item6 = StringVar()
        E_Item7 = StringVar()
        E_Item8 = StringVar()
        E_Item9 = StringVar()
        
        E_Item1.set("0")
        E_Item2.set("0")
        E_Item3.set("0")
        E_Item4.set("0")
        E_Item5.set("0")
        E_Item6.set("0")
        E_Item7.set("0")
        E_Item8.set("0")
        E_Item9.set("0")
                
        #=================================================Title Declaration=====================================================================================================

        self.lblTitle = Label (F1 , textvariable=Date1, font=('arial',30,'bold'),pady=9,bd=5, bg='lightsteelblue', fg="cornsilk").grid(row=0, column=0)

        self.lblTitle = Label (F1 , text="\t\tAll Billing System\t\t", font=('arial',30,'bold'), pady=9, bd=5 ,bg='lightsteelblue', fg="cornsilk", justify=CENTER).grid(row=0, column=1)

        self.lblTitle = Label (F1 , textvariable=Time1, font=('arial',30,'bold'), pady=9,bd=5, bg='lightsteelblue', fg="cornsilk").grid(row=0, column=2)


        #========================================Exit=============================================================================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Billing System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        #========================================Reset=============================================================================================================================
        def iReset():
            iReset = tkinter.messagebox.askyesno("Billing System","Confirm if you wamt to Reset")
            if iReset > 0:
                self.txtReceipt.delete("1.0",END)
                E_Item1.set("0")
                E_Item2.set("0")
                E_Item3.set("0")
                E_Item4.set("0")
                E_Item5.set("0")
                E_Item6.set("0")
                E_Item7.set("0")
                E_Item8.set("0")
                E_Item9.set("0")

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
                var11.set(0)
                var12.set(0)
                var13.set(0)
                var14.set(0)
                var15.set(0)
                var16.set(0)


                CustomerRef.set("")
                Fullname.set("")
                Address.set("")
                Company.set("")
                Pannumber.set("")
                Mobile.set("")
                Email.set("")
                Purchasedate.set("")
                Paymentdate.set("")
                Purchasetype.set("")
                Rate.set("")
                PaidTax.set("")
                Total.set("")
                GrandTotal.set("")


                self.txtItem1.configure(state=DISABLED)
                self.txtItem2.configure(state=DISABLED)
                self.txtItem3.configure(state=DISABLED)
                self.txtItem4.configure(state=DISABLED)
                self.txtItem5.configure(state=DISABLED)
                self.txtItem6.configure(state=DISABLED)
                self.txtItem7.configure(state=DISABLED)
                self.txtItem8.configure(state=DISABLED)
                self.txtItem9.configure(state=DISABLED)

                return()

        #=====================================================================================================================================================================
        def chkItem1():
            if(var1.get()==1):
                self.txtItem1.configure(state=NORMAL)
                self.txtItem1.delete(0,END)
                self.txtItem1.focus()
                
            elif var1.get()==0:
                self.txtItem1.configure(state=DISABLED)
                E_Item1.set("0")

        def chkItem2():
            if(var2.get()==1):
                self.txtItem2.configure(state=NORMAL)
                self.txtItem2.delete(0,END)
                self.txtItem2.focus()
                
            elif var2.get()==0:
                self.txtItem2.configure(state=DISABLED)
                E_Item2.set("0")

        def chkItem3():
            if(var3.get()==1):
                self.txtItem3.configure(state=NORMAL)
                self.txtItem3.delete(0,END)
                self.txtItem3.focus()
                
            elif var3.get()==0:
                self.txtItem3.configure(state=DISABLED)
                E_Item3.set("0")

        def chkItem4():
            if(var4.get()==1):
                self.txtItem4.configure(state=NORMAL)
                self.txtItem4.delete(0,END)
                self.txtItem4.focus()
                
            elif var4.get()==0:
                self.txtItem4.configure(state=DISABLED)
                E_Item4.set("0")

        def chkItem5():
            if(var5.get()==1):
                self.txtItem5.configure(state=NORMAL)
                self.txtItem5.delete(0,END)
                self.txtItem5.focus()
                
            elif var5.get()==0:
                self.txtItem5.configure(state=DISABLED)
                E_Item5.set("0")

        def chkItem6():
            if(var6.get()==1):
                self.txtItem6.configure(state=NORMAL)
                self.txtItem6.delete(0,END)
                self.txtItem6.focus()
                
            elif var6.get()==0:
                self.txtItem6.configure(state=DISABLED)
                E_Item6.set("0")

        def chkItem7():
            if(var7.get()==1):
                self.txtItem7.configure(state=NORMAL)
                self.txtItem7.delete(0,END)
                self.txtItem7.focus()
                
            elif var7.get()==0:
                self.txtItem7.configure(state=DISABLED)
                E_Item7.set("0")

        def chkItem8():
            if(var8.get()==1):
                self.txtItem8.configure(state=NORMAL)
                self.txtItem8.delete(0,END)
                self.txtItem8.focus()
                
            elif var8.get()==0:
                self.txtItem8.configure(state=DISABLED)
                E_Item8.set("0")

        def chkItem9():
            if(var9.get()==1):
                self.txtItem9.configure(state=NORMAL)
                self.txtItem9.delete(0,END)
                self.txtItem9.focus()
                
            elif var9.get()==0:
                self.txtItem9.configure(state=DISABLED)
                E_Item9.set("0")
        
        #==================================Total=============================================================================================================================
        def costofItem():
            CustomerRef.set(random.randint(15440, 9672842531))
            Item101=float(E_Item1.get())
            Item102=float(E_Item2.get())
            Item103=float(E_Item3.get())
            Item104=float(E_Item4.get())
            Item105=float(E_Item5.get())
            Item106=float(E_Item6.get())
            Item107=float(E_Item7.get())
            Item108=float(E_Item8.get())
            Item109=float(E_Item9.get())

            PriceofItems = (Item101*1.2)+(Item102*1.2)+(Item103*1.2)+(Item104*1.2)+(Item105*1.2)+(Item106*1.2)+(Item107*1.2)+(Item108*1.2)+(Item109*1.2)
            
            TotalofItems = ( str('%.2f'% PriceofItems))
            Total.set(TotalofItems)
            TaxonItems = ( str('%.2f'% ((PriceofItems) * 0.13)))
            
            TotTax = (PriceofItems)*0.13
            PaidTax.set(TaxonItems)
            TotCost = str('%.2f'% (PriceofItems+TotTax))

            GrandTotal.set(TotCost)
            #==================================Receipt show=============================================================================================================================
            self.txtReceipt.insert(END,'Items\t\t\t'+ "Cost of Items\n")
            self.txtReceipt.insert(END,'Customer Ref:  \t\t\t\t'+ CustomerRef.get()+ "\n")
            self.txtReceipt.insert(END,'Item1:  \t\t\t\t\t'+ E_Item1.get()+ "\n")
            self.txtReceipt.insert(END,'Item2:  \t\t\t\t\t'+ E_Item2.get()+ "\n")
            self.txtReceipt.insert(END,'Item3:  \t\t\t\t\t'+ E_Item3.get()+ "\n")
            self.txtReceipt.insert(END,'Item4:  \t\t\t\t\t'+ E_Item4.get()+ "\n")
            self.txtReceipt.insert(END,'Item5:  \t\t\t\t\t'+ E_Item5.get()+ "\n")
            self.txtReceipt.insert(END,'Item6:  \t\t\t\t\t'+ E_Item6.get()+ "\n")
            self.txtReceipt.insert(END,'Item7:  \t\t\t\t\t'+ E_Item7.get()+ "\n")
            self.txtReceipt.insert(END,'Item8:  \t\t\t\t\t'+ E_Item8.get()+ "\n")
            self.txtReceipt.insert(END,'Item9:  \t\t\t\t\t'+ E_Item9.get()+ "\n")


            self.txtReceipt.insert(END, '\nTax Paid:\t\t\t\t'+ PaidTax.get()+"\n")
            self.txtReceipt.insert(END, '\nTotal:\t\t\t\t'+ str(Total.get())+"\n")
            self.txtReceipt.insert(END, '\nGrand Total:\t\t\t\t'+ str(GrandTotal.get()))

            
        
        #======================================Text===============================================================================================================================
        self.txtReceipt = Text(F5, height=19,width=43,bd=10,font=('arial',9 ,'bold'))
        self.txtReceipt . grid(row=0,column=0)

        ##def iclear():
        ##    iclear = tkinter.messagebox.askyesno("Billing System", "Confirm clear the previous receipt?")
        ##    if iclear > 0:
        ##        self.txtReceipt.delete("1.0",END)
        ##        return

        

       
       
        #======================================Entry boxes=========================================================================================================================
        self.lblCus_Ref=Label(F2,font=('arial',12,'bold'), text="Customer Ref:",padx=2, fg="Cornsilk", bg="lightsteelblue")
        self.lblCus_Ref.grid(row=0,column=0, sticky =W)
        self.txtCus_Ref = Entry(F2, font= ('arial',12,'bold'),textvariable= CustomerRef, width=20)
        self.txtCus_Ref.grid(row=0,column=1, pady=3, padx=20)

        self.lblFullname=Label(F2,font=('arial',12,'bold'), text="Full Name:",padx=2, fg="Cornsilk", bg="lightsteelblue")
        self.lblFullname.grid(row=1,column=0, sticky =W)
        self.txtFullname = Entry(F2, font= ('arial',12,'bold'),textvariable=Fullname, width=20)
        self.txtFullname.grid(row=1,column=1, pady=3, padx=20)


        self.lblAddress=Label(F2,font=('arial',12,'bold'), text="Address:",padx=2,pady=2, fg="Cornsilk", bg="lightsteelblue")
        self.lblAddress.grid(row=2,column=0, sticky =W)
        self.txtAddress = Entry(F2, font= ('arial',12,'bold'),textvariable=Address, width=20)
        self.txtAddress.grid(row=2,column=1, pady=3, padx=20)

        self.lblCompany=Label(F2,font=('arial',12,'bold'), text="Company:",padx=2,pady=2, fg="Cornsilk", bg="lightsteelblue")
        self.lblCompany.grid(row=3,column=0, sticky =W)
        self.txtCompany = Entry(F2, font= ('arial',12,'bold'),textvariable=Company, width=20)
        self.txtCompany.grid(row=3,column=1, pady=3, padx=20)

        self.lblPannumber=Label(F2,font=('arial',12,'bold'), text="Pan No.:",padx=2,pady=2, fg="Cornsilk", bg="lightsteelblue",)
        self.lblPannumber.grid(row=4,column=0, sticky =W)
        self.txtPannumber = Entry(F2, font= ('arial',12,'bold'),textvariable=Pannumber, width=20)
        self.txtPannumber.grid(row=4,column=1, pady=3, padx=20)

        self.lblMobile=Label(F2,font=('arial',12,'bold'),text="Mobile No.:",padx=2,pady=2,fg="Cornsilk",bg="lightsteelblue",)
        self.lblMobile.grid(row=5,column=0,sticky=W)
        self.txtMobile=Entry(F2,font=('arial',12,'bold'),textvariable=Mobile,width=20)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail=Label(F2,font=('arial',12,'bold'),text="Email:",padx=2,pady=2,fg='Cornsilk',bg="lightsteelblue",)
        self.lblEmail.grid(row=6,column=0,sticky=W)
        self.txtEmail=Entry(F2,font=('arial',12,'bold'),textvariable=Email,width=20)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblPurchasetype= Label(F2,font=('arial',12,'bold'),text="Purchase Type:",padx=2,pady=2,fg="Cornsilk",bg="lightsteelblue",)
        self.lblPurchasetype.grid(row=7,column=0, sticky=W)
        self.cboPurchasetype=ttk.Combobox(F2,textvariable= Purchasetype, state='readonly', font=('arial', 12,'bold'))

        self.cboPurchasetype['value']=('','Debit','Credit',)
        self.cboPurchasetype.grid(row=7,column=1,pady=3,padx=20)

        self.lblPurchasedate=Label(F2,font=('arial',12,'bold'),text="Purchase Date:",padx=2,pady=2,fg='Cornsilk',bg="lightsteelblue",)
        self.lblPurchasedate.grid(row=8,column=0,sticky=W)
        self.txtPurchasedate=Entry(F2,font=('arial',12,'bold'),textvariable=Date1,width=20)
        self.txtPurchasedate.grid(row=8,column=1,pady=3,padx=20)

        self.lblPaymentdate=Label(F2,font=('arial',12,'bold'),text="Payment Date:",padx=2,pady=2,fg='Cornsilk',bg="lightsteelblue",)
        self.lblPaymentdate.grid(row=9,column=0,sticky=W)
        self.txtPaymentdate=Entry(F2,font=('arial',12,'bold'),textvariable=Paymentdate,width=20)
        self.txtPaymentdate.grid(row=9,column=1,pady=3,padx=20)

        
      
        #=========================================================================================================================================================================
        """Jeans_Joggers.set("0")
        Coats_Jackets.set("0")
        Sportswear.set("0")
        Dresses.set("0")
        Skirts.set("0")
        Swimwear.set("0")
        School_Uniform.set("0")
        Pyjamas_Dressing.set("0")

        Jackets_Blazers.set("0")
        Formal_Trousers.set("0")
        Formal_Shirts.set("0")
        Mens_Boots.set("0")
        Bed_sheets.set("0")
        Pillows_Covers.set("0")
        Patterened_Bedding.set("0")
        Matteress_Protectors.set("0") """

        #=========================================================================================================================================================================

        self.Item1 = Checkbutton(F3, text="Item1",variable=var1, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem1).grid(row=0,sticky=W)
        self.txtItem1 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item1,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem1.grid(row=0,column=1)

        self.Item2 = Checkbutton(F3, text="Item2",variable=var2, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem2).grid(row=1,sticky=W)
        self.txtItem2 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item2,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem2.grid(row=1,column=1)

        self.Item3 = Checkbutton(F3, text="Item3",variable=var3, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem3).grid(row=2,sticky=W)
        self.txtItem3 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item3,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem3.grid(row=2,column=1)

        self.Item4 = Checkbutton(F3, text="Item4",variable=var4, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem4).grid(row=3,sticky=W)
        self.txtItem4 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item4,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem4.grid(row=3,column=1)

        self.Item5 = Checkbutton(F3, text="Item5",variable=var5, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem5).grid(row=4,sticky=W)
        self.txtItem5 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item5,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem5.grid(row=4,column=1)

        self.Item6 = Checkbutton(F3, text="Item6",variable=var6, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem6).grid(row=5,sticky=W)
        self.txtItem6 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item6,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem6.grid(row=5,column=1)

        self.Item7 = Checkbutton(F3, text="Item7",variable=var7, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem7).grid(row=6,sticky=W)
        self.txtItem7 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item7,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem7.grid(row=6,column=1)

        self.Item8 = Checkbutton(F3, text="Item8",variable=var8, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem8).grid(row=7,sticky=W)
        self.txtItem8 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item8,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem8.grid(row=7,column=1)

        self.Item9 = Checkbutton(F3, text="Item9",variable=var9, onvalue=1,offvalue=0, font=('arial',12),bg="papayawhip",command=chkItem9).grid(row=8,sticky=W)
        self.txtItem9 = Entry(F3,font=('arial',12,'bold'),textvariable= E_Item9,bd=8,width=20,justify='left',state = DISABLED)
        self.txtItem9.grid(row=8,column=1)

        self.lblspace= Label(F3, text= "Tax and Total Sum",font=('aarial',18,'bold'), pady=1,bd=9,bg="lightsteelblue",fg="Cornsilk",width=26,justify= CENTER).grid(row=8,column=0, columnspan=4)

        #=========================================================================================================================================================================
        ##self.lblRate = Label(F3,font=('arial',12,'bold'),text="Rate",bd=7,bg="papayawhip",fg="black",)
        ##self.lblRate.grid(row=10,column=0,sticky=W)
        ##self.txtRate = Entry(F3,font=('arial',12,'bold'),textvariable= Rate, bd=7,bg="white",width=20,justify=LEFT)
        ##self.txtRate.grid(row=10,column=1)

        
        self.lblTotal = Label(F3,font=('arial',12,'bold'),text="Total",bd=7,bg="papayawhip",fg="black",)
        self.lblTotal.grid(row=11,column=0,sticky=W)
        self.txtTotal = Entry(F3,font=('arial',12,'bold'),textvariable= Total, bd=7,bg="white",width=20,justify=LEFT)
        self.txtTotal.grid(row=11,column=1)

        self.lblPaidTax = Label(F3,font=('arial',12,'bold'),text="Paid Tax",bd=7,bg="papayawhip",fg="black",)
        self.lblPaidTax.grid(row=12,column=0,sticky=W)
        self.txtPaidTax = Entry(F3,font=('arial',12,'bold'),textvariable= PaidTax, bd=7,bg="white",width=20,justify=LEFT)
        self.txtPaidTax.grid(row=12,column=1)

        self.lblGrandTotal = Label(F3,font=('arial',12,'bold'),text="Total Cost",bd=7,bg="papayawhip",fg="black",)
        self.lblGrandTotal.grid(row=13,column=0,sticky=W)
        self.txtGrandTotal = Entry(F3,font=('arial',12,'bold'),textvariable= GrandTotal, bd=7,bg="white",width=20,justify=LEFT)
        self.txtGrandTotal.grid(row=13,column=1)
        
        #=========================================================================================================================================================================
        #=========================================================================================================================================================================


        self.txtReceipt = Text(F5, height=19, width=43, bd=10, font=('arial',9,'bold'))
        self.txtReceipt .grid(row=0,column=0)
        #=================================Buttons================================================================================================================================
        selfbtnTotal = Button(F6, padx=14, pady=7, bd=5, fg="black", font=('araial',16,'bold'), width=5, height=2, bg="aquamarine", text="Total",command=lambda:[costofItem()]).grid(row=0, column=0) 
        
        selfbtnReset = Button(F6, padx=14, pady=7, bd=5, fg="black", font=('araial',16,'bold'), width=5, height=2, bg="aquamarine", text="Reset",command=iReset).grid(row=0, column=1)

        selfbtnExit = Button(F6, padx=14, pady=7, bd=5, fg="black", font=('araial',16,'bold'), width=5, height=2, bg="aquamarine", text="Exit",command=iExit).grid(row=0, column=2)    
        #=========================================================================================================================================================================
        
 





if __name__=='__main__':
    root = Tk()
    application = Customer(root)
    root.mainloop()
##total button nneds change to add iclear() then clear comment tag from defination . . . 
##-tickrate 128 -novid +fps_max 200 -nojoy +exec useful.cfg -lv  +mat_queue_mode 2 -noaafonts +cl_forcepreload 1 -noipx -nosync +fps_max_menu 200 +rate 786432 +cl_cmdrate 128 +cl_updaterate 128 +cl_interp_ratio 1 +cl_interp 0 -noubershader