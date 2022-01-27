import random
import string
from unicodedata import numeric 


# chars

letters = string.ascii_lowercase

print(letters + " this is letters")
 

# test = True
# while(test):
#     pword_len = int(input("how long would you like your password to be?"))	
#     if pword_len not in range(7,21): 
# 	    print("enter a valid number between 7 and 21")         
# else:
#         test = False
#         print("your password length is " +pword_len)    
#         numboption = int(input("do you want numbers ?"))

        # use recursion 

def getPwordLength():
    pword_len = (input("how long would you like your password to be?"))	
    # validates string is a number
    if pword_len.isnumeric():
        # changes type to var type of int 
        pword_len = int(pword_len)
        # if outside of range 
        if pword_len not in range(7,21):
            print("enter a number between 7,21")
            # invokes func again 
            getPwordLength()
        else: 
            # confirms response in happy path 
            print("your password length is " +str(pword_len))
            # next stage this is happy path 
    else: 
        # if a string is provided that is not a number
        print("enter a NUMBER between 7,21")
        getPwordLength() 
getPwordLength()

 


# def range(pword_len, 7, maxn):
#     if pword_len < 7:
#         return 7
#     elif pword_len > maxn:
#         return maxn
#     else:
#         return pword_len
    



text = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
'''

file = open("password.html","w")
file.write(text)
file.close()