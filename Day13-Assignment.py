#1.create set of objects using LIST datatype




class car:
    def __init__(self,carname,carprice):
        self.carname=carname
        self.carprice=carprice

    def display(self):
        print("carname",self.carname,"carprice",self.carprice)

c1=car("kia",1100000)
c2=car("hyundai",1000000)
c3=car("maruti",700000)

car_list = [c1,c2,c3]

for c in car_list:
    c.display()
