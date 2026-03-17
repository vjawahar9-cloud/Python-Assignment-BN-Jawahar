

#1.Implement multithreading for any real time example

import time
import threading


def youtube_video():
    for i in range(3):
        time.sleep(1)
        print("video playing...")

def youtube_comments():
    for i in range(3):
        time.sleep(3)
        print("loading comments...")

t1=threading.Thread(target=youtube_video)
t2=threading.Thread(target=youtube_comments)

t1.start()
t2.start()






#2.write studnet's rollno, name in a file and then display it on screen


fp=open("C:\\Users\\vjawa\\Desktop\\PYTHON WORK NOTES\\students.txt","a+")

student_rollno=input("Enter the student roll no : ")
student_name=input("Enter the student name: ")


fp.write(student_rollno + " " + student_name )

fp.close()



fp=open("C:\\Users\\vjawa\\Desktop\\PYTHON WORK NOTES\\students.txt","r")

for line in fp:
    print(line)































