import random

#number=random.randint(1,10)
#print(number)
#uess=int(input("please guess the number?"))
#while number !=guess:
    #guess=int(input('uffs!! try again:guess again:'))
#else:
    #print("Congrachlation!!!U r right")

#while True:

    #guess=int(input("please guess the number?"))
    # guess==number:
       #print('la badhai xa')
#n=int(input("Enter the numbers of  rows in needed"))
#for i in range(n):
    #for j in range(i+1):
        #print(j+1,end="")
        #print()

#: Simple Number Triangle Pattern
#rows=5
#for i in range(rows):
    #for j in range(i+1):
        #print(i,end="")
    #print()

#Half Pyramid Pattern of Numbers
#rows=9
#for i in range(rows):
    #for j in range(i):
        #print(j+1,end="")
    #print()

#for i in range(65,70):
    #for j in range(65, i+1):
        #print(chr(j),end=" ")
    #print()

#n=int(input("Enter the number in rows"))
#k=ord("A")
#for i in range(n):
    #for j in range(i+1):
        #print(chr(k),end="")
        #k=k+1
    #print()

#n=int(input("Enter the number in rows"))
#k=ord("A")
#for i in range(n):
    #for j in range(,i+1):
        #print(chr(k),end="")
        #k=k+1
    #print()

#string pattern
#str1=(input("enter string"))
#length=len(str1)
#for i in range(length):
    #for j in range(i+1):
        #print(str1[i],end="")
    #print()

#str1=input("enter string")
#length=len(str1)
#for i in range(length):
    #for j in range(i+1):
        #print(str1[j],end="")
    #print()


str1=input("enter string")
length=len(str1)
for i in range(length):
    for j in range(length-i-1):
        print("",end="")
    for j in range(i+1):
        print(str1[j],end="")
    print()

a=10

