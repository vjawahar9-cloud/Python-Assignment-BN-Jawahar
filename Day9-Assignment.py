
# 1. No parameter , No return type

def total_price1():
    price=20
    quantity=10
    total=price*quantity
    print("total price=",total)

total_price1()
                               #output: total price= 200



# 2. Parameters , no return type

def total_price2(price,quantity):
    total = price*quantity
    print("total price",total)

price=200
quantity=4
total_price2(price,quantity)
                               #output:total price 800



# 3. No parameters, with return type

def total_price3():
    price=300
    quantity=2
    return price * quantity

result=total_price3()
print("total price=",result)
                               #output:total price= 600



# 4. parameters with return type

def total_price4(price,quantity):
    return price*quantity

price=400
quantity=3
result=total_price4(price,quantity)
print("total price=",result)
                                #output:total price= 1200



    
