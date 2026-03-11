


'''1.User enter a number N.
     Print all even numbers from 1 to N using a loop and check using decision making.'''

'''n=int(input("Enter the number"))

for i in range(1,n+1):
    if i%2==0:
        print(i , end="")

                           #output: value enter :10
                           #Ans   : 2 , 4 , 6 , 8 , 10

                           #output: value enter :8
                           #Ans   : 2 , 4 , 6 , 8'''



'''2. User enter a number.
Print the multiplication table up to 10 using a loop.'''

'''n=int(input("Enter the number"))
for i in range(1,11):
    print(n , "x", i,"=",n*i)'''


                            #output : value enter : 2
                          #  ans    :  2 x 1 = 2
                          #            2 x 2 = 4
                          #            2 x 3 = 6
                          #            2 x 4 = 8 
                          #            2 x 5 = 10
                          #            2 x 6 = 12
                          #            2 x 7 = 14
                          #            2 x 8 = 16
                          #            2 x 9 = 18
                          #            2 x 10 = 20 


'''3.User enters 10 numbers using a loop.
Count and display how many numbers are:

Positive

Negative

Zero'''

'''positive=0

negative=0

zero=0

for i in range(1,11):
    num=int(input("Enter the number"))

    if num>0:
        positive+=1
    elif num<0:
        negative+=1
    else:
        zero+=1

print("postive numbers",positive)
print("negative numbers",negative)
print("zero numbers",zero)'''


                         #output: value enter=-1
                                # value enter=-2
                                # value enter=-3
                                # value enter=-4
                                # value enter=-5
                                # value enter=1
                                # value enter=2
                                # value enter=0
                                # value enter=3
                                # value enter=4

                                #Ans: positive=4
                                     #negative=5
                                     #zero    =1






'''4.User must enter username and password.

Rules:

Correct username = "admin"

Correct password = "pass@123"

Allow 3 attempts only using a loop.
If correct → display Login Successful
If wrong after 3 attempts → display Account Locked'''


attempt=0

while attempt<3:
    username=input("Enter the username")
    password=input("Enter the password")

    if username=="admin" and password=="pass@123":
        print("login sucessful")
        break

    else:
        print("invalid")

    attempt+=1
if attempt==3:
    print("Account locked")


                       '''output:Enter the usernamejoe
                               Enter the password1234
                               invalid
                               
                               Enter the usernameanand
                               Enter the password1234
                               invalid
                               
                               Enter the usernamejeeva
                               Enter the password1234
                               invalid
                               Account locked'''



'''5.Question:
User keeps entering numbers.
Program should add the numbers using a loop.

Condition:

If user enters 0, stop the loop and print the total sum.'''


'''total = 0

while True:
    num = int(input("Enter a number: "))
    
    if num == 0:
        break
    
    total = total + num

print("Total Sum =", total)'''
    
        





























































                          
                             
