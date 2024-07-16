a = int(3)
b = 4 #sets to int automatically
c = float(2)
d= 2.0 #sets to float auto

e = a+c # int + float = float
#any arithmentic will change to float

#a//b: gives qutioent
#a%b: gives remainder
#a**b: a to the exponent of b

#Boolean
# 1 = true, 0 = false

a += 3
print(a)

#String
# using '' or "" is fine, but ""is preferred
a = "thank"
b = "you"
#a*2 prints a twice
print(a+" "+b)

a = "Seojun"
name = a

print(name)

email = "seojunlee@gmail.com"


print("{}'s email address is {}".format(name,email))


s = "2021-06-01"
result = s.split('-')
print(result)

result2 = '-'.join(result)
print(result2)

#upper(): all capital
#lower(): all lowercase
#capitalize(): caplitalize the first letter
#ex. email.upper()

ex = s.center(50)
print(ex)
ex1 = s.center(50, '*')
print(ex1)

s.count('2021')# counts how many 2021 there are
s.find('2021')# tells you where 2021 is 

ex.strip() #removes " "
ex1.strip('*') # removes *

"adsf123".isalnum() #returns true
"312334".isdecimal() # returns true
"3123".isdigit() # returns true

"a".isidentifier() # checks if the variable is valid, this will return true
"31a".isidentifier() # returns false

'3 \n dd'.isprintable() # cuz of \n, it is false

" ".isspace() #true

a  =""
b=" "
len(a) #is 0
len(b) #is 1

#Q1. 

x= 5.0
y = 3
c = x+y

print("x + y is {}".format(c))

#Q2. 

x = "than3k"
y = "yo97u"
print(x.replace("3","")+ " "+y.replace("97",""))