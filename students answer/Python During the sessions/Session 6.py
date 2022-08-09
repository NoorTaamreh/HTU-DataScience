import re
#1
p='^S..A$'
s='SARA'
result=re.match(p,s)
if result:
    print("match1")
#2
p='^b'
s='abc'
result=re.match(p,s)
if result:
    print("match2")
else:
    print("no match2")
#3
p='^ab'
s='abc'
result=re.match(p,s)
if result:
    print("match3")
else:
    print("no match3")
    
#4
p='[a-e]'
s='abc'
result=re.match(p,s)
if result:
    print("match4")
else:
    print("no match4")

#5
# ask eng about this 
p='a$'
s='Sara'
result=re.match(p,s)
if result:
    print("match5")
else:
    print("no match5")
result=re.findall(p,s)
print (result)
    
#6
# ask eng about this 
p='\bfoo'
s='a football'
result=re.match(p,s)
if result:
    print("match6")
else:
    print("no match6")
result=re.findall(p,s)
print (result)
    
#7
# ask eng about this 
p='foo\b'
s='a foo test'
result=re.match(p,s)
if result:
    print("match7")
else:
    print("no match7")
result=re.findall(p,s)
print (result)

#8
# ask eng about this 
p='\Bfoo'
s='a football'
result=re.match(p,s)
if result:
    print("match8")
else:
    print("no match8")
result=re.findall(p,s)
print (result)

#9
# ask eng about this 
p='foo\B'
s='a foo test'
result=re.match(p,s)
if result:
    print("match9")
else:
    print("no match9")
    
result=re.findall(p,s)
print (result)
    
#10
p='\d[0-9]'
s='12bs89'
result=re.match(p,s)
if result:
    print("match10")
else:
    print("no match10")
    
result=re.findall(p,s)
print (result)
    
#11
#ask eng about this
p='\D[0-9]'
s='1289'
result=re.match(p,s)
if result:
    print("match11")
else:
    print("no match11")
    
#12
p='\D+'
s="Hello 12 Hi 89"
result=re.findall(p,s)
print(result)

