

students = [
    {"name": "Arun", "marks": [78, 82, 90]},
    {"name": "Bala", "marks": [65, 70, 60]},
    {"name": "Chitra", "marks": [88, 92, 95]}

]



# 1.calculate average for each student:


for student in students:
    total=0
    for mark in student['marks']:
        total = total + mark

    average = total / len(student['marks'])
    student['average']=average
    print(student['name'], 'average=',average)

    #output:
           # Arun average= 83.33333333333333
           # Bala average= 65.0
           #Chitra average= 91.66666666666667




#2.find highest average
    name = ''
    highest_average = 0


for student in students:
    if student['average']> highest_average:
        highest_average=student['average']
        name = student['name']
print("highest average:", name, "=",highest_average)


     #output:
             # highest average: Chitra = 91.66666666666667





#3.list students with average above 80

for student in students:
    if student ['average']>80:
        print(student['name'])


        #output:
             #students above 80 average
                #1.Arun
                #2.Chitra







































             

    
    
        
