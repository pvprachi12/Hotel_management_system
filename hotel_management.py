#hotel Management system 
class hotelmanage:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1000,name='',address='',cindate='',coutdate='',rno=1):

        print ("\n\n*****WELCOME TO HOTEL ELITE*****\n")

        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
#Customer details
    def inputdata(self):
        self.name=input("\nEnter your Fullname:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        print("Your room no.:",self.rno,"\n")

#For Room details
        
    def roomrent(self):#sel1353

        print ("We have the following rooms for you:-")

        print ("1.  Class A----&gt;4000")

        print ("2.  Class B----&gt;3000")

        print ("3.  Class C----&gt;2000")

        print ("4.  Class D----&gt;1000")

        x=int(input("Enter the number of your choice Please-&gt;"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have choose room Class A")

            self.s=4000*n

        elif (x==2):

            print ("you have choose room Class B")

            self.s=3000*n

        elif (x==3):

            print ("you have choose room Class C")

            self.s=2000*n

        elif (x==4):
            print ("you have choose room Class D")

            self.s=1000*n

        else:

            print ("please choose a room")

        print ("your choosen room rent is =",self.s,"\n")
#for food purchased 

    def foodpurchased(self):

        print("*****RESTAURANT MENU*****")

        print("1.Dessert-----&gt;100","2.Drinks-----&gt;50","3.Breakfast---&gt;90","4.Lunch----&gt;110","5.Dinner---&gt;150","6.Exit")


        while (1):

            c=int(input("Enter the number of your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+100*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+50*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.r=self.r+150*d

            elif (c==6):
                break;
            else:
                print("You've Enter an Invalid Key")

        print ("Total food Cost=Rs",self.r,"\n")

#For games available in hotel

    def gamebill(self):
        print("*******GAME MENU*******")
        print("1.Table tennis---->Rs60","2.Bowling---->Rs80","3.Snooker---->Rs70","4.Video Games---->Rs90","5.Pool---->Rs50","6.Exit")
        while(1):
            g=int(input("Enter your choice:"))
        
            if (g==1):
               h=int(input("No.of hours:"))
               self.g=self.p+60*h
            elif (g==2):
                 h=int(input("No.of hours:"))
                 self.g=self.p+80*h
            elif (g==3):
                 h=int(input("No.of hours:"))
                 self.g=self.p+70*h
            elif (g==4):
                 h=int(input("No.of hours:"))
                 self.g=self.p+90*h
            elif (g==5):
                 h=int(input("No.of hours:"))
                 self.g=self.p+50*h
            elif (g==6):
                 break
            else:
                 print("Invalid option")

            print("Total Game Bill=Rs",self.p,"/n")
        

    def display(self):
        print ("******HOTEL BILL******")
        print ("Customer details:")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.s)
        print ("Your Food bill is:",self.r)
        print ("Your Game bill is:",self.g)

        self.rt=self.s+self.t+self.p+self.r+self.g

        print ("Your sub total Purchased is:",self.rt)
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal Purchased is:",self.rt+self.a+self.g,"\n")
        self.rno+=1

            
def main():

    a=hotelmanage()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate Room Rent")

        print("3.Calculate Food Purchased")

        print("4.Calculate gamebill")

        print("5. Show Total cost")

        print("6.EXIT")

        b=int(input("\nEnter the number of your choice:"))
        if (b==1):
            a.inputdata()

        elif (b==2):

            a.roomrent()

        elif (b==3):

            a.foodpurchased()

        elif (b==4):
            a.gamebill()

        elif (b==5):

            a.display()

        elif (b==6):

            quit()



main()