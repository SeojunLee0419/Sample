name = ["Leade", "Parfdk", "Osdfh", "Wfdse", "Jusdfng", "Hfdseo", "ㄹㅇㄴ"]
a = dict()
b = []
for i in range(1, len(name)+1):
    b.append("{}번".format)

for i in range(0,len(name)):
    a[b[i]] = name[i]

print(a)

#OR

a = dict(zip(b,name))
print(a)