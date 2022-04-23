from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview,Scrollbar,Combobox
from PIL import Image,ImageTk

nameList = []
number = 0
money = []
buyed_property_list = []
Ret = FALSE
Mortgage_Properites = {"Mortgage":[],"Property_values":[]}


class Entry_widget:
    
    def __init__(self,screen):
        self.screen = screen
        self.screen.title("Monopoly Banker")
        self.screen.geometry("400x400+75+75")
        img1 = PhotoImage(file="img/ico.png")


        self.no_of_players = IntVar()
        self.name_of_players = StringVar()
        self.screen.iconphoto(FALSE,img1)
        img2 = Image.open("img/logo.png").resize((400,150))
        self.photoImage = ImageTk.PhotoImage(img2)
        label = Label(self.screen,image=self.photoImage,bd=4,relief=RIDGE)
        label.image = self.photoImage
        label.place(x=0,y=0,width=400,height=150)
        
        self.frame = Frame(self.screen,bd=4,relief=RIDGE)
        self.frame.place(x=0,y=150,width=400,height=125)
        
        self.frame2 = Frame(self.screen,bd=4,relief=RIDGE)
        self.frame2.place(x=0,y=275,width=400,height=125)



        label2 = Label(self.frame,text="Enter No of Players",font=("times new roman",14,"bold"),fg="#FF005C")
        label2.grid(row=0,column=0,pady=12,padx=6)
        self.txt_1 = Entry(self.frame,borderwidth=5,font=("times new roman",14,"bold"),textvariable=self.no_of_players)
        self.txt_1.grid(row=1,column=0,pady=12,padx=25)
        btn1 = Button(self.frame,text="Submit",bd=2,relief=RIDGE,fg="black",bg="#00FFF5",font=("times new roman",16,"bold"),command=self.submit)
        btn1.grid(row=1,column=1)
        enterPlayers = Label(self.frame2,text="Enter Players",font=("times new roman",14,"bold"),fg="#FF005C")
        enterPlayers.grid(row=0,column=0,padx=25,pady=12)
        txt_2 = Entry(self.frame2,borderwidth=5,font=("times new roman",14,"bold"),textvariable=self.name_of_players)
        txt_2.grid(row=1,column=0,padx=25,pady=5)
        btn2 = Button(self.frame2,text="Submit",bd=2,relief=RIDGE,fg="black",bg="#00FFF5",font=("times new roman",16,"bold"),command=self.btn2_submit)
        btn2.grid(row=1,column=1)

    def btn2_submit(self):
        if Ret == TRUE:
            global number
            if self.name_of_players.get()!='':
                name = self.name_of_players.get()
                try:
                    int(name)
                    nameList.append(name)
                    self.name_of_players.set("")
                    number+=1
                except ValueError:
                    if len(name)<=12:
                        nameList.append(name.upper())
                        self.name_of_players.set("")
                        number+=1
                    else:
                        messagebox.showwarning("Monopoly Community","Maximum Characters of name are 12")

                if number == self.no_of_players.get():
                    self.screen.destroy()
                    root = Tk()
                    Monopoly_banker(root)
                    root.resizable(FALSE,FALSE)
                    root.mainloop()
        else:
            messagebox.showerror("Monopoly Community","Please Submit Number Of Players")
    
    
    def submit(self):
        try:
            if self.no_of_players.get()>=2 and self.no_of_players.get()<=12:
                self.txt_1.config(state=DISABLED)
            else:
                if self.no_of_players.get()<2:
                    messagebox.showerror("Monopoly Community","Minimum Players Must Be 2")
                if self.no_of_players.get()>12:
                    messagebox.showerror("Monopoly Community","Maximum Players are 12")
            global Ret
            Ret = TRUE
        except TclError as e:
            messagebox.showerror("Monopoly Community",f"{e}")


class Monopoly_banker:
    def __init__(self,root):

# ++++++++++++++++++++++++++++++++Intialization++++++++++++++++++++++++++++++++++++++++++++++++
        self.root = root
        self.root.title("Monopoly Banker")
        self.root.geometry("1000x780+0+0")
# ===========================Adding Icon To the Window============================================
        img1 = PhotoImage(file="img/ico.png")
        self.root.iconphoto(FALSE,img1)

