#!/usr/bin/python3
import re
print(1+1)
print("hello")
line = "X-server: main server"
if(re.search('^X.*:',line)):
    print(line)

line1 = "X-plane is behind sechedue : 2hours"
if re.search('^X-\S+:',line1):
    print("non whitespace",line1)
    pass

if(re.search('^X.*:',line1)):
    print(line1)

# find all returns a list
x = 'my birth day is march 10 and roll number is 56'
y = re.findall('[0-9]',x)
print(y)

y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[0-9]*',x)
print(y)

y = re.findall('[AEIOU]+',x)
print(y)

#greedy matching ,
#exp matches with 'From:' and 'From: Using the :', so greedy returns The
#biggest match
x = 'From: Using the : character'
y = re.findall('^F.+:',x)
print(y)

#not greedy
y = re.findall('^F.+?:',x)
print(y)

y1 = re.findall('^F\S+:',x)
print("y1",y1)


mail = "From joeal.james@gmail.com : hello \n To james.joeal@gmail.com"
#gets all emails
print(re.findall("\S+@\S+",mail))

#finetuning getting email only From
print(re.findall("^From (\S+@\S+)",mail))

#
atpos = mail.find('@')
sppos = mail.find(' ',atpos)
print(mail[atpos+1 : sppos])

#using dual split
words = mail.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])

#using regular Expression
print(re.findall('@(\S+)',mail))
print(re.findall('@([^ ])',mail))
print(re.findall('From.+@([^ ]+)',mail))

hand = open('/home/vijay/Documents/Python_AccessingWeb/mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence:.*([0-9.]+)',line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Max:',max(numlist))

# '[0-9.]+' chars 0,1,2,3,4,5,6,7,8,9,'.' repeated once or more than once

score = 'my score is 3.7 and my cgpa is 3.8'
print(re.findall('[.0-9]+',score))
print(re.findall('[.0-9]+',score)[0])
print(re.findall('[.0-9]',score))
