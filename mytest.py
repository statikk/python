# HomeWork#1 Split long string 'mycustomtext' by chars space and concut reversed chars with dash

phrase = "mycustomtext"

phrase = ' '.join(phrase) #add spaces
phrase = phrase.replace(" ","-") #replace spaces with dash
print(phrase[::-1]) #reverse


#Correct answer 
phrase = "mycustomtext"

phrase = ' '.join(phrase).replace(" ","-")
print(phrase[::-1])

num_1, num_2 = 5, 7
print(num_1 + num_2)


x = float(5)
y = float(6)
z = x + y
print('Result: ' + str(z))




# HomeWork#2
"""Reg Exp""""" 

import re

phrase = "replace spaces with dash"

result = re.findall(".", phrase)
print(result)

import re

phrase = "replace spaces with dash"

result = re.findall("\.", phrase)
print(result)

#-----------alphanumeric only-----------------------------------------
import re

phrase = "replace spaces with dash"

result = re.findall("\w", phrase)
print(result)

#-----------phone numbers-----------------------------------------
import re


#--------------