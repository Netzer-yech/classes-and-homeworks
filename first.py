name='netzer'
print(name)
num=3
age=31
print(age)
name2='yechezkel'

# f string
# good for using when strings are long and when you want to print a big number of strings

print(name+name2)
print(f'{name} {name2}')
print(f'{name} {name2}')

# casting

print(name + str(num))
print(name,num)


# operators arithmatic

a=100
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)

c='my age is'
d=31
print(c+str(d))
print(c,d)
print(c+" "+str(d))

# statements
# if
# operator bolian

if a>b:
    print('true')

if a<b:
    print('false')
# code is ok but a bigger then b so python not printed 'flase'

# else
if a<b:
    print('true')
else:
    print('false')

# elif

if a<b:
    print('false')
elif a==b:
    print('wrong')
elif a != b:
    print('correct')
else:
    print('check')





