# i / o
# open a txt file on python
# my_file = open("C:\\automation course\\to do list.txt", 'r', encoding='utf8')
# content = my_file.read()
# print(content)

# wirte to file
# write_to_file = open('C:\\automation course\\to do list.txt', 'a')
# write_to_file.write(' skateboarding')

# packaging

import datetime
print(datetime.datetime.now())
#first datetime is the package
# second datetime is the file
# third datetime is the class
# now is a funcion inside datetime class

try:
    x = 10
    netzer = 10/0
except ZeroDivisionError:
    print('zero division error 1')
# try is casting the code
# if except happend, then it will move to print funcion
# putting the name of the except is good for ordering and good quallity of code writing

try:
    my_file = open('C:\\automation course\\to do list.txt', 'a')
    my_file.read()
except IOError:
    print('i/o error 1')
# file type is 'a' - append , function is read, so except happend


# with open("C:\\automation course\\to do list.txt", 'r') as my_file:
#     my_file.write('hello world')

# using with defined the file that imported as a variable 'my_file' and go to function
# automatically finally function is running file.close function
