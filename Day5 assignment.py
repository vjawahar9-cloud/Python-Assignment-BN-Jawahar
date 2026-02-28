#Question 1

for i in range(3):
    if i==0:
        print("    *")
    elif i==1:
        print("  * *")
    else:
        print("* * *")

#Question 2

for i in range(5):
    if i == 0 or i == 4:
        print("   *")
    elif i == 1 or i == 3:
        print(" * *")
    else:
        print("* * *")
