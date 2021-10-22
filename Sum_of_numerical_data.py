import re
handle=open('assignment.txt')
lst=list()
sum=0
for line in handle:
    line=line.strip()
    stuff= re.findall('[0-9]+', line)
    for n in range(0,len(stuff)):
       num= int(stuff[n])
       lst.append(num)
for n in range(0,len(lst)):
    sum=sum+lst[n]
print(sum)