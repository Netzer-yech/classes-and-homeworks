
# statements
# loops

for x in range (5):
    print(x)
# number of iteration
for x in range (4,5):
    print(x)
# 4 is the value of x. 5 is number of iteration
for x in range (0,10,2):
    print(x)
    if x == 4:
        break
# 0 is value of x. 10 is number of iteration. 2 is amount of increment


# whlie loop

count = 10
while count < 15:
    print(count)
    count +=1
    if count == 12:
        break
# break is stop the loop, not the code.
# += means value of count +1

# continue

for x in range(10):
    print(x)
    if x == 3:
        continue

# function

def run_1():
    a = 2
    b = 10
    print(a * b)

run_1()

def run_2():
    return 100/2

value = run_2()

print(value)


def run_3(x):
    print(x * 2)

run_3(5)

def run_4(y):
    yech = 100
    return 'hello' + y


welcome = run_4(' world')

print(welcome)

def person(name, age):
    print(name, age)

person('netzer', 31)

net = 15
# global variable

person('netzer', net)

# person('netzer', yech)
# yech is local variable in run_4 so python sending error

# data structures


list_1 = ['netzer', 31, 'noa']
list_1.append('gil')
print(list_1)
list_1.insert(1, 'yechezkel')
print(list_1)
print(list_1[3])
list_1.insert(3, 'zeevi')
print(list_1[3])
list_1.pop(-1)
print(list_1)
# gil was removing by pop function
list_1[0]= 'net'
print(list_1)
print(list_1[0:2])
# printing only index 0 until 2 not include 2
print(len(list_1))
# count elements in data structures
for x in list_1:
    print(x)
    if x == 31:
        break

tuple = 'spring', 'summer', 'fall', 'winter'

my_dictionery = {'netzer': 123, 'noa': 456, 'gil': 789}
print(my_dictionery['netzer'])
print(my_dictionery.values())
print(my_dictionery.keys())


# keyboard input

name = input('please enter your name in console')
print('hello', name)

number = int(input('please enter you age'))
print(10 * number)
# casting input value to int because default value in input is string


