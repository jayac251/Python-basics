def Collatz(number):
    val = 0
    if(number % 2==0):
        val=number //2
        print("even :" , val)
        return val

    else : 
        val =  3 * number + 1
        print( "odd: " , val)
        return val;

try:
    userInteger = input("Enter Number: ")
    while(userInteger != 1):
        userInteger = Collatz(int(userInteger))
        # print("userInput", userInteger)
except Exception as ex:
    print("Exception Occured: Enter integer", ex.args)
    



==========================================================
animals = ['cat', 'mouse', 'rabbit', 'pig','cow']
print(animals[1:6])
print("length:" , len(animals))
==================================================

fruits = []
while True:
    print("Enter name of fruit " , len(fruits) + 1 ,  '(Or enter nothing to stop.)')
    fruit=input();
    
    if(fruit == ''):
        break
    
    fruits = fruits + [fruit]

print('Fruit names are: ')
for fruit in fruits:
    print (fruit)

===============================================
cat = ['white','fat','fierce']
color, size, nature = cat
print(color, size, nature)
========================================
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
print('\n')
for index, item in enumerate(supplies):
    print('Index ' , index , ' in supplies is: ' ,item)
================================================
import random
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
random.choice(supplies)
random.shuffle(supplies)

print(supplies)

===============================================
from math import *
sqrt(2)
=====================================
#tuple
a,b,c = 'blue','black','red'

print(a,b,c)

balls = a,b,c

print(balls[1])
=========================
#Range
#range (<startvalue>, <endvalue>, <stepsize>)

x = range(3, 20, 2)
for n in x:
  print(n)

r2 = range(5,16) # 5...15
for r in r2:
    print (r) 

r3 = range(4,21,2) # 4...20 step 2
for r in r3:
    print (r)

r4 = range(15, 4, -5)
for r in r4:
    print (r)

r5 = range(0,11)
print(r5[:]) 
===================================
#getting list from another list
fruits = ['apple','banana','orange','pineapple','cherry']

favfruits = fruits[1:3]
print("Fruits: ", fruits,'\nFavorite fruits:',favfruits)

#delete an item from list
del fruits[2]
print("Fruits: ", fruits)

#using range
for i in range(len(fruits)):
    print('Index ' + str(i) + ' in fruits is: ' + fruits[i])

print('apple' in fruits)
print('guava' in fruits)
print('grape' not in fruits)

random.choice(fruits)
random.shuffle(fruits)
print(fruits)

fruits.index('pineapple')
fruits.append('mongoosteen')
fruits.insert(1, 'mango')
fruits.remove('pineapple')
fruits.sort(reverse=True)

for index, fruit in enumerate(fruits):
    print('Index ' + str(index) + ' in fruits is: ' + fruit)
====================================================
diction = {'key1':'val1', 'key2':'val2','key3':'val3'}
print(diction)


house = {'color':'yellow', 'floors':'2','age':'12 years'}
print(house)

print(house.keys())
print(house.values())

for k,v in house.items():
    print ('House\'s ',k,' is ',v)

print('Getting House\'s Rooms',house.get('rooms',0))

house["rooms"]=2
#house.update({'rooms',2})

print('Added new rooms, Now Getting House\'s Rooms',house.get('rooms',0))

house.update({"rooms": "4"})
print('Rooms Updated! Getting House\'s Rooms',house.get('rooms',0))
===================================================================
#Nested Dictionary

Friends = {'Supraja': {'fruit':'apple','age':7,'gender':'f'},
            'Girisha':{'fruit':'banana','age':5,'gender':'f'},
            'Adhira':{'fruit':'mango','age':9,'gender':'f'},
            'Ashwin':{'fruit':'orange','age':10,'gender':'m'}            
            }

for k,v in Friends.items():
    print('Friend name:', k)
  
    for key,val in v.items():
        print('Key:',key)
        print('Value:' , val)

       
for k,v in Friends.items():
    flag='she'
    if(v.get('gender')=='m'):
        flag='he'
    print(k,' is ',v.get('age'),' years old and ',flag,' likes ',v.get('fruit'),' very much :)')   
        
        #print('Friend ',k,' is ',v1.get('age'),' years old and favorite fruit is ',v1. )
