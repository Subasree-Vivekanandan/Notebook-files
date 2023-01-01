#print(round(3.5))
#print(abs(-50))


print(bin(5))
print(int('0b101',2))

Name = "suba"
print(Name)

a,b,c = 1.3,50,3.6543
print(a,b,c)

__hihi ="hi"
print(__hihi)

PI = 3.14
print(PI)
PI=100
print(PI)

# augmented assignment operator

some_value = 10
some_value /= 2
print(some_value)


# strings

newStr= "suba"
singlequote = 'new year wishes'

multiplequote = '''
hi there,
Santa here,
wishing ''' + newStr +''' a Very
successful year ahead 23' 
Cheeeeeeerss!
'''

print(multiplequote)


#string concatenation

first_name ="suba"
last_name ="sree.v"
full =first_name + last_name
print(full)


# type conversion

intgr = str(100)
print(type(intgr))

# Escape sequences

print("\nHello there,\nit\'s Santa here:\n\t"+newStr+"\'s gift is here!")

# formatted string

year =2023
print(f'\nFormatted string ex:\nHello {newStr} \nYou\'r gift is {year}')

# dot format

print("\nDot format ex:\nhello {} your age is {}".format("suba",55))

# string indexes
# slicing - [start:stop:stepover]

string = "subasree.v"
print("reverse string: \n\t"+string[::-1])
print("\n")

print(string[0::2])
print(string[::-2])
print(string[::-1])

# strings are immutable

st = "how are you?"
print(st[4:7])
#st[0]="s" does not support 
print(st)

#length

print(len("helloo"))

# methods ex: .format(name,age)

name ='sUba'
print(name.upper())
print(name.capitalize())
print(name.lower())

title = 'EEG based attention detection using ML'
print("\nIndex of detection : ")
print(title.find("detection"))

print(title.replace("detection","monitoring"))
print(title)

# Booleans
print(bool(0))
# suba = bool(input("enter your name: "))
# print(type(suba))
# if(suba==True):
#     print("your are suba")
# else:
#     print("you are not suba")

# age = input("enter your birth year: ")
# print(age)
# print(type(age))
# age =int(age)
# print(type(age))

# username=input("enter username:\n")
# password = input("enter your password\n")
# secret = len(password)*'*'
# print(f'hey {username},\tyour password is {secret} and\tit\'s {len(password)} long' )


#list 
myorder = ["earphone","phonecase","arduino"]

print(myorder[0])

#matrix
print("\nAfter matrix:\n")
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(mat)

# slicing

print(myorder[0::2])


# list - mutable

myorder[1] ="Raspberry pi"
print(myorder)

# copying a list does not modify the original list
print("\ncopying a list\n")
neworder = myorder[:]
neworder[0]="jumping wires"
print(neworder)
print(myorder)


# assigning a list modifies the original list becz the assigned list points to the
#memory address of original list
print("\nAssigning a list \n")
listassign = myorder
listassign[0] = "rgb led"
print(listassign)
print(myorder)


#methods perform on list
#methods modify the original list does not create a copy of the list 
# means methods on performing actions does not return anything

#APPEND

num = [1,8,2,5,4]
num.append(10)
#newnum = num.append(100) # print(newnum) will return NONE
newnum =num
print("\nAfter append\n")
print(num)
print(newnum)

#INSERT # list.insert(index,element)

print("\nAfter insert\n")
newnum.insert(7,100) # [1,8,2,5,4,10,100]
print(newnum)
print(newnum[6])
#print(newnum[7]) # index out of range

#EXTEND

print("\nAfter extend: \n")
newnum.extend([200,101])
print(newnum)
print(num)

#POP # exception : this method returns the element that will be popped out
print("\nAfter pop:\n")
newnum = num.pop()
num.pop(0)
print(newnum)
print(num)

# REMOVE # list.remove(element)

print("\nAfter remove\n")
#newnum = num.remove(5) # returns nothing
#print(newnum) # returns none
num.remove(5)
print(num)

# CLEAR

newnum = num.clear()
print(newnum)
print(num)

#INDEX
print("\nUsing index: \n")
num=['a','b','c','d','e','b']
print(num.index('b'))
print(num.index('b',2,6))
#print(num.index('s')) # throw error since 's' is not in the list

