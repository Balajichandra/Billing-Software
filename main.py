from tkinter import * 
from tkinter import ttk
from PIL import  Image,ImageTk
import random
from tkinter import messagebox
import tempfile
import os
class Bill_App:
    def __init__(self,root):
        self.root = root
        #root.geometry('350x200')
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # variables
        self.customer_name = StringVar()
        self.customer_Pnumber = StringVar()
        self.bill_no = StringVar()
        z = random.randint(1000,9999)
        self.bill_no.set(z)
        self.customer_email = StringVar()
        self.search_bill = StringVar()
        self.product = StringVar()
        self.price = IntVar()
        self.qty = IntVar()
        self.sub_total = StringVar()
        self.tax_input = StringVar()
        self.total = StringVar()
         
        ## Product Category Details
        self.Category = ["Select Option","Clothing","LifeStyle","Mobiles"]

        ## sub category
        self.Sub_category_Clothing = ["Pant","T-Shirt","Shirt"]
        
        self.pant = ["Levis","Disel","Pepe Jeans"]
        self.levis_price = 1500
        self.disel_price = 1200
        self.pepe_jeans_price = 1800

        self.TShirt = ["Otto","Polo","Crocodile"]
        self.otto_price = 950
        self.polo_price = 1200
        self.crocodile_price = 1500

        self.Shirt = ["Ramraj","Venfield","Raymonds"]
        self.ramraj_price = 1000
        self.venfield_price = 1200
        self.raymonds_price = 1100

        ## Life style
        self.Sub_category_LifeStyle = ["Face Cream","Perfume","Skin Loation"]
        
        self.face_cream = ["Fair and lovely Mens","Himalyan Mens","Jhonson and Jhonson Mens"]
        self.fair_lovely_price = 150
        self.himalyan_price = 1200
        self.JandJ_price = 180

        self.perfume = ["Fog","Denvier","One8"]
        self.fog_price = 350
        self.denvier_price = 410
        self.One8_price = 280

        self.loations = ["Garnier Men","Loreal","Nivea"]
        self.garnier_price = 150
        self.loarel_price = 175
        self.nivea_price = 200

        ## Mobile
        self.Sub_category_mobile = ["Iphone","OnePlus","Realme"]
        
        self.Iphone = ["Xr","iphone12","iphone13"]
        self.xr_price = 44000
        self.iphone12_price = 69000
        self.iphone13_price = 89000

        self.OnePlus = ["Nord","8","9"]
        self.nord_price = 25000
        self.Oplus8_price = 38000
        self.Oplus9_price = 49000

        self.Realme = ["Narzo","R8","X7"]
        self.Narzo_price = 15000
        self.R8_price = 19900
        self.X7_price = 30000
#############   PART - 1 #########################################################
        ## adding logo
        img = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/Flipkart-Logo.png")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg_logo = ImageTk.PhotoImage(img)

        lb1_img = Label(self.root,image=self.photoimg_logo)
        lb1_img.place(x=0,y=0,width=500,height=130)

        ### adding address
        img = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/address_1.png")
        img = img.resize((250,130),Image.ANTIALIAS)
        self.photoimg_address = ImageTk.PhotoImage(img)

        lb2_img = Label(self.root,image=self.photoimg_address)
        lb2_img.place(x=510,y=0,width=250,height=130)

        ## adding mobile number
        img = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/phone-logo.png")
        img = img.resize((250,130),Image.ANTIALIAS)
        self.photoimg_phone = ImageTk.PhotoImage(img)

        lb3_img = Label(self.root,image=self.photoimg_phone)
        lb3_img.place(x=770,y=0,width=250,height=130)

        ## adding gmail
        img = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/gmail-logo.png")
        img = img.resize((250,130),Image.ANTIALIAS)
        self.photoimg_gmail = ImageTk.PhotoImage(img)

        lb4_img = Label(self.root,image=self.photoimg_gmail)
        lb4_img.place(x=1050,y=0,width=250,height=130)

        ## adding gpay
        img = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/all_pay.jpg")
        img = img.resize((250,130),Image.ANTIALIAS)
        self.photoimg_gpay = ImageTk.PhotoImage(img)

        lb5_img = Label(self.root,image=self.photoimg_gpay)
        lb5_img.place(x=1300,y=0,width=250,height=130)
        ## adding title
        lb_title = Label(self.root,text="Billing Software",font=("times_new_roman",35,"bold"),background="white",foreground="red")
        lb_title.place(x=0,y=130,width=1530,height=45)
