# HomeWork#1 Split long string 'mycustomtext' by chars space and concut reversed chars with dash

phrase = "mycustomtext"

phrase = ' '.join(phrase) #add spaces
phrase = phrase.replace(" ","-") #replace spaces with dash
print(phrase[::-1]) #reverse


#Correct answer 
phrase = "mycustomtext"

phrase = ' '.join(phrase).replace(" ","-")
print(phrase[::-1])


# HomeWork#2

import re

phrase = "replace spaces with dash"
result = re.match("dash", phrase)
print(result)