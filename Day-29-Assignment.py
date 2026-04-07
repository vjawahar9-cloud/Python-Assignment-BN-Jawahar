#1.Comprehension function

'''customers = [
    {"name" : "sudhakar","feedback" : "food is good"},
    {"name" : "edwin","feedback" : "food is ok"},
    {"name" : "prem","feedback" : "food is fine"},
    {"name" : "malik","feedback" : "food is well"}
    ]

customers = [cus for cus in customers if "good" in cus["feedback"]]

print(customers)



#output:
          [{'name': 'sudhakar', 'feedback': 'food is good'}]'''




#2.Decorator Function:


def  additionalfunction(functionptr):

    def wrapperfunction():
        print('...Welcome to my project...')
        functionptr()
        print('...Lets start...')
        
    return wrapperfunction

@additionalfunction
def sayhello():
        print("wait a minute")

sayhello()
