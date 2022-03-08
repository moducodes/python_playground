Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> if a == 1:
...     print("Yay")
...
Yay
>>> if a == 2:
...     print("a is 2")
... elif a == 1:
...     print("a is 1")
...
a is 1
>>> if a == 2:
...     print("a is 2")
... elif a == 0:
...     print("a is 0")
... else:
...     print("a is neither 2 nor 0")
...
a is neither 2 nor 0
>>> if a < 0 or a > -1:
...     print("a is within range")
...
a is within range
>>> if a <= 2 and a >= -1:
...     print("a is within range")
...
a is within range
>>> a + 2
3
>>> a + 2
3
>>> a <= 2
True
>>> if a + 2:
...     print("This is a truthy expression")
...
This is a truthy expression
>>> if a + 1 + 1:
...     print("Same thing")
...
Same thing
>>> if a - 1:
...     print("This is truthy.")
...
>>> if a - 2:
...     print("This is truthy.")
...
This is truthy.
>>> if a - 1:
...     print("This is truthy.")
... else:
...     print("This is falsy.")
...
This is falsy.
>>> a_str = "Bala"
>>> if a_str:
...     print("This is truthy.")
...
This is truthy.
>>> e_str = ""
>>> if e_str:
...     print("This is truthy.")
... else:
...     print("This is falsy.")
...
This is falsy.
>>> len(a_str)
4
>>> a_list = [1,2,3]
>>> if a_list:
...     print("This is truthy.")
...
This is truthy.
>>> e_list = []
>>> if e_list:
...     print("This is truthy")
... else:
...     print("This is falsy.")
...
This is falsy.
>>>
>>>
>>> a_list = [3, 4, 5, 1, 10, 17, 42, 73]
>>> for i in a_list:
...     print(i)
...
3
4
5
1
10
17
42
73
>>> a_list[2]
5
>>> a_list[2:4]
[5, 1]
>>> for i in a_list[2:5]:
...     print(i)
...
5
1
10
>>> type(a_list[2:5])
<class 'list'>
>>> len(a_list[2:5])
3
>>> spliced_list = a_list[3:6]
>>> spliced_list
[1, 10, 17]
>>> a_list[0:5]
[3, 4, 5, 1, 10]
>>> a_list[:5]
[3, 4, 5, 1, 10]
>>> a_list[5:len(a_list)]
[17, 42, 73]
>>> a_list[5:]
[17, 42, 73]
>>> a_list[5::2]
[17, 73]
>>> a_list[5::1]
[17, 42, 73]
>>> a_list[5:]
[17, 42, 73]
>>> a_list[2::1]
[5, 1, 10, 17, 42, 73]
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73]
>>> a_list[2:]
[5, 1, 10, 17, 42, 73]
>>> a_list[2:7]
[5, 1, 10, 17, 42]
>>> a_list[2:7:2]
[5, 10, 42]
>>> a_list[2:7:1]
[5, 1, 10, 17, 42]
>>> a_list[5::-1]
[17, 10, 1, 5, 4, 3]
>>> a_list[::-1]
[73, 42, 17, 10, 1, 5, 4, 3]
>>> a_list[5:2]
[]
>>> a_list[5:2:1]
[]
>>> a_list[5:2:-1]
[17, 10, 1]
>>>
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73]
>>> b_list = []
>>>
>>> for i in a_list:
...     b_list.append(i*2)
...
>>> b_list
[6, 8, 10, 2, 20, 34, 84, 146]
>>>
>>> for i in a_list:
...
... for i in a_list:
  File "<stdin>", line 3
    for i in a_list:
    ^
IndentationError: expected an indented block
>>> for i in a_list:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
>>>
>>> a_list.index(17)
5
>>> for i in a_list:
...     idx = a_list.index(i)
...
>>> b_list
[6, 8, 10, 2, 20, 34, 84, 146]
>>> b_list.clear()
>>> b_list
[]
>>> for i in a_list:
...     idx = a_list.index(i)
...     b_list.append(i+idx)
...
>>> b_list
[3, 5, 7, 4, 14, 22, 48, 80]
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73]
>>> a_list.append(17)
>>> a_list.append(5)
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73, 17, 5]
>>> b_list.clear()
>>>
>>> for i in a_list:
...     idx = a_list.index(i)
...     b_list.append(i+idx)
...
>>> b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>>
>>>
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73, 17, 5]
>>> b_list
[3, 5, 7, 4, 14, 22, 48, 80, 22, 7]
>>>
>>> a_list[8]
17
>>> a_list[5]
17
>>> a_list.append(67)
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73, 17, 5, 67]
>>> b_list.clear()
>>> for i in a_list:
...     idx = a_list.index(i)
...     b_list.append(i+idx)
...
>>>
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73, 17, 5, 67]
>>> b_ist
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b_ist' is not defined
>>> b_list
[3, 5, 7, 4, 14, 22, 48, 80, 22, 7, 77]
>>>
>>>
>>> range(4)
range(0, 4)
>>> rng = range(4)
>>> type(rng)
<class 'range'>
>>> list(rng)
[0, 1, 2, 3]
>>>
>>> for i in range(4)"
  File "<stdin>", line 1
    for i in range(4)"
                     ^
SyntaxError: EOL while scanning string literal
>>> for i in range(4):
...     print(i)
...
0
1
2
3
>>>
>>> for i in range(len(a_list)):
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block
>>>
>>> b_list.clear()
>>> for i in range(len(a_list)):
...     b_list.append(a_list[i] + i)
...
>>>
>>> a_list
[3, 4, 5, 1, 10, 17, 42, 73, 17, 5, 67]
>>> b_list
[3, 5, 7, 4, 14, 22, 48, 80, 25, 14, 77]
>>>
>>>
>>> y_list = [1, 2, 3]
>>> z_list = [11, 12, 13]
>>> x_list = []
>>>
>>> for i in range(len(y_list)):
...     x_list.append(y_list[i] + z_list[i])
...
>>> x_list
[12, 14, 16]
>>>
>>> for i in range(2,5):
...     print(i)
...
2
3
4
>>> for i in range(2,10):
...     print(i)
...
2
3
4
5
6
7
8
9
>>> for i in range(2,10,3):
...     print(i)
...
2
5
8
>>> for i in range(12,5,-4):
...     print(i)
...
12
8
>>>
>>> for i in range(12,5,-4):
...     print(i)
... else:
...     print("loop ends")
...
12
8
loop ends
>>>
>>> for i in range(12,5,-4):
...     print(i)
... print("loop ends")
  File "<stdin>", line 3
    print("loop ends")
    ^
SyntaxError: invalid syntax
>>>
>>>
>>> bool_list = []
>>> bool_list.append(True)
>>> bool_list = []
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list
[True, True, True, True, True, True, True, True, True]
>>> bool_list.append(False)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list.append(True)
>>> bool_list
[True, True, True, True, True, True, True, True, True, False, True, True, True, True, True]
>>>
>>> for i in bool_list:
...     if i == True:
...             print("Still true")
...     else:
...             break
...
Still true
Still true
Still true
Still true
Still true
Still true
Still true
Still true
Still true
>>> i = 0
>>> while bool_list[i]"
  File "<stdin>", line 1
    while bool_list[i]"
                      ^
SyntaxError: EOL while scanning string literal
>>> while bool_list[i]:
...     print("Still true")
...     i += 1
...
Still true
Still true
Still true
Still true
Still true
Still true
Still true
Still true
Still true
>>> if bool_list:
...     print("Truthy")
...
Truthy