#############   PART - 2 #########################################################
        ##billing area
        Main_frame = Frame(self.root,bd=5,relief=GROOVE,background="white")
        Main_frame.place(x=0,y=175,width=1530,height=620)

        ##Customer Label Frame
        Customer_Frame = LabelFrame(Main_frame,text="Customer",font=("times_new_roman",12,"bold"),background="white",foreground="red")
        Customer_Frame.place(x=10,y=5,width=350,height=140)

        self.label_mobile = Label(Customer_Frame,text="Mobile_No",font=("times_new_roman",12,"bold"),background="white")
        self.label_mobile.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mobile = ttk.Entry(Customer_Frame,textvariable=self.customer_Pnumber,font=("times_new_roman",12,"bold"))
        self.entry_mobile.grid(row=0,column=1)

        ## Customer Name
        self.label_name = Label(Customer_Frame,text="Customer Name",font=("arial",12,"bold"),background="white",bd=4)
        self.label_name.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.entry_name = ttk.Entry(Customer_Frame,textvariable=self.customer_name,font=("arial",10,"bold"),width=24)
        self.entry_name.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        ## Customer Email
        self.label_email = Label(Customer_Frame,text="Email",font=("arial",12,"bold"),background="white",bd=4)
        self.label_email.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.entry_email = ttk.Entry(Customer_Frame,textvariable=self.customer_email,font=("arial",10,"bold"),width=24)
        self.entry_email.grid(row=2,column=1,sticky=W,padx=5,pady=2)
#############   PART - 3 #########################################################
        ##Product Label Frame
        Product_Frame = LabelFrame(Main_frame,text="Product",font=("times_new_roman",12,"bold"),background="white",foreground="red")
        Product_Frame.place(x=370,y=5,width=700,height=140)

        ## Category
        self.label_category = Label(Product_Frame,text="Select Category",font=("arial",12,"bold"),background="white",bd=4)
        self.label_category.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.combo_cateogry = ttk.Combobox(Product_Frame,value=self.Category,state="readonly",font=('arial',12,'bold'),width=24)
        self.combo_cateogry.current(0)
        self.combo_cateogry.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        self.combo_cateogry.bind("<<ComboboxSelected>>",self.Categries)
        ## SubCategory
        self.label_sub_category = Label(Product_Frame,text="Subcategory",font=("arial",12,"bold"),background="white",bd=4)
        self.label_sub_category.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.combo_sub_cateogry = ttk.Combobox(Product_Frame,value=[""],state="readonly",font=('arial',12,'bold'),width=24)
        self.combo_sub_cateogry.current(0)
        self.combo_sub_cateogry.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        self.combo_sub_cateogry.bind("<<ComboboxSelected>>",self.Product_select)

        ## Product Name
        self.label_Product_Name = Label(Product_Frame,text="Product Name",font=("arial",12,"bold"),background="white",bd=4)
        self.label_Product_Name.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.combo_Product_Name = ttk.Combobox(Product_Frame,textvariable=self.product,state="readonly",font=('arial',12,'bold'),width=24)
        self.combo_Product_Name.grid(row=2,column=1,sticky=W,padx=5,pady=2)
        self.combo_Product_Name.bind("<<ComboboxSelected>>",self.Price)
        ##Price
        self.label_Price = Label(Product_Frame,text="Price",font=("arial",12,"bold"),background="white",bd=4)
        self.label_Price.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.combo_Price = ttk.Combobox(Product_Frame,state="readonly",textvariable=self.price,font=('arial',12,'bold'),width=24)
        self.combo_Price.grid(row=0,column=3,sticky=W,padx=5,pady=2)
        
        ##Qty
        self.label_Qty = Label(Product_Frame,text="Qty",font=("arial",12,"bold"),background="white",bd=4)
        self.label_Qty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.combo_Qty = ttk.Combobox(Product_Frame,textvariable=self.qty,font=('arial',12,'bold'),width=24)
        self.combo_Qty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

        ##Middle frame
        MiddleFrame = Frame(Main_frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980,height=340)

        ## Image1
        img1 = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/mall.jpg")
        img1 = img1.resize((490,340),Image.ANTIALIAS)
        self.photimg_img1 = ImageTk.PhotoImage(img1)

        lb_img1 = Label(MiddleFrame,image=self.photimg_img1)
        lb_img1.place(x=0,y=0,width=490,height=340)

        ## Image2
        img2 = Image.open("C:/Users/Balaji/Documents/Python/Projects/Billing Software/images/good.jpg")
        img2 = img2.resize((490,340),Image.ANTIALIAS)
        self.photimg_img2 = ImageTk.PhotoImage(img2)

        lb_img2 = Label(MiddleFrame,image=self.photimg_img2)
        lb_img2.place(x=490,y=0,width=500,height=340)


        ##Search
        Search_Frame = Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=1080,y=15,width=450,height=40)

        self.label_bill_no = Label(Search_Frame,text="Bill Number",font=('arial',12,'bold'),foreground="white",background="red")
        self.label_bill_no.grid(row=0,column=0,sticky=W,padx=1)

        self.text_entry_search = ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',12,'bold'),width=18)
        self.text_entry_search.grid(row=0,column=1,sticky=W,padx=2)

        self.label_Button_Search = Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',12,"bold"),background="blue",foreground="white",cursor="hand2",width=15)
        self.label_Button_Search.grid(row=0,column=2)
