first = 7
second = 44.3
print(first + second)
print(first * second)
print(second / first)

a = 8
a = 17
a = 9
b = 6
c = b +a
b = c + a
b = 8

print(a)
print(b)
print(c)

# python using all variable in order of righting. here first variable b is 6
# but later in code we change the value so at the end python using the value 8

name1 = 'john'
name2 = "john"
print(name1)
print(name2)

# there is no different between two examples

my_number = 5 + 5
print("result is" + str(my_number))
# str casting the integer so python can print two string. but no space between "is" and 10.
print("result is" + ' ' + str(my_number))
# adding a string with space

x = 5
y = 2.36
print(x + int(y))
# integer is a whole number so python adding just 2
print(x + y)
# that why python is printing the exact content of variables

if x > y :
    print('big')
if x < y :
    print('small')
# python did not print second if because it is not true
# only first if was printed

season = 5
if season == 1:
    print('summer')
elif season == 2:
    print('winter')
elif season != 3:
    print('fall')
elif season == 4:
    print('spring')
# python check if/elif according to the code line - the first that true will be printed
# this is a system of conditions

age = 31
first_name = 'netzer'
family_name = 'yechezkel'
date_of_born = '01.11.1991'
if first_name != family_name:
    print('error')
elif age < 0 :
    print('unvalid')
else:
    print('all good')

# challenge
n = 8
m = '123'
print(n + int(m))

print(first_name + ' ' + family_name + ' is ' + str(age) + ' years old')
# casting string m with int so python looking at the number 123 as integer
# adding space in string will appear in print
