

#1.IF ELSE PROGRAM

#student grade:

##mark=int(input("Enter student mark"))
##
##if mark>=90:
##    print("Grade A")
##elif mark>=75:
##    print("Grade B")
##elif mark>=35:
##    print("Grade C")
##else:
##    print("fail")





#2. WHILE PROGRAM

    #print numbers 1 to 10:

##i=1
##while i <= 10:
##    print(i)
##    i=i+1


    #print number 10 to 1:
##i=10
##while i >=1:
##    print(i)
##    i=i-1
##    


    #print 1 to 10 and remove number 3:
##i=1
##while i <=10:
##    if i==3:
##        i=i+1
##        continue
##    print(i)
##    i=i+1






#3.FOR LOOP PROGRAM

      #Print list elements

##numbers = [10,20,30,40,50]
##
##for n in numbers:
##    print(n)



        #print students marks
##
##marks=[95,75,90,65,85]
##
##for i in marks:
##    print(i)





#4. CLASS AND OBJECT PROGRAM


##class student:
##    def __init__(self,studentname,studentmark):
##        self.studentname=studentname
##        self.studentmark=studentmark
##
##    def display(self):
##        print("student name",self.studentname,"student mark",self.studentmark)
##
##student1=student("jawahar",95)
##student1.display()
##student2=student("arun",85)
##student2.display()





#5.INHERITANCE PROGRAM:


##class myclass1:
##    def initialize (self):
##        self.a=200
##        self.b=50
##
##    def addition(self):
##        self.c=self.a+self.b
##        print("addition result is",self.c)
##
##class myclass2(myclass1):
##    def subtraction(self):
##        self.c=self.a-self.b
##        print("subtraction result is",self.c)
##
##m1=myclass1()
##m1.initialize()
##m1.addition()
##
##m2=myclass2()
##m2.initialize()
##m2.subtraction()



#6. LIST PROGRAM:

##numbers=[100,200,300,400,500]
##
##for n in numbers:
##    print(n)



#7.TUPLE PROGRAM:

 #find average of student marks

marks = (90,85,80,75,70)

total=0

for m in marks:
    total=total + m

average = total / len(marks)
print("average marks",average)










        



















































       
    
