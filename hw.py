import string
import time
text = 'Hello world'
temp = ''

for ch in text:
    for i in string.printable:
        if i == ch or i == '':
            time.sleep(0.02)
            print(temp + i)
            temp += ch 
            break
        else:
            time.sleep(0.02)
            print(temp + i)
