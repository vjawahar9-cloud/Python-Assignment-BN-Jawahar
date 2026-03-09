# 1. find biggest number in the list

list_elements =[80,160,240,320,400]

assign_big = 0

for big in list_elements:
    if big>assign_big:
        assign_big = big
print("biggest number is",assign_big)



# 2. noparameter,noreturn_type

def biggestnumber():
    big_num = 0
    elements=[10,20,25,40,100]
    for big in elements:
        if big>big_num:
            big_num = big
    print("biggest number is",big_num)

biggestnumber()




# 3. with parameter,noreturn_type

def biggestnumber(big_num,elements):
    for big in elements:
        if big>big_num:
            big_num = big
    print("biggest number is",big_num)

big_num = 0
elements=[100,80,200,158,225]
biggestnumber(big_num,elements)


    

# 4. with parameter,withreturn type

def biggestnumber(big_num,elements):
    for big in elements:
        if big>big_num:
            big_num=big
    return big_num
big_num = 0
elements=[85,100,125,200,224]
result=biggestnumber(big_num,elements)
print("biggest number is",result)




# 5. no parameter,with return type

def biggestnumber():
    big_num = 0
    elements=[20,40,400,500,100]
    for big in elements:
        if big>big_num:
            big_num = big
    return big_num
result=biggestnumber()
print("biggest number is",result)
