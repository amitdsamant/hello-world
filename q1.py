'''
s="Python is Object Oriented"
print(s[-1]) #d
print(s[::-1]) #detneirO tcejbO si nohtyP print reverse with increment of 1
print(s[:-1]) #Python is Object Oriente
print(s[1:1]) #empty string
print(s[4:10]) #on is

#s=""
#print(s[1]) - string index out of range

S='Gaurav'
print(s[1]) #name s is not defined

s = 'a b cd'
print(len(s)) #6
print(s[::2])#abc print
print(len(s[::2])) #3


s ="a#b#c#d#"
print(s.split()) #['a#b#c#d#']
print(s.split('#')) #['a', 'b', 'c', 'd', '']
l = s.split('#')
print(l)
s = '$'.join(l)
print(s) # a$b$c$d$

print(1>2) #false


#print(dir(str))
strMethods = ' '.join(dir(str))
print(strMethods)
isavailable = strMethods.find('add') # finds the index of the string
print(isavailable) #prints the index where this str is found

'''
userString = input("Enter a string: ")
print("User entered: "+userString)
#userString = userString.replace(' ', '\n')
#print(userString)
'''
Enter a string: Amit is a good boy
User entered: Amit is a good boy
Amit
is
a
good
boy
'''
userString2 = input("Enter 2nd string: ")
swapString = userString
userString = userString2
userString2 = swapString
print("printing first string..."+userString)
print("printing second string..."+userString2)







