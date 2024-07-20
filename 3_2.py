#file in python
#f = open(name, open type)
#open types: w: write, r: read, a: add
#f.close()

#ex. f = open("info.txt", 'r', encoding='utf8')
#while True:
#   line = f.readline()
#   if not line:
#       break;  
#    print(line)
#f.close()

#ex.2 f = open("info.txt", 'r', encoding='utf8')
#lines = f.readlines()
#for line in lines:
#   print(line)
#f.close()

#ex.3 f = open("info.txt", 'r', encoding='utf8')
#lines = f.read()
#print(lines)
#f.close()

#ex4.  f = open("info.txt", 'a', encoding='utf8')
#f.write('\nheight: 180cm')
#f.close()

#**when you use w, it creates a whole new thing, so it deletes what was originally in there

#ex5. with open("info.txt", 'r', encoding='utf8') as f:
#          data=f.read()
#     print(data)
#**this closes the text file for you