#############   PART - 4 #########################################################
        ## Bill Display Area
        BillArea = LabelFrame(Main_frame,text="Bill Area",font=("times_new_roman",12,"bold"),background="white",foreground="red")
        BillArea.place(x=1080,y=45,width=400,height=400)

        scroll_y = Scrollbar(BillArea,orient=VERTICAL)
        self.text_area = Text(BillArea,yscrollcommand=scroll_y.set,background="white",foreground="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH,expand=1)

        ## Bill Counter area
        Bottom_Frame = LabelFrame(Main_frame,text="Bill Counter",font=("times_new_roman",12,"bold"),background="white",foreground="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.label_sub_total = Label(Bottom_Frame,text="SubTotal",font=('arial',12,"bold"),background="white",bd=4)
        self.label_sub_total.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entry_label_subtotal = ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=("arial",12,"bold"),width=24)
        self.entry_label_subtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.label_tax = Label(Bottom_Frame,text="Tax",font=('arial',12,'bold'),background="white",bd=4)
        self.label_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entry_label_tax = ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arail',12,'bold'),width=24)
        self.entry_label_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2) 

        self.label_total_amount = Label(Bottom_Frame,text="Total Amount",font=('arial',12,'bold'),background="white",bd=4)
        self.label_total_amount.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entry_label_total_amount = ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',12,'bold'),width=24)
        self.entry_label_total_amount.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        ## Add to kart button
        Button_frame = Frame(Bottom_Frame,bd=2,bg="white")
        Button_frame.place(x=380,y=0)
        self.add_Cart_button = Button(Button_frame,command=self.AddItem,text="Add to Cart",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Cart_button.grid(row=0,column=0)

        self.add_Generate_bill_button = Button(Button_frame,command=self.Generate_Bill,text="Genrate Bill",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Generate_bill_button.grid(row=0,column=1)

        self.add_Save_bill_button = Button(Button_frame,command=self.Save_bill,text="Save Bill",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Save_bill_button.grid(row=0,column=2)

        self.add_Print_button = Button(Button_frame,command=self.PrintBill,text="Print",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Print_button.grid(row=0,column=3)

        self.add_Save_button = Button(Button_frame,text="Save",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Save_button.grid(row=0,column=4)

        self.add_Clear_button = Button(Button_frame,command=self.Clear,text="Clear",font=('arial',15,'bold'),background="blue",foreground="white",width=15)
        self.add_Clear_button.grid(row=0,column=5)

        self.welcome()
        self.l=[]
    def AddItem(self):
           
        Tax = 1
        self.n = self.price.get()
        self.m = self.qty.get() * self.n 
        self.l.append(self.m)  

        if self.product.get() == "":
                messagebox.showerror("Error","Please Select  Product Name")
        else:
                self.text_area.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t{self.m}")
                self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
                self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.price.get()))*Tax)/100)))
                self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.price.get()))*Tax)/100)))))
                

    def Generate_Bill(self):
        if self.product.get() == "":
                messagebox.showerror("Error","Please Add element to kart")
        else:
                #text = self.text_area.get(self.items)
                text = self.text_area.get(8.1,(8.1+float(len(self.l))))
                self.welcome()
                print(text)
                self.text_area.insert(END,text)
                self.text_area.insert(END,"\n ---------------------------------------------------")
                self.text_area.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
                self.text_area.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
                self.text_area.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
                self.text_area.insert(END,"\n ---------------------------------------------------")

    def Save_bill(self):
            op = messagebox.askyesno("Save Bill","Do you want to save bill")
            if op > 0:
                self.bill_data = self.text_area.get(1.0,END)
                f1 = open('bills/'+str(self.bill_no.get())+".txt","w+")
                f1.write(self.bill_data)
                op = messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} saved sucessfully")
                f1.close()

    def PrintBill(self):
            q = self.text_area.get(1.0,END)
            filename = tempfile.mktemp('.txt')
            open(filename,"w").write(q)
            os.startfile(filename,"print")


    def welcome(self):
        self.text_area.delete(1.0,END)
        self.text_area.insert(END,"\t Welcome to Flipkart Billing System")
        self.text_area.insert(END,f"\n Bill Number:{self.bill_no.get()}") 
        self.text_area.insert(END,f"\n Customer Name:{self.customer_name.get()}")
        self.text_area.insert(END,f"\n Customer Phone Number:{self.customer_Pnumber.get()}")
        self.text_area.insert(END,f"\n Customer EMail ID:{self.customer_email.get()}")
        self.text_area.insert(END,"\n-------------------------------------------------------------") 
        self.text_area.insert(END,f"\n Products\t\t\t Qty\tPrice") 
         
    def find_bill(self):
        found = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                    f2 = open(f'bills/{i}','r')
                    self.text_area.delete(1.0,END)
                    for d in f2:
                        res = self.text_area.insert(END,d)
                    f2.close()
                    found="yes"
                     
        if found == "no":    
                messagebox.showerror("Error","No bill found for this number")

    def Clear(self):
        self.text_area.delete(1.0,END)
        self.customer_name.set("")
        self.customer_email.set("")
        self.customer_Pnumber.set("")
        x = random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.product.set("")
        self.price.set(0)
        self.qty.set(0)
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()


    def Categries(self,event=""):
        if self.combo_cateogry.get() == "Clothing":
                self.combo_sub_cateogry.config(value=self.Sub_category_Clothing)
                self.combo_sub_cateogry.current(0)

        if  self.combo_cateogry.get() == "LifeStyle":
                self.combo_sub_cateogry.config(value=self.Sub_category_LifeStyle)
                self.combo_sub_cateogry.current(0)

        if self.combo_cateogry.get() == "Mobiles":
                self.combo_sub_cateogry.config(value=self.Sub_category_mobile) 
                self.combo_sub_cateogry.current(0)               
    def Product_select(self,event=""):
        if self.combo_sub_cateogry.get() == "Pant":
                self.combo_Product_Name.config(value=self.pant)
                self.combo_Product_Name.current(0)

        if self.combo_sub_cateogry.get() == "T-Shirt":
                self.combo_Product_Name.config(value=self.TShirt)
                self.combo_Product_Name.current(0)

        if self.combo_sub_cateogry.get() == "Shirt":
                self.combo_Product_Name.config(value=self.Shirt) 
                self.combo_Product_Name.current(0)       

        if self.combo_sub_cateogry.get() == "Face Cream":
                self.combo_Product_Name.config(value=self.face_cream) 
                self.combo_Product_Name.current(0)                
        
        if self.combo_sub_cateogry.get() == "Perfume":
                self.combo_Product_Name.config(value=self.perfume) 
                self.combo_Product_Name.current(0) 

        if self.combo_sub_cateogry.get() == "Skin Loation":
                self.combo_Product_Name.config(value=self.loations) 
                self.combo_Product_Name.current(0)     
        
        if self.combo_sub_cateogry.get() == "Iphone":
                self.combo_Product_Name.config(value=self.Iphone) 
                self.combo_Product_Name.current(0)      

        if self.combo_sub_cateogry.get() == "OnePlus":
                self.combo_Product_Name.config(value=self.OnePlus) 
                self.combo_Product_Name.current(0) 

        if self.combo_sub_cateogry.get() == "Realme":
                self.combo_Product_Name.config(value=self.Realme) 
                self.combo_Product_Name.current(0)   
    def Price(self,evenet=""):
        if self.combo_Product_Name.get() == "Levis":
                self.combo_Price.config(value=self.levis_price)
                self.combo_Price.current(0)
                self.qty.set(1)   
        
        if self.combo_Product_Name.get() == "Disel":
                self.combo_Price.config(value=self.disel_price)
                self.combo_Price.current(0)
                self.qty.set(1)

        if self.combo_Product_Name.get() == "Pepe Jeans":
                self.combo_Price.config(value=self.pepe_jeans_price)
                self.combo_Price.current(0)
                self.qty.set(1)      

        if self.combo_Product_Name.get() == "Pepe Jeans":
                self.combo_Price.config(value=self.pepe_jeans_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Otto":
                self.combo_Price.config(value=self.otto_price)
                self.combo_Price.current(0)
                self.qty.set(1)

        if self.combo_Product_Name.get() == "Polo":
                self.combo_Price.config(value=self.polo_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Crocodile":
                self.combo_Price.config(value=self.crocodile_price)
                self.combo_Price.current(0)
                self.qty.set(1)                                    

        if self.combo_Product_Name.get() == "Ramraj":
                self.combo_Price.config(value=self.ramraj_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Venfield":
                self.combo_Price.config(value=self.venfield_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Raymonds":
                self.combo_Price.config(value=self.raymonds_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Fair and lovely Mens":
                self.combo_Price.config(value=self.fair_lovely_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Himalyan Mens":
                self.combo_Price.config(value=self.himalyan_price)
                self.combo_Price.current(0)
                self.qty.set(1) 

        if self.combo_Product_Name.get() == "Jhonson and Jhonson Mens":
                self.combo_Price.config(value=self.JandJ_price)
                self.combo_Price.current(0)
                self.qty.set(1)                                               

        if self.combo_Product_Name.get() == "Fog":
                self.combo_Price.config(value=self.fog_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Denvier":
                self.combo_Price.config(value=self.denvier_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "One8":
                self.combo_Price.config(value=self.One8_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Garnier Men":
                self.combo_Price.config(value=self.garnier_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Loreal":
                self.combo_Price.config(value=self.loarel_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Nivea":
                self.combo_Price.config(value=self.nivea_price)
                self.combo_Price.current(0)
                self.qty.set(1)    

        if self.combo_Product_Name.get() == "Xr":
                self.combo_Price.config(value=self.xr_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "iphone12":
                self.combo_Price.config(value=self.iphone12_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "iphone13":
                self.combo_Price.config(value=self.iphone13_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "Nord":
                self.combo_Price.config(value=self.nord_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "8":
                self.combo_Price.config(value=self.Oplus8_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "9":
                self.combo_Price.config(value=self.Oplus9_price)
                self.combo_Price.current(0)
                self.qty.set(1)     

        if self.combo_Product_Name.get() == "Narzo":
                self.combo_Price.config(value=self.Narzo_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "R8":
                self.combo_Price.config(value=self.R8_price)
                self.combo_Price.current(0)
                self.qty.set(1)  

        if self.combo_Product_Name.get() == "X7":
                self.combo_Price.config(value=self.X7_price)
                self.combo_Price.current(0)
                self.qty.set(1)                                                   
if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()        