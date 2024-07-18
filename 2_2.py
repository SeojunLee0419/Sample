score = 30

if score<30:
    print("fail")
elif score >= 30:
    print("pass")
else: 
    print("errror")


for i in range(3):
    print(i)

for i in [0,1,2]:
    print(i)

for i in ["apple", "banana", "cherry"]:
    print(i)

i = 0
while i <3:
    print(i)
    i +=1

while True:
    a = input("Enter a number")
    if not a.isnumeric():
        print("It is not a number")
        break
    elif int(a)%2 == 0:
        print("it is even")
    else:
        print("it is odd")

name = ["Lee", "Kim", "Park"]
for i, j in enumerate(name):
    print(i,j)


lst= list(range(9)) 
lst_odd = [x for x in lst if x%2 ==1]
lst_even = [x for x in lst if x%2 ==0]
print(lst_odd)
print(lst_even)

#Q1. 
lst1 = [1,2,3,4,5,6,7,8,9,10]

i = 0
while i < 5:
   lst1[i]=i+6
   i+=1
j= 5
while j<10:
    lst1[j] = 10-j
    j+=1

#or
lst2 = lst1
print(lst2)

lst2 = lst1[5:] + lst1[:5]
print(lst2)

