


fhand = open('Data Structure\HomeWork5\README.txt','r',encoding="utf-8")
for line in fhand:
    if not line.startswith('Hw4'):
        line =line.rstrip()
        print(line)
     
     
#print(fhand)
    