Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>>
>>> dict_a = {}
>>> dict_a["a"] = 1
>>> dict_a["b"] = 2
>>> dict_a["d"] = 4
>>> dict_a["f"] = 6
>>> dict_a["a"]
1
>>> dict_a.get("a")
1
>>> dict_a["c"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'c'
>>> dict_a.get("c")
>>> dict_a.get("c", 3)
3
>>> dict_b = {"y": 345}
>>> dict_b
{'y': 345}
>>> dict_b.clear()
>>> dict_b
{}
>>> dict_b = dict_a.copy()
>>> dict_b
{'a': 1, 'b': 2, 'd': 4, 'f': 6}
>>> dict_b["z"] = 26
>>> dict_b
{'a': 1, 'b': 2, 'd': 4, 'f': 6, 'z': 26}
>>> dict_a
{'a': 1, 'b': 2, 'd': 4, 'f': 6}
>>> dict_c = dict_a
>>> dict_c
{'a': 1, 'b': 2, 'd': 4, 'f': 6}
>>> dict_a
{'a': 1, 'b': 2, 'd': 4, 'f': 6}
>>> dict_c["y"] = 25
>>> dict_c
{'a': 1, 'b': 2, 'd': 4, 'f': 6, 'y': 25}
>>> dict_a
{'a': 1, 'b': 2, 'd': 4, 'f': 6, 'y': 25}
>>> a = 5
>>> b = a
>>> a
5
>>> b
5
>>> b = b + 7
>>> b
12
>>> a
5
>>>
>>> list_a = [1,2,3,4]
>>> list_b = list_a.copy()
>>> list_b
[1, 2, 3, 4]
>>> list_b.append(5)
>>> list_b
[1, 2, 3, 4, 5]
>>> list_a
[1, 2, 3, 4]
>>> list_c = list_a
>>> list_C
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'list_C' is not defined
>>> list_c
[1, 2, 3, 4]
>>> list_a
[1, 2, 3, 4]
>>> list_c.append(5)
>>> list_c
[1, 2, 3, 4, 5]
>>> list_a
[1, 2, 3, 4, 5]
>>> dict_a
{'a': 1, 'b': 2, 'd': 4, 'f': 6, 'y': 25}
>>> dict_a.items()
dict_items([('a', 1), ('b', 2), ('d', 4), ('f', 6), ('y', 25)])
>>> type(dict_a.items())
<class 'dict_items'>
>>> for k, v in dict_a.items():
...     print(k, v)
...
a 1
b 2
d 4
f 6
y 25
>>> for item in dict_a.items():
...     print(item)
...
('a', 1)
('b', 2)
('d', 4)
('f', 6)
('y', 25)
>>> for item in dict_a.items():
...     print(item)
...     print(type(item))
...
('a', 1)
<class 'tuple'>
('b', 2)
<class 'tuple'>
('d', 4)
<class 'tuple'>
('f', 6)
<class 'tuple'>
('y', 25)
<class 'tuple'>
>>> for (k, v) for dict_a.items():
  File "<stdin>", line 1
    for (k, v) for dict_a.items():
               ^
SyntaxError: invalid syntax
>>> for (k, v) in dict_a.items():
...     print(k)
...
a
b
d
f
y
>>> for k for dict_a.keys():
  File "<stdin>", line 1
    for k for dict_a.keys():
          ^
SyntaxError: invalid syntax
>>> for k in dict_a.keys():
...     print(k)
...
a
b
d
f
y
>>> for k in dict_a.values():
...     print(k)
...
1
2
4
6
25
>>> dict_a
{'a': 1, 'b': 2, 'd': 4, 'f': 6, 'y': 25}
>>> del dict_a["b"]
>>> dict_a
{'a': 1, 'd': 4, 'f': 6, 'y': 25}
>>> f_value = dict_a.pop("f")
>>> dict_a
{'a': 1, 'd': 4, 'y': 25}
>>> f_value
6
>>> dict_a.pop("y")
25
>>> dict_a
{'a': 1, 'd': 4}
>>> dict_a.popitem()
('d', 4)
>>> dict_a["b"] = 2
>>> dict_a
{'a': 1, 'b': 2}
>>> dict_a["e"] = 5
>>> dict_a["d"] = 4
>>> dict_a
{'a': 1, 'b': 2, 'e': 5, 'd': 4}
>>> dict_a.setdefault("a", 7)
1
>>> dict_a.setdefault("z", 26)
26
>>> dict_a
{'a': 1, 'b': 2, 'e': 5, 'd': 4, 'z': 26}
>>>
>>> list_a
[1, 2, 3, 4, 5]
>>> list_a.append(3)
>>> list_a.append(3)
>>> list_a.append(3)
>>> list_a.append(7
... )
>>> list_a.append(7)
>>> list_a.append(5)
>>> list_a
[1, 2, 3, 4, 5, 3, 3, 3, 7, 7, 5]
>>> len(list_a)
11
>>> list_a.count(7)
2
>>> list_a.count()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: count() takes exactly one argument (0 given)
>>> list_a.count(3)
4
>>> list_b = [11, 13, 11]
>>> list_a.extend(list_b)
>>> list_a
[1, 2, 3, 4, 5, 3, 3, 3, 7, 7, 5, 11, 13, 11]
>>> list_a
[1, 2, 3, 4, 5, 3, 3, 3, 7, 7, 5, 11, 13, 11]
>>> list_a.index(3)
2
>>> list_a.insert(8, 19)
>>> list_a
[1, 2, 3, 4, 5, 3, 3, 3, 19, 7, 7, 5, 11, 13, 11]
>>> list_a.pop(3)
4
>>> list_a
[1, 2, 3, 5, 3, 3, 3, 19, 7, 7, 5, 11, 13, 11]
>>> list_a.remove(3)
>>> list_a
[1, 2, 5, 3, 3, 3, 19, 7, 7, 5, 11, 13, 11]
>>> for a in list_a:
...     print(a)
...
1
2
5
3
3
3
19
7
7
5
11
13
11
>>> if 3 in list_a:
...     print("3 is present")
...
3 is present
>>> 3 in list_a
True
>>> list_a.reverse()
>>> list_a
[11, 13, 11, 5, 7, 7, 19, 3, 3, 3, 5, 2, 1]
>>> list_a[1:4]
[13, 11, 5]
>>> list_a[1:4:-1]
[]
>>> list_a[1:4]
[13, 11, 5]
>>> list_a[1:4:-1]
[]
>>> list_a[1:4:1]
[13, 11, 5]
>>> list_a[::-1]
[1, 2, 5, 3, 3, 3, 19, 7, 7, 5, 11, 13, 11]
>>> list_a[1:4:-1]
[]
>>> list_a[4:1:-1]
[7, 5, 11]
>>> list_a
[11, 13, 11, 5, 7, 7, 19, 3, 3, 3, 5, 2, 1]
>>> list_a.sort()
>>> list_a
[1, 2, 3, 3, 3, 5, 5, 7, 7, 11, 11, 13, 19]
>>> list_a
[1, 2, 3, 3, 3, 5, 5, 7, 7, 11, 11, 13, 19]
>>> list_a[4:1:-1]
[3, 3, 3]
>>> list_b = [4,6,2,8,1,4]
>>> list_b
[4, 6, 2, 8, 1, 4]
>>> sorted(list_b)
[1, 2, 4, 4, 6, 8]
>>> list_b
[4, 6, 2, 8, 1, 4]
>>> list_c = sorted(list_b)
>>> list_c
[1, 2, 4, 4, 6, 8]
>>> list_b
[4, 6, 2, 8, 1, 4]
>>> list_b.sort()
>>> list_b
[1, 2, 4, 4, 6, 8]
>>>
>>> def hello_world():
...     print("Hello")
...
>>> hello_world
<function hello_world at 0x7f4b4641e310>
>>> hello_world()
Hello
>>> def hello_user(name):
...     print("Hello " + user)
...
>>> hello_user("Bala")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in hello_user
NameError: name 'user' is not defined
>>> def hello_user(name):
...     print("Hello " + name)
...
>>> hello_user("Bala")
Hello Bala
>>> print(f"Hello {name}")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>> name = "Bala"
>>> print(f"Hello {name}")
Hello Bala
>>>
>>> def hello_user(name):
...     print(f"Hello {name}")
...
>>> hello_user("Bala")
Hello Bala
>>> name
'Bala'
>>>
>>> def sum(n1, n2, n3):
...     return n1 + n2 + n3
...
>>> sum(1, 2, 3)
6
>>> sum_n = sum(1, 2, 3)
>>> sum_n
6
>>> sum(4, 5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() missing 1 required positional argument: 'n3'
>>> def sum(n1=0, n2=0, n3=0):
...     return n1+n2+n3
...
>>> sum(4, 5)
9
>>> sum(4, 5, 6, 8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() takes from 0 to 3 positional arguments but 4 were given
>>> def sum(n_list):
...     sum_n = 0
...     for n in n_list:
...             sum_n += n
...     return sum_n
...
>>> sum([1,2,3,5,6,7,8,9])
41
>>> sum(1,2,3,5,6,7,8,9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() takes 1 positional argument but 8 were given
>>> def sum(*n_list):
...     n_sum = 0
...     for n in n_list:
...             n_sum += n
...     return n_sum
...
>>> sum(1,2,3,5,6,7,8,3,2,12)
49
>>> def sum(*n_list):
...     n_sum = 0
...     for n in n_list:
...             n_sum += n
...     return n_sum, len(n_list)
...
>>> sum(1,2,3,5,6,7,8,3,2,12)
(49, 10)
>>> sum_n = sum(1,2,3,5,6,7,8,3,2,12)
>>> type(sum_n)
<class 'tuple'>
>>> sum_n, count = sum(1,2,3,5,6,7,8,3,2,12)
>>> sum_n
49
>>> count
10
>>> sum_n, count, random = sum(1,2,3,5,6,7,8,3,2,12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
>>>
>>>
>>> tuple_a = (1, 2, 4, 6)
>>> a1, a2, a3, a4 = tuple_a
>>> a1
1
>>> a2
2
>>> def sum(*n_list, name):
...     n_sum = 0
...     for n in n_list:
...             n_sum += n
...     print(f"Passed name is {name}")
...     return n_sum, len(n_list)
...
>>> sum(1,2,3,5,6,7,8,3,2,12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() missing 1 required keyword-only argument: 'name'
>>> sum(1,2,3,5,6,7,8,3,2,12, name="Vedant")
Passed name is Vedant
(49, 10)
>>> sum(1,2,3,5,6,7,8,3,2,12,"Vedant")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sum() missing 1 required keyword-only argument: 'name'
>>> def sum(*n_list):
...
KeyboardInterrupt
>>> def sum(a, b, c, *n_list):
...     n_sum = 0
...     for n in n_list:
...             n_sum += n
...     return n_sum, len(n_list)
...
>>> sum(1,2,3,5,6,7,8,3,2,12)
(43, 7)
>>> sum(1,2,3,5,6,7,8,3,2,12,"Vedant")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in sum
TypeError: unsupported operand type(s) for +=: 'int' and 'str'
