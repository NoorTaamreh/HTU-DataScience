#list
print("#list eg.")
list=['Noor', 'Ibrahim', 'Saber', 'Al Taamreh']
print (list)
print(list[1:3])
print(list*2)
print(list+list)
list.append('test')
print(list)
print("\n\n")
#you can use append, pop , reverse, sort.

#tuple---------------------------------------
print("#tuple eg.")
T=('Noor', 'Ibrahim', 'Saber', 'Al Taamreh')
print(T)
print(T*2)
print("\n\n")
#print(T.sort)

#set-----------------------------------------
print("#set eg.")
#in set you can use add, and pop.
set1={1,2,2,2,4,5}
print(set1)
print("\n\n")

#dictionaries--------------------------------
print("dictionaries eg.")
dic={}
dic['Key1']="Value 1"
dic['Key2']='Value 2'
dic[3]='Value 3'
print(dic)
print(dic['Key2'])
print(dic.keys())
print(dic.values())
print("\n\n")

#time--------------------------------------
print("time eg.")
import time
print(time.time())
time1=time.localtime(time.time())
time2=time.asctime(time.localtime(time.time()))
print(time1)
print(time2)
print("\n\n")

#if statment--------------------------------
print("#if statment eg.")
x=-7
if x==5:
    print("True1")
else:
    print("False")

#elif-------
print("#elif eg.")
x=-7
if x==5:
    print("True1")
elif x>=-1:
    print("True2")

elif x<=0:
    print("True3")
else:
    print("False")
print("\n\n")

#condition statment
print("#condiotion statment eg.")
if x<5 and x>0:
    print("Ture4")
else:
    print("False")
if x<5 or x>0:
    print("Ture5")

print("\n\n")

#insted condiotion-------------
print("#insted condiotion eg.")
car=1
color="Blue"
if car==1:
    print("user has a car")
    if color=="Blue":
        print("Blue car found ")
    else:
        print("Blue car not found")
else:
    print("user doesn't have a car ")

print("\n\n")

#Loop--------
print("#Loop eg.")
for counter in range(5):
    print("Loop1 test")

for conter in range(0,4,2):
    print("Loop2 test")

for conter in range(10,6,-2):
    print("Loop3 test")
print("\n\n")

#while loop ---------
print("#while loop eg.")
x=0
while x<4:
    print("while loop")
    x+=1
