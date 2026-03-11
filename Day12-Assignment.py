

#1.Remove duplicates from string

##text=input("Enter the text")
##result=""
##for ch in text:
##    if ch not in result:
##        result=result+ch
##
##        print("result",result)
##                                       #output:
##                                            Enter the text :jawahar
##                                                        result j
##                                                        result ja
##                                                        result jaw
##                                                        result jawh
##                                                        result jawhr
##       
 




#2.Remove duplicates words from string

text1=input("Enter the words")
text2=text1.split()
result=[]

for word in text2:
    if word not in result:
        result.append(word)

        print("result","".join(result))


##                                         output:
##                                             Enter the word:Geeks for Geeks

        
        


