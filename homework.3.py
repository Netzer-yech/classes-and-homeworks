# 1&2

try:
    a = 1 / 0
except ZeroDivisionError:
    print('error 1')

# 3
# code is ok
try:
    x = 1
finally:
    print('finally')

# 4
# except is a multy useful statements for all exception

#5
# no wrong using flat except, but its better to categorise your exception.
# also good for making good impression for new job interviews

# 6
# except I/OError using for any type of exception that happened during I/O statements
# except ZeroDevisionError using for math except that devision number with 0

# 7
words = open("C:\\automation course\\words.txt", 'w')
# 'w' mean only creating a file and write to it

# 8
words.write('netzer')

# 9
words = open('C:\\automation course\\words.txt', 'r')
# open the file again as 'r' = reading
content = words.read()
print(content)

# 10
words = open("C:\\automation course\\words.txt", 'w')
words.write("שלום עולם")
words = open('C:\\automation course\\words.txt', 'r')
content = words.read()
print(content)
# every line that we want to operate a file we need to open it again for any type we need
# at line 31 in the file we will find the word 'netzer'
# after using again the open function with 'w' we are overwriting the file
# at the end we will writing at line 41 the word "שלום עולם"

words = open("C:\\automation course\\words.txt", 'a')
words.write(' ' + 'netzer again')
words = open('C:\\automation course\\words.txt', 'r')
content = words.read()
print(content)
# using 'a' we append the new text to the file

# challenge
# 11
import PIL.Image as image
import io
import base64
from byte_data import byte_data
# first byte_data is the python module and second byte_data is the variable that holding the image code
b = base64.b64decode(byte_data)
# print(b) is printing the code as b64decoding method
img = image.open(io.BytesIO(b))
img.show('b')
img.save("my lightning.png")
# save img to the pycharmproject folder
print(img.size)
print(img.height)
print(img.width)
print(img.format)
print(img.mode)

# more pillow from youtube by chorey schafer
from PIL import Image

# image1 = image.open("C:\\Users\\netze\\PycharmProjects\\py.class1\\DSC_5340.jpg")
# image1.save("C:\\Users\\netze\\PycharmProjects\\py.class1\\DSC_5340.png")
# open a image and convert it to png

# import os
# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i = image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.save('pngs\{}.png'.format(fn))

# working only when images located at the same folder as the python file (module)

