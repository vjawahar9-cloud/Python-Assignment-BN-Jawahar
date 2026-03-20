#UPDATE QUERY

##import mysql.connector
##
##conn=mysql.connector.connect(host="localhost",database="userdb1",user="root",password="jawahar1497@",use_pure=True)
##
##cursor=conn.cursor()
##
##uid = int(input("Enter the user id"))
##
##upassword = input("Enter the password")
##
##query="update userlogin set userpassword=%s where userid=%s"
##
##cursor.execute(query,(upassword,uid))
##
##conn.commit()
##
##conn.close
##
##print("password updated successfully")




#SEARCH QUERY

import mysql.connector

conn=mysql.connector.connect(host="localhost",database="userdb1",user="root",password="jawahar1497@",use_pure=True)

cursor=conn.cursor()

uid=int(input("Enter the user id"))

query="select * from userlogin where userid=%s"

cursor.execute(query,(uid,))

result=cursor.fetchone()

if result:
    print("userid:", result[0])
    print("username:", result[1])
    print("userpassword:", result[2])

else:
    print("no user")



conn.close()


                  
