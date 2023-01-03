from functools import reduce

age = input("What is your age?: ")

def checkDriverAge():
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()


# doc strings

def doc_string(a):
    '''
    this function accepts a parameter 'a' 
    '''
    print("returned by function doc_string: ",a)


help(doc_string)
print(doc_string.__doc__)


# *args , **kwargs    # actual representation def func_name(parameters,*args,default parameters, **kwargs)

def demo_arg(name,*args,i="default param",**kwargs):
    print("\n Arguments : \n")
    print(args)
    print("\n keyword arguments: \n")
    print(kwargs)
    
    print("\n Sum of arguments:\n")
    print(sum(args))

    print("\n Sum of kwargs:\n")
    tot=0
    for i in kwargs.values():
        tot+=i
    return (tot)

print(demo_arg("suba",1,2,3,4, m1=89, m2=95))
num = int(input("enter the number elements in the list\n"))
my_list=[]

for i in range(num):
    print("enter element at position: ",i)
    my_list.append(int(input()))
    
def highest_even(my_list):
    even=0
    for i in range(len(my_list)):
        if(my_list[i]%2==0):
            if(my_list[i]>even):
                even = my_list[i]
            
    return even
        
print("highest_even is :" ,highest_even(my_list))

or new function

def even_high(my_list):
    even_list=[]
    even = 0
    for i in range(len(my_list)):
        if(my_list[i]%2==0):
            even_list.append(my_list[i])
    
    for i in range(len(even_list)):
        for j in range(i+1,len(even_list)):
            if(even_list[i+1] > even_list[i]):
                even = even_list[i+1]
    return(even)
    
print("high even : ",even)
                
            
# scope of variables

def parent():
    a=10
    def func_scope():
        return " a is :",a
    return func_scope()

print(parent())

# 1 - check for a local variable
# 2 - check for parent local
# 3 - check for global variable
# 4 - check for built in functions

def scope_builtin():
    def child():
        return sum
    return child()

print(scope_builtin())

# global

count =0

def global_var():
    global count
    count+=2
    return count
    
global_var()
global_var()
print(global_var())

# or 

tot =0

def global_variable():
    global tot
    tot+=2
    return tot
    
    
global_variable()
global_variable()
print(global_variable())

# non local keyword

def parent():
    x="parent local"
    def child():
        nonlocal x
        x="child nonlocal"
        print("child: ",x)
    child()
    print("parent: ",x)

parent()

# map
print("\nAfter map:\n")
def map_func(i):
    return i+i
print(list(map(map_func,[1,2,3,4,5,6])))   

def filter_func(num):
    return num % 2 ==0

print(list(map(filter_func,[1,2,3,4,5,6,7,8])))

# filter

print("\nAfter filter:\n")
def filter_func(num):
    return num % 2 ==0

print(list(filter(filter_func,[1,2,3,4,5,6,7,8])))


# zip
print("\nResult after zip\n")
x =[1,2,3,4]
y =[5,6,7,8]
z = (10,15,20,25)
print(list(zip(x,y,z)))


# reduce
print("\nResult of reduce:\n")
def func_reduce(acc,i):
    print(acc,i)
    return acc*i

print(reduce(func_reduce,[1,2,3],10))

# list comprehension

print("\nApplying list comprehension:\n")

char_list = [ char for char in "suba"]
ori_list = [num for num in range(10)]
sq_list = [num**2 for num in range(10)]
num_list = [num**2 for num in range(10) if num%2==0]


print(char_list)
print(ori_list)
print(sq_list)
print(num_list)


#set comprehension

print("\nApplying set comprehension:\n")

set1 = { s for s in "subasree.v"}
set2 = { n**2 for n in range(20)}

print(set1)
print(set2)

#dictionary comprehension

print("\nApplying dictionary comprehension\n")

my_dict = {
    'a':1,
    'b':2,
    'c':3
}

dict1 = { k:val*2 for k,val in my_dict.items() }
dict2 = { k:val*2 for k,val in my_dict.items() if val%2==0}

print(dict2)
print(dict1)

# challenge

num_dict = { num:num*num for num in [1,2] }

print(num_dict)


# challenge comprehension

alpha_list = ['a','b','c','b','c','d']
dup =[]
dup = list(set([num for num in alpha_list if (alpha_list.count(num) > 1) ]))

print(dup)





