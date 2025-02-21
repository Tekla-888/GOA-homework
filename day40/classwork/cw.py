#Function 1 - hello world


def greet():
    
    return "hello world!"
#Counting sheep..

def count_sheeps(sheep):
    return sheep.count(True)




def no_space(x):
    return x.replace(" ", "")



# 1)

def count_sheeps(sheep):
    return sheep.count(True)


# 2)

def no_space(x):
    return x.replace(" ", "")

# 3)

def double_integer(i):
    return i*2


def greet(name):
    return "Hello, {} how are you doing today?".format(name)

def greet(name):
    return f"Hello, {name} how are you doing today?"





def boolean_to_string(b):
    return str(b)

def litres(time):
    return time // 2

def litres(time):
    return int(time * 0.5)





def century(year): 
    return (year + 99) // 100
#amisia
def century(year): 
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1






#Function 1 - hello world
def greet():
    return "hello world!"

#Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)


#Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

#You Can't Code Under Pressure #1
def double_integer(i):
    return i*2

#Returning Strings
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

#Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)

#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1+value2
    elif operator == "-":
        return value1-value2
    elif operator == "*":
        return value1*value2
    elif operator == "/":
        return value1/value2

#Keep Hydrated!
def litres(time):
    return time//2

#Century From Year
def century(year):
    return (year + 99) // 100

def digitize(n):
    starting_str = str(n)
    reversed_str = starting_str[::-1]
    
    res_list = []
    
    for i in reversed_str:
        res_list.append(int(i))
    
    return res_list


def maps(a):
    saver=[]
    for i in a:
        saver.append(i*2)
    return saver