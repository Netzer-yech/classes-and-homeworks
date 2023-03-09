# a.
x = 5
y = 10
if x < y :
    print('small')
if y > x :
    print('big')
print()

# b.
for m in range(5):
    print(m)
print()
# empty print = clean line in console

# c.
for m in range(5):
    if m == 1:
        print('summer')
    elif m == 2:
        print('fall')
    elif m == 3:
        print('winter')
    elif m == 4:
        print('spring')
print()


# d.
# 10 time when 11 iterations and + 1 every time. all depend on number of iteration and index progres
count = 1
while count < 11:
    print(count)
    count = count + 1
print()

# e.
age = 31
letter = 'y'
shekel_dollar = 3.8
flight = 'true'
apartment = 1
print(age)
print(letter)
print(shekel_dollar)
print(flight)
print(apartment)
print(age + shekel_dollar)
print()

# f.
phone = input("please enter your phone number")
print('phone number : ' + phone)
print()

# g.
def printhello():
    print('hello')
printhello()
def calculate():
    print(5 + 3.2)
calculate()

# h
def printname(name):
    print(name)
printname('netzer')
def divide_by_2(num):
    print(num/2)
divide_by_2(4)

# i
def num_ret_sum(num,num2):
    sum = num + num2
    return sum
print(num_ret_sum(2, 2))

def space_string(str, str2):
    add_space = str + ' ' + str2
    return add_space
print(space_string('netzer', 'yechezkel'))

# j
my_list_num = [1, 3, 5]
for temp in my_list_num:
    print(temp)
# temp is iterate in a list and getting all element without index

# k.
k = [10, 100, 1000]
print(k[0] + k[1] + k[2])
# hard way to print list of number and sum them

def sum_num_list(list):
    sum_num = 0
    for x in list:
        sum_num += x
    print(sum_num)
sum_num_list(k)
# this function will work only with list of numbers
# initially sum_num = 0 just for create variable outside for loop
# then x is variable associated with list elements in every iteration
# for loop body is adding current number in current iteration with the next number of next iteration


# l.
first_dictionery = {'net': 1, 'noa': 2, 'gil': 3}
print(first_dictionery.keys())
# here console is return "dict_keys(['net', 'noa', 'gil'])". to print only keys we use for loop
for keys in first_dictionery.keys():
    print(keys)


# challenge

# m.

for i in range(1,6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

# first loop run 5 time from index 1 until index 5
# second loop get the index from first loop to the range of iteration and adding 1 every iteration
# second loop body print * every iteration according to range number. that why every iteration will get one more *.
# end='' for printing in line every iteration
# empty print at the end for new line in first for loop creating the pyramid stairs


print()

# n.

i = 0
j = 6

for row in range(7):
    for col in range(7):
        if row == i and col == j:
            print('*', end='')
            i = i + 1
            j = j - 1
        elif row == col:
            print('*', end='')
        else:
            print(end=' ')
    print()

# create variables for first condition from our design sketch of the pattern shape (on paper)
# first loop runs 7 times creating 7 lines
# second loop runs 7 times. each time looking at the variables i & j
# second loop looking at three conditions every iteration and printing * when 1 condition taking place
# all conditions printing in line 7 times because of end='', just else condition printing space as end=' '
# after first if we are creating the changes in variables according
# to our design sketch where first variable i increment by one each iteration and a second variable j decrement by one
# empty print at end of first loop create the new line


# o
num = int(input('enter a positive number'))
result = 0
while num > 0:
    digit = num % 10
    result = result + digit
    num = num // 10
print('sum is :', result)
# result=0 outside loop just for starting from 0
# using the while because i dont know which number i will get from input and how many iteration will be processed
# % 10 split the integer by 10 and using only number after decimal point. get digit in loop
# adding to result and start sum the digit in every iteration
# //10 using to bring num to integer after using the % in code above
# at the end, num%10 will bring 0 because numbers are getting smaller every iteration.
# when that happened the while loop will stop by the conditions statement

# p.
my_tuple = ('h', 'e', 'l', 'l', 'o')
for items in my_tuple:
    print(str(items[0]), end='')
# items is a variable in for loop
# number of iteration is similar to number of elements in the data structure
# casting to string and using end='' for printing in line to create the word 'hello'
print()

# q.
list_num = [123, 456, 789, 987, 654, 321, 21, 35, 67, 89, 77, 5, 888]
print(min(list_num))




