# ==============================Variables Declaration================================================
        self.From = StringVar()
        self.From1 = StringVar()
        self.To = StringVar()
        self.operation = StringVar()
        self.amount_to_tranfered = IntVar()
        self.amount = IntVar()
        self.property = StringVar()
        self.owner = StringVar()
        self.Mortgage__property = StringVar()
        self.Before__Owner = StringVar()
        self.selected_player = StringVar()
        self.owner1 = StringVar()
        self.rent = IntVar()
        self.selling_amount = IntVar()
        self.mortgage = IntVar()
        self.loan = IntVar()

# ===================================Bg Image===========================================================
        img2 = Image.open("img/heading.png").resize((680,780))
        
        self.photoImage = ImageTk.PhotoImage(img2)
        label = Label(image=self.photoImage)
        label.image = self.photoImage
        label.place(x=0,y=0,width=680,height=780)
# ================================Declaring Center Frame==================================================

        frame = Frame(self.root,bd=4,relief=RIDGE)
        frame.place(x=102,y=120,width=480,height=545)

# ==================================Frames Within the Center Frame==========================================

        frame2 = Frame(frame,bd=2,relief=RIDGE)
        frame2.place(x=0,y=0,width=238,height=270)
        
        self.frame3 = Frame(frame,bd=2,relief=RIDGE)
        self.frame3.place(x=238,y=0,width=234,height=270)
        
        self.frame4 = Frame(frame,bd=2,relief=RIDGE)
        self.frame4.place(x=0,y=270,width=472,height=268)

# ===================================Players Frame =============================================================
        
        self.frame5 = Frame(self.root,bd=2,relief=RIDGE)
        self.frame5.place(x=680,y=0,width=318,height=460)

        self.frame6 =Frame(self.root,bd=2,relief=RIDGE)
        self.frame6.place(x=680,y=460,width=318,height=318)

        self.frame7 = Frame(self.frame6)
        self.frame7.place(x=0,y=0,width=313,height=195)

# ========================================Center Tree View ============================================================
       


        label2 = Label(frame2,text="Transfer",bg="black",font=("times new roman",20,"bold"),fg="gold")
        label2.place(x=0,y=0,width=238,height=50)

        label3 = Label(self.frame3,text="Operations",bg="black",font=("times new roman",20,"bold"),fg="gold")
        label3.place(x=0,y=0,width=234,height=50)
        
        label4 = Label(frame2,text="From",font=("times new roman",14,"bold"))
        label4.place(x=0,y=79)
        
        self.txt_3 = Combobox(frame2,font=("times new roman",14,"bold"),textvariable=self.From)
        self.txt_3["values"] = tuple(nameList)
        self.txt_3["state"] = "readonly"
        self.txt_3.place(x=60,y=79,width=169)
        
        label5 = Label(frame2,text="Rs.",font=("times new roman",14,"bold"))
        label5.place(x=0,y=120)
       
        txt_4 = Entry(frame2,font=("times new roman",14,"bold"),textvariable=self.amount_to_tranfered)
        txt_4.place(x=60,y=120,width=169)

        label6 = Label(frame2,text="To",font=("times new roman",14,"bold"))
        label6.place(x=0,y=160)

        
        
        self.txt_5 = Combobox(frame2,font=("times new roman",14,"bold"),textvariable=self.To)
        self.txt_5["values"] = tuple(nameList)
        self.txt_5["state"] = "readonly"
        self.txt_5.place(x=60,y=160,width=169)

        btn1 = Button(frame2,text="Transfer",width=13,bd=2,relief=RIDGE,fg="black",bg="#00FFF5",font=("times new roman",16,"bold"),command=self.ammount_transfer)
        btn1.place(x=40,y=200)
    
        label7 = Label(self.frame3,text="Operation",font=("times new roman",14,"bold"))
        label7.place(x=0,y=79)
        
        self.txt_6 = Combobox(self.frame3,font=("times new roman",14,"bold"),textvariable=self.operation)
        self.txt_6["values"] = ("Add","Subtract")
        self.txt_6["state"] = "readonly"
        self.txt_6.place(x=100,y=79,width=129)

        label8 = Label(self.frame3,text="Player",font=("times new roman",14,"bold"))
        label8.place(x=0,y=110)
        
        self.txt_7 = Combobox(self.frame3,font=("times new roman",14,"bold"),textvariable=self.From1)
        self.txt_7["values"] = tuple(nameList)
        self.txt_7["state"] = "readonly"
        self.txt_7.place(x=60,y=110,width=169)
        
        label9 = Label(self.frame3,text="Rs.",font=("times new roman",14,"bold"))
        label9.place(x=0,y=150)
       
        txt_8 = Entry(self.frame3,font=("times new roman",14,"bold"),textvariable=self.amount)
        txt_8.place(x=60,y=150,width=169)

        btn2 = Button(self.frame3,text="Submit",width=13,bd=2,relief=RIDGE,fg="black",bg="#00FFF5",font=("times new roman",16,"bold"),command=self.Operation)
        btn2.place(x=40,y=200)


        btn6 = Button(self.frame6,text="Selected Player Properties",bd=2,relief=RIDGE,bg="#00FF89",font=("times new roman",14,"bold"),command=self.show_player_property)
        btn6.place(x=30,y=200,width=250)

        btn7 = Button(self.frame6,text="Mortgage Properties",bd=2,relief=RIDGE,bg="#00FF89",font=("times new roman",14,"bold"),command=self.show_mortgage_data)
        btn7.place(x=30,y=240,width=250,height=35)
        
        btn8 = Button(self.frame6,text="Sell Property",bd=2,relief=RIDGE,bg="#00FF89",font=("times new roman",14,"bold"),command=self.show__sell_form)
        btn8.place(x=30,y=277,width=120,height=35)
        
        btn9 = Button(self.frame6,text="clear",bd=2,relief=RIDGE,bg="#00FF89",font=("times new roman",14,"bold"),command=self.clear)
        btn9.place(x=153,y=277,width=127,height=35)



        
        
        self.initialize_money()
        self.players()
        self.show_buy_mortgage_form()
    def initialize_money(self):
        for i in range(0,len(nameList)):
            money.append(10000)
        for i in range(0,len(nameList)):
            k = {}
            k[nameList[i]] = []
            buyed_property_list.append(k)
    def players(self):
        label_4 = Label(self.frame5,text=f"Players",font=("times new roman",16,"bold"))
        label_4.grid(row=0,column=0,padx=15,pady=15)
        label_5 = Label(self.frame5,text=f"Money",font=("times new roman",16,"bold"))
        label_5.grid(row=0,column=1,padx=15,pady=15)
        for i in range(0,len(nameList)):
            label_i = Label(self.frame5,text=f"{nameList[i]}",font=("times new roman",16,"bold"))
            label_i.grid(row=i+1,column=0,padx=4)
            label2_i = Label(self.frame5,text=f"{money[i]}",font=("times new roman",16,"bold"))
            label2_i.grid(row=i+1,column=1)
    def destroy_frame(self):
        for widgets in self.frame5.winfo_children():
            widgets.destroy()
    def destroy_frame7(self):
        for widgets in self.frame7.winfo_children():
            widgets.destroy()
    def destroy_frame4(self):
        for widgets in self.frame4.winfo_children():
            widgets.destroy()

    def clear_tree_view(self):
        for record in self.treeview.get_children():
            self.treeview.delete(record)
