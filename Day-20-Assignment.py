#create a class and object with custom example


class bike:

    def  getdetails(self):
        self.bikename=input("Enter the bike name")
        self.bikeprice=int(input("Enter the bikeprice"))
        self.bikecc=input("Enter the bikecc")

    def displaydetails(self):
        print("BIKE NAME : ",self.bikename)
        print("BIKE PRICE : ",self.bikeprice)
        print("BIKE CC : ",self.bikecc)

b=bike()
b.getdetails()
b.displaydetails()


#output
BIKE NAME :  R15
BIKE PRICE :  195000
BIKE CC :  155

                           