#IN
print("\nAfter IN keyword: \n")
print('s' in num)
print ('b' in num)
print('b' in num[2:])

print ('suba' in 'hello there suba')


#COUNT
print("\nAfter count: \n")
print(num.count('b'))
print(num.count('s'))


# sort

print("\nAfter sorting :\n")
alpha =['a','d','x','d','s','b']
alpha.sort()
print(alpha)

# reverse

print("\nAfter reversing:\n")
alpha.reverse()
print(alpha)

# range
print("\nAfter range: \n")
print(list(range(1,100)))

# join
print("\nAfter join:\n")
print(' '.join(["hi","suba","new","year","greetings"]))

#list unpacking
print("\nAfter unpacking:\n")
a,b,c,*other,d = [1,2,3,4,5,6,7,8,9,10]

print(a)
print(b)
print(c)
print(other)
print(d)

#none
print("\nAfter none:\n")
a=None
print(type(a))

# Dictionaries - unordered list of key-value pairs
#keys must be immutable - int,string,True,False,tuple

print("\nAfter dictionary:\n")
dict1 = {
    "name": "suba",
    "rollno": 349,
    'subjects' : ["CN","OOAD","TOC","AI","MP"],
    "marks" : { "CN" : 10, "OOAD":9 , "TOC":10, "AI":8, "MP":9},
    "gpa": 9.31
}


print(dict1['marks']['CN'])


# DICTIONARY WITHIN list

print("\ndict inside list\n")

student_history=[
    {
        "name": "suba",
        "rollno" :349,
        "gpa" : 9.31
    },
    {
        "name":"ruba",
        "rollno" : 238,
        "gpa":9.18
    }
    ]

print(student_history[0]['name'])

# dict methods

# get  # dict.get(key,valueifkey does'nt exist)
print("\nAfter get:\n")
user = {
    "name" : 'xyz',
    "area" : "hwuih"
}
print(user.get("mark")) # returns none if key doesnt exist
print(user.get("course","BE"))

# in  # 'key' in dict.keys()
print("\nAfter in:\n")
print('name' in user.keys())
print('cse' in user.values())
print(user.items())

#clear # clears the dictionary # dict.clear()

print("\nAfter clear:\n")
user.clear()
print(user)

#copy # creates a copy of original dictionary

print("\nAfter copy:\n")
new_dict = {
    "name":"PSG",
    "dept" :"cse",
    "year" : 3
}

next_dict = new_dict.copy()
print(new_dict)
print(next_dict)

# pop 

print("\nAfter pop:\n")

print(next_dict.pop("name"))

#popitem  #pops any key-value pair from dictionary (not the last last one since it is unordered)

print("\nAfter popitem:\n")

print(next_dict.popitem())

#update # dict.update({key:value})

print("\nAfter update\n")

next_dict.update({"dept":"CSE"})
print(next_dict)


# Tuple - immutable

tuple1 =(1,2,3,4,"suba")
print(tuple("tuple")+tuple1)

new_tuple = tuple1[2:]
print(new_tuple)
print(tuple1)

print(new_tuple.count('suba'))
print(len(new_tuple))
print(new_tuple.index('suba'))

# SETS - unordered collection of uniques objects

set1 = {1,2,3,45,45,55,66,55}
print(set1)

set1.add(100)
set1.add(2)

print(set1)

listtoset =[1,2,3,2,5,2,5,6,7,8,7]
print(set(listtoset))


print(10 in set1)
print(len(set1))

new_Set= set1.copy()
new_Set.add(150)
set1.clear()
print(new_Set)
print(set1)

# methods

set_1 = {1,2,3,4,5,6}
set_2 = {1,5,2,10,11}

print(set_1.difference(set_2))

print(set_1.discard(3))
print(set_1)


print(set_1.difference_update(set_2))
print(set_1)
print(set_1.intersection(set_2))


print(set_1.isdisjoint(set_2)) # nothing common btwn two sets

s1 = {1,2,3}
s2 = {4,5,6,1,2,3}

print(s1.issubset(s2))
print(s2.issuperset(s1)) # s2 encompasses s1