# ======================= Operations =============
    def ammount_transfer(self):
        try:
            if self.From.get() == "" or self.To.get() == "" or self.amount_to_tranfered == 0:
                messagebox.showerror("Monopoly Community","All Fields are Required")
            elif self.From.get() == self.To.get():
                messagebox.showerror("Monopoly Communinty","Please Select Different Players")
            else:
                for i in range(0,len(nameList)):
                    if nameList[i] == self.From.get():
                        k = int(money[i])
                        k-=self.amount_to_tranfered.get()
                        money[i] = k
                for i in range(0,len(nameList)):
                    if nameList[i] == self.To.get():
                        k = int(money[i])
                        k+=self.amount_to_tranfered.get()
                        money[i] = k
                self.destroy_frame()
                self.players()
                self.clear()
        except TclError as e:
            messagebox.showerror("Monopoly Community","Enter Amonunt Perfectly")
    def Operation(self):
        try:
            if self.From1.get() == "" or self.amount.get() == 0 or self.operation.get() =="":
                messagebox.showerror("Monopoly Community","All Fields are Required")
            else:
 
                if self.operation.get() == "Add":
                    for i in range(0,len(nameList)):
                        if nameList[i] == self.From1.get():
                            k = int(money[i])
                            k+=self.amount.get()
                            money[i] = k
                if self.operation.get() == "Subtract":
                    for i in range(0,len(nameList)):
                        if nameList[i] == self.From1.get():
                            k = int(money[i])
                            k-=self.amount.get()
                            money[i] = k
                self.destroy_frame()
                self.players()
                self.clear()
        except TclError as e:
            messagebox.showerror("Monopoly Community","Recheck Your Submission Once Ammount Entered Wronly")
    def search_property(self):
        value = FALSE
        for i in range(len(nameList)):
            if(len(buyed_property_list[i][nameList[i]])>0):
                for row in range(len(buyed_property_list[i][nameList[i]])):
                    y = buyed_property_list[i][nameList[i]][row][0]
                    if y == self.property.get():
                        value = TRUE   
        return value
    def buy_property(self):
        try:
            if self.search_property() == TRUE:
                messagebox.showerror("Monopoly Community","Property already Exists")
            elif self.property.get() =="":
                messagebox.showerror("Monopoly Community","All Fields are required")

            elif self.rent.get() == 0: 
                messagebox.showerror("Monopoly Community","All Fields are required")

            elif self.owner.get() =="":  
                messagebox.showerror("Monopoly Community","All Fields are required")

            elif self.mortgage.get() == 0:
                messagebox.showerror("Monopoly Community","All Fields are required")
            else:
                lis = []
                prop = self.property.get()
                try:
                    prop = int(prop)
                    messagebox.showerror("Monopoly Community","Property Must Be In Characters")
                except Exception as e:
    
                    lis.append(prop.upper())
                    lis.append(self.owner.get())
                    lis.append(self.rent.get())
                    lis.append(self.mortgage.get())
                    y = tuple(lis)
                    for row in range(0,len(nameList)):
                        if nameList[row] == self.owner.get():
                            buyed_property_list[row][self.owner.get()].append(y)
                    self.clear_tree_view()
                    self.add_properties_to_treeview()
                    self.clear()
        except TclError as e:
            messagebox.showerror("Monopoly Community",f"{e}")
    def delete_property(self):
        value = FALSE
        try:
            if self.property.get() =="":
                messagebox.showerror("Monopoly Community","All Fields are required")
                return value

            elif self.rent.get() == 0: 
                messagebox.showerror("Monopoly Community","All Fields are required")
                return value

            elif self.owner.get() =="":  
                messagebox.showerror("Monopoly Community","All Fields are required")
                return value
            elif self.mortgage.get() == 0:
                messagebox.showerror("Monopoly Community","All Fields are required")
                return value
            else:
                property_name = self.property.get()
                owner_name = self.owner.get()
                for i in range(len(nameList)):
                    if nameList[i] == owner_name:
                        if len(buyed_property_list[i][owner_name])>0:
                            for row in range(0,len(buyed_property_list[i][owner_name])):
                                if buyed_property_list[i][owner_name][row][0] == self.property.get():
                                    del buyed_property_list[i][owner_name][row]
                                    break
                self.clear_tree_view()
                self.add_properties_to_treeview()
                return TRUE
            


        except TclError:
            messagebox.showerror("Monopoly Community","Enter Rent or Mortgage in Integer Values")
            return value

    def delete_row_in_treeview(self):
        try:
            if self.property.get() =="":
                messagebox.showerror("Monopoly Community","All Fields are required")

            elif self.rent.get() == 0: 
                messagebox.showerror("Monopoly Community","All Fields are required")

            elif self.owner.get() =="":  
                messagebox.showerror("Monopoly Community","All Fields are required")
            elif self.mortgage.get() == 0:
                messagebox.showerror("Monopoly Community","All Fields are required")
            else:
                property_name = self.property.get()
                owner_name = self.owner.get()
                for i in range(len(nameList)):
                    if nameList[i] == owner_name:
                        for row in range(len(buyed_property_list[i][owner_name])):
                            if buyed_property_list[i][owner_name][row][0] == self.property.get():
                                del buyed_property_list[i][owner_name][row]
                                break    
                self.clear_tree_view()
                self.add_properties_to_treeview()
                self.clear()
        except TclError:
            messagebox.showerror("Monopoly Community","Enter Rent or Mortgage in Integer Values")


    def mortgage_property(self):
        if self.delete_property() == TRUE:
            amount = self.mortgage.get()
            amount = amount + amount*(0.1)
            lis = []
            lis.append(self.property.get())
            lis.append(self.owner.get())
            lis.append(int(amount))
            Mortgage_Properites["Mortgage"].append(tuple(lis))
            Mortgage_Properites["Property_values"].append((self.rent.get(),self.mortgage.get()))
            self.clear()
        else:
            messagebox.showerror("Monopoly Community","Property Does Not Exists")

    def pay_loan_amount(self):
        self.operation.set("Subtract")
        self.From1.set(self.Before__Owner.get())
        self.amount.set(int(self.loan.get()))
        self.Operation()

    def get_back_property_from_mortgage(self):
        for row in range(len(Mortgage_Properites["Mortgage"])):
            if Mortgage_Properites["Mortgage"][row][0] == self.Mortgage__property.get():
                self.rent.set(Mortgage_Properites["Property_values"][row][0])
                self.mortgage.set(Mortgage_Properites["Property_values"][row][1])

        self.property.set(self.Mortgage__property.get())
        self.owner.set(self.Before__Owner.get())
        lis = []
        lis.append(self.property.get())
        lis.append(self.owner.get())
        lis.append(self.rent.get())
        lis.append(self.mortgage.get())
        for i in range(len(nameList)):
            if nameList[i] == self.owner.get():
                buyed_property_list[i][self.owner.get()].append(tuple(lis))
        self.delete_mortgage_data()
        self.pay_loan_amount()
        self.add_mortgage_properties_list_to_mortgage_treeview()
        self.clear()
    def delete_mortgage_data(self):
        value = 0
        if self.Before__Owner.get() == "" or self.Mortgage__property.get()== "":
            return
        else:
            if len(Mortgage_Properites["Mortgage"])>0:
                for row in range(len(Mortgage_Properites["Mortgage"])):
                    if Mortgage_Properites["Mortgage"][row][0] == self.Mortgage__property.get() and Mortgage_Properites["Mortgage"][row][1] == self.Before__Owner.get():
                        value = row
                del Mortgage_Properites["Mortgage"][value]
                del Mortgage_Properites["Property_values"][value]
                self.add_mortgage_properties_list_to_mortgage_treeview()
            else:
                messagebox.showerror("Monopoly Community","Please Enter Details First")
    
    def delete_mortgage_data_Function(self):
        value = 0
        if self.Before__Owner.get() == "" or self.Mortgage__property.get()== "":
            return
        else:
            if len(Mortgage_Properites["Mortgage"])>0:
                for row in range(len(Mortgage_Properites["Mortgage"])):
                    if Mortgage_Properites["Mortgage"][row][0] == self.Mortgage__property.get() and Mortgage_Properites["Mortgage"][row][1] == self.Before__Owner.get():
                        value = row
                del Mortgage_Properites["Mortgage"][value]
                del Mortgage_Properites["Property_values"][value]
                self.add_mortgage_properties_list_to_mortgage_treeview()
                self.clear()
            else:
                messagebox.showerror("Monopoly Community","Please Enter Details First")
    def sell_property(self):
        from_name = self.owner.get()
        to_name = self.To.get()
        amount = self.amount_to_tranfered.get()
        property_name = self.property.get()
        if from_name == "" or to_name == "" or amount == 0 or property_name == "":
            messagebox.showerror("Monopoly Community","All Fields Are Required")
        else:
            for i in range(len(nameList)):
                if nameList[i] == from_name:
                    for row in range(len(buyed_property_list[i][from_name])):
                        if buyed_property_list[i][from_name][row][0] == property_name:
                            rent = buyed_property_list[i][from_name][row][2]
                            mortgage = buyed_property_list[i][from_name][row][3]
                            del buyed_property_list[i][from_name][row]
            if to_name == "Bank":
                self.operation.set("Add")
                self.From1.set(from_name)
                self.amount.set(amount)
                self.Operation()
                self.clear_tree_view()
                self.add_properties_to_treeview()
            else:
                self.From.set(to_name)
                self.To.set(from_name)
                self.amount_to_tranfered.set(amount)
                self.ammount_transfer()
                self.property.set(property_name)
                self.owner.set(to_name)
                self.rent.set(rent)
                self.mortgage.set(mortgage)
                self.buy_property()
    def sell_in_auction(self):
        rent = ""
        mortgage =""
        from_name = self.Before__Owner.get()
        to_name = self.To.get()
        amount = self.amount.get()
        property_name = self.Mortgage__property.get()
        for row in range(len(Mortgage_Properites["Mortgage"])):
            if Mortgage_Properites["Mortgage"][row][0] == self.Mortgage__property.get():
                rent = Mortgage_Properites["Property_values"][row][0]
                mortgage = Mortgage_Properites["Property_values"][row][1]                
        if rent == "" or mortgage == "":
            messagebox.showerror("Monopoly Community","No Such Property Exists")
        else:
                self.delete_mortgage_data()
                self.operation.set("Subtract")
                self.From1.set(to_name)
                self.amount.set(amount)
                self.Operation()
                self.show_buy_mortgage_form()
                self.property.set(property_name)
                self.owner.set(to_name)
                self.rent.set(rent)
                self.mortgage.set(mortgage)
                self.buy_property()
    def set_rent(self):
        self.amount_to_tranfered.set(self.rent.get())
        self.To.set(self.owner.get())
    def fetch_data(self,event=""):
        cursur_row = self.treeview.focus()
        if cursur_row:
            content = self.treeview.item(cursur_row)
            row = content["values"]
            self.owner.set(row[1])
            self.property.set(row[0])
            self.rent.set(int(row[2]))
            self.mortgage.set(int(row[3]))
            self.selected_player.set(row[1])
            self.show_buy_mortgage_form_with_selected_player_properties()

    def fetch_mortgage_data(self,event=""):
        cursur_row = self.mortgage_treeview.focus()
        if cursur_row:
            content = self.mortgage_treeview.item(cursur_row)
            row = content["values"]
            self.Mortgage__property.set(row[0])
            self.Before__Owner.set(row[1])
            self.loan.set(int(row[2]))
