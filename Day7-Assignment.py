#Analyze and samples of tuple

#1.Ordered: Tuple maintain the order of elements.

elements=(10,20,30,40,50,60,70)
print("elements",elements)
                               #output:[10,20,30,40,50,60,70]


#2.Immutable: Once created u cannot modify a tuple.

elements=(1,2,3)
elements(0)=100
                              #output= Error


#3.Allow Duplicates: Tuples can store duplicate values.

elements=(10,20,30,10)
print(elements)
                              #output=[10,20,30,10]



#4.It stores different data types

elements=(10,20,"jawahar",11.9,"true")
print(elements)
                             #output=(10,20,"jawahar",11.9,"true')


#5. slicing : It also support slicing

 elements=(10,20,30,40,50)
 print('elements[0:4]',elements)
                              #output=10, 20, 30, 40
 

 #6.Append : Tuple has no attribute append

 elements.append(60)
 print('after append',elements)
                              #output=Error

 

 #7.Insert : Tuple has no insert attribute

 elements.insert(25)
 print('after insert',elements)
                              #output=Error





