# HomeWork#1 Split long string 'mycustomtext' by chars space and concut reversed chars with dash

phrase = "mycustomtext"

phrase = ' '.join(phrase) #add spaces
phrase = phrase.replace(" ","-") #replace spaces with dash
print(phrase[::-1]) #reverse