# ======================== Tree View Adding Property =============================================================

    def add_properties_to_treeview(self):
        for i in range(0,len(nameList)):
            if len(buyed_property_list[i][nameList[i]])>0:
                for row in buyed_property_list[i][nameList[i]]:
                    self.treeview.insert("",END,values=row)

    def show_selected_player_properties_in_treeview(self):
        name = self.selected_player.get()
        for i in range(len(nameList)):
            if nameList[i] == name:
                self.clear_tree_view()
                for row in buyed_property_list[i][name]:
                    self.treeview.insert("",END,value=row)
                

    def add_mortgage_properties_list_to_mortgage_treeview(self):
        for record in self.mortgage_treeview.get_children():
            self.mortgage_treeview.delete(record)
        if len(Mortgage_Properites["Mortgage"])>0:
            for row in Mortgage_Properites["Mortgage"]:
                self.mortgage_treeview.insert("",END,value=row)        
# ++=====================================Widget Functions===============================

    def show_buy_mortgage_form_with_selected_player_properties(self):
        self.destroy_frame7()
        self.property_treeview()
        self.show_selected_player_properties_in_treeview()
        label10 = Label(self.frame7,text="Property",font=("times new roman",14,"bold"))
        label10.grid(row=0,column=0)

        txt_9 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.property)
        txt_9.config(state=DISABLED)
        txt_9.grid(row=0,column=1)
        
        label11 = Label(self.frame7,text="Owner",font=("times new roman",14,"bold"))
        label11.grid(row=1,column=0)

        self.txt_10 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.owner)
        self.txt_10.config(state=DISABLED)
        self.txt_10.grid(row=1,column=1,pady=10)

        label12= Label(self.frame7,text="Rent",font=("times new roman",14,"bold"))
        label12.grid(row=2,column=0)

        txt_11 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.rent)
        txt_11.config(state=DISABLED)
        txt_11.grid(row=2,column=1)

        label13 = Label(self.frame7,text="Mortgage",font=("times new roman",14,"bold"))
        label13.grid(row=3,column=0)

        txt_12 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.mortgage)
        txt_12.config(state=DISABLED)
        txt_12.grid(row=3,column=1,pady=10)

        btn3 = Button(self.frame7,text="Mortgage",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.mortgage_property)
        btn3.place(x=5,y=148,width=100)
        
        btn4 = Button(self.frame7,text="Rent",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.set_rent)
        btn4.place(x=110,y=148,width=100)
        
        btn5 = Button(self.frame7,text="Back",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form)
        btn5.place(x=215,y=148,width=90)
    

    def show_buy_mortgage_form(self):
        self.destroy_frame7()
        self.property_treeview()
        self.add_properties_to_treeview()
        self.clear()
        label10 = Label(self.frame7,text="Property",font=("times new roman",14,"bold"))
        label10.grid(row=0,column=0)

        txt_9 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.property)
        txt_9.grid(row=0,column=1)
        
        label11 = Label(self.frame7,text="Owner",font=("times new roman",14,"bold"))
        label11.grid(row=1,column=0)

        self.txt_10 = Combobox(self.frame7,font=("times new roman",13,"bold"),textvariable=self.owner)
        self.txt_10["values"] = tuple(nameList)
        self.txt_10["state"] = "readonly"
        self.txt_10.grid(row=1,column=1,pady=10)

        label12= Label(self.frame7,text="Rent",font=("times new roman",14,"bold"))
        label12.grid(row=2,column=0)

        txt_11 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.rent)
        txt_11.grid(row=2,column=1)

        label13 = Label(self.frame7,text="Mortguage",font=("times new roman",14,"bold"))
        label13.grid(row=3,column=0)

        txt_12 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.mortgage)
        txt_12.grid(row=3,column=1,pady=10)

        btn3 = Button(self.frame7,text="Add Property",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",16,"bold"),command=self.buy_property)
        btn3.place(x=5,y=148,width=300)
        
    
    def show__sell_form(self):
        self.destroy_frame7()
        self.property_treeview()
        self.add_properties_to_treeview()
        label10 = Label(self.frame7,text="Property",font=("times new roman",14,"bold"))
        label10.grid(row=0,column=0)

        txt_9 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.property)
        txt_9.config(state=DISABLED)
        txt_9.grid(row=0,column=1)
        
        label11 = Label(self.frame7,text="To",font=("times new roman",14,"bold"))
        label11.grid(row=1,column=0)

        self.txt_10 = Combobox(self.frame7,font=("times new roman",13,"bold"),textvariable=self.To)
        lis = []
        lis.append("Bank")
        lis = set(lis)
        lis = list(lis)
        lis = lis + nameList
        self.txt_10["values"] = tuple(lis)
        self.txt_10["state"] = "readonly"
        self.txt_10.grid(row=1,column=1,pady=10)
                
        label11 = Label(self.frame7,text="From",font=("times new roman",14,"bold"))
        label11.grid(row=2,column=0)

        self.txt_11 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.owner)
        self.txt_11.config(state=DISABLED)
        self.txt_11.grid(row=2,column=1,pady=10)

        label12= Label(self.frame7,text="Amount",font=("times new roman",14,"bold"))
        label12.grid(row=3,column=0)

        txt_11 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.amount_to_tranfered)
        txt_11.grid(row=3,column=1)


        btn3 = Button(self.frame7,text="Sell",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.sell_property)
        btn3.place(x=5,y=148,width=150)
        
        btn4 = Button(self.frame7,text="Back",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form)
        btn4.place(x=160,y=148,width=150)
    
    def show_player_property(self):
        self.destroy_frame7()
        self.clear()
        label_10 = Label(self.frame7,text="Select Player",bg="black",fg="gold",font=("times new roman",18,"bold"))
        label_10.place(x=0,y=0,width=310,height=60)

        self.txt_10 = Combobox(self.frame7,font=("times new roman",18,"bold"),textvariable=self.selected_player)
        self.txt_10["values"] = tuple(nameList)
        self.txt_10["state"] = "readonly"
        self.txt_10.place(x=20,y=80,width=280,height=30)

                
        btn3 = Button(self.frame7,text="Details",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form_with_selected_player_properties)
        btn3.place(x=5,y=148,width=150)
        
        btn4 = Button(self.frame7,text="Back",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form)
        btn4.place(x=160,y=148,width=150)
                
            

    def property_treeview(self):
        self.destroy_frame4()

        self.treeview = Treeview(self.frame4)
        self.treeview.place(x=0,y=0,width=452,height=220)

        self.yscroll = Scrollbar(self.frame4,orient=VERTICAL,command=self.treeview.yview)
        self.yscroll.pack(side=RIGHT,fill=Y)

        self.treeview.config(yscrollcommand=self.yscroll.set)
        self.treeview["columns"] = ("Property","Owner","Rent","Mortgage")

        self.treeview.column("Property", width = 60)
        self.treeview.column("Owner", width = 60)
        self.treeview.column("Rent", width = 60)
        self.treeview.column("Mortgage", width = 60)

        self.treeview.heading("Property", text ="Property")
        self.treeview.heading("Owner", text ="Owner")
        self.treeview.heading("Rent", text ="Rent")
        self.treeview.heading("Mortgage", text ="Mortgage")

        self.treeview['show'] = 'headings'
        self.treeview.bind("<ButtonRelease-1>",self.fetch_data)

        button1 = Button(self.frame4,bd=2,relief=RIDGE,text="Delete Row",font=("times new roman",14,"bold"),bg="#FE0017",fg="white",command=self.delete_row_in_treeview)
        button1.place(x=154,y=225,width=150,height=35)
    
    def show_mortgage_data(self):
        self.mortgage__treeview()
        self.show_mortguage_form()
        self.add_mortgage_properties_list_to_mortgage_treeview()
        self.clear()



    def mortgage__treeview(self):
        self.destroy_frame4()
        self.mortgage_treeview = Treeview(self.frame4)
        self.mortgage_treeview.place(x=0,y=0,width=452,height=220)

        self.yscroll = Scrollbar(self.frame4,orient=VERTICAL,command=self.mortgage_treeview.yview)
        self.yscroll.pack(side=RIGHT,fill=Y)

        self.mortgage_treeview.config(yscrollcommand=self.yscroll.set)
        self.mortgage_treeview["columns"] = ("Property","Owner","amount")

        self.mortgage_treeview.column("Property", width = 60)
        self.mortgage_treeview.column("Owner", width = 60)
        self.mortgage_treeview.column("amount", width = 60)

        self.mortgage_treeview.heading("Property", text ="Property")
        self.mortgage_treeview.heading("Owner", text ="Owner")
        self.mortgage_treeview.heading("amount", text ="Loan Amount")

        self.mortgage_treeview['show'] = 'headings'

        self.mortgage_treeview.bind("<ButtonRelease-1>",self.fetch_mortgage_data)

        button1 = Button(self.frame4,bd=2,relief=RIDGE,text="Delete Row",font=("times new roman",14,"bold"),bg="#FE0017",fg="white",command=self.delete_mortgage_data_Function)
        button1.place(x=154,y=225,width=150,height=35)
    
    def show_auction_form(self):
        self.destroy_frame7()
        label10 = Label(self.frame7,text="Property",font=("times new roman",14,"bold"))
        label10.grid(row=0,column=0)

        txt_9 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.Mortgage__property)
        txt_9.config(state=DISABLED)
        txt_9.grid(row=0,column=1)
        
        label11 = Label(self.frame7,text="To",font=("times new roman",14,"bold"))
        label11.grid(row=1,column=0)

        self.txt_10 = Combobox(self.frame7,font=("times new roman",13,"bold"),textvariable=self.To)
        self.txt_10["values"] = tuple(nameList)
        self.txt_10["state"] = "readonly"
        self.txt_10.grid(row=1,column=1,pady=10)

        label11 = Label(self.frame7,text="From",font=("times new roman",14,"bold"))
        label11.grid(row=2,column=0)

        self.txt_11 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.Before__Owner)
        self.txt_11.config(state=DISABLED)
        self.txt_11.grid(row=2,column=1,pady=5)


        
        label13 = Label(self.frame7,text="Amount",font=("times new roman",14,"bold"))
        label13.grid(row=3,column=0)


        txt_12 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.amount)
        txt_12.grid(row=3,column=1)

        
        btn3 = Button(self.frame7,text="Pay",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.sell_in_auction)
        btn3.place(x=5,y=150,width=150)
        
        btn5 = Button(self.frame7,text="Back",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form)
        btn5.place(x=160,y=150,width=150)

    
    def show_mortguage_form(self):
        self.destroy_frame7()
        label10 = Label(self.frame7,text="Property",font=("times new roman",14,"bold"))
        label10.grid(row=0,column=0)

        txt_9 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.Mortgage__property)
        txt_9.config(state=DISABLED)
        txt_9.grid(row=0,column=1)
        
        label11 = Label(self.frame7,text="Owner",font=("times new roman",14,"bold"))
        label11.grid(row=1,column=0)

        self.txt_10 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.Before__Owner)
        self.txt_10.config(state=DISABLED)
        self.txt_10.grid(row=1,column=1,pady=10)

        
        label13 = Label(self.frame7,text="Loan",font=("times new roman",14,"bold"))
        label13.grid(row=2,column=0)

        txt_12 = Entry(self.frame7,font=("times new roman",14,"bold"),textvariable=self.loan)
        txt_12.config(state=DISABLED)
        txt_12.grid(row=2,column=1)

        
        btn3 = Button(self.frame7,text="Pay",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.get_back_property_from_mortgage)
        btn3.place(x=5,y=148,width=100)
        
        btn4 = Button(self.frame7,text="Auction",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_auction_form)
        btn4.place(x=110,y=148,width=100)
        
        btn5 = Button(self.frame7,text="Back",bd=2,relief=RIDGE,bg="#FF00F3",font=("times new roman",14,"bold"),command=self.show_buy_mortgage_form)
        btn5.place(x=215,y=148,width=90)


# ++=========================== Other Operations ===============================
    def clear(self):
        self.From.set("")
        self.From1.set("")
        self.To.set("")
        self.operation.set("")
        self.amount_to_tranfered.set(0)
        self.amount.set(0)
        self.property.set("")
        self.owner.set("")
        self.owner1.set("")
        self.rent.set(0)
        self.selling_amount.set(0)
        self.mortgage.set(0)
        self.loan.set(0)
        self.selected_player.set("")
        self.Before__Owner.set("")
        self.Mortgage__property.set("")

        