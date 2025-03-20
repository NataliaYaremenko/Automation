#count
string = 'Hello World'
a - 'l '
print(string.count(a, 0, 5))
if string.count(a)
    print ('Hi')

#string replace
string = 'Hello World'
print(string.replace('l', ' del', 20))

#strip - прибираэ елементи
string = '!  Hello Worl!d'
print(string.strip('!'))

#.join - join
lst = ['Hello', 'World', 'World']
print(' '.join(lst))

#
print('999'.isdigit())

#import re
import re
result = re.match(r"\d+", "123abc")
print(result)