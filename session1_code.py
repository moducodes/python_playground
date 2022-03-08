Python 3.8.5 (default, Jan 27 2021, 15:41:15)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 3
>>> a = "bala"
>>> a = 3
>>> type(a)
<class 'int'>
>>> a = "bala"
>>> type(a)
<class 'str'>
>>> a = 3
>>> type(a)
<class 'int'>
>>> a = "3"
>>> str(a)
'3'
>>> type(a)
<class 'str'>
>>> a = 99
>>> b = 1/10
>>> type(a)
<class 'int'>
>>> a
99
>>> b
0.1
>>> b = a/10
>>> b
9.9
>>> type(b)
<class 'float'>
>>> c = 9.9
>>> c = 1.1
>>> d = 4
>>> type(c)
<class 'float'>
>>> type(d)
<class 'int'>
>>> e = c + d
>>> e
5.1
>>> type(e)
<class 'float'>
>>> a = "3"
>>> type(a)
<class 'str'>
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> a = "a"
>>> b = int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'a'
>>> a_list = [1, 2, 3, 4, 5]
>>> type(a_list)
<class 'list'>
>>> a_list.append(6)
>>> a_list
[1, 2, 3, 4, 5, 6]
>>> a_list.length()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'list' object has no attribute 'length'
>>> len
<built-in function len>
>>> len(a_list)
6
>>> a = 3
>>> len(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> len(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
>>> a_list.append("bala")
>>> a_list
[1, 2, 3, 4, 5, 6, 'bala']
>>> b_list = [1, 4, 5, 7, "vedant"]
>>> a_list.extend(b_list)
>>> a_list
[1, 2, 3, 4, 5, 6, 'bala', 1, 4, 5, 7, 'vedant']
>>> a_list[0]
1
>>> a_list[7]
1
>>> a_list[8]
4
>>> a_tuple = (1, 2, 3,)
>>> type(a_tuple)
<class 'tuple'>
>>> a_tuple.append(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
>>> a_tuple[0]
1
>>> a_tuple[2]
3
>>> a_dict = {"name": "bala"}
>>> a_dict = {1: "bala"}
>>> a_dict
{1: 'bala'}
>>> a_dict = {1: "bala", 4: "vedant"}
>>> a_dict
{1: 'bala', 4: 'vedant'}
>>> a_dict = {1: "bala", 4: "vedant", "day": "wednesday"}
>>> a_dict[4]
'vedant'
>>> a_dict
{1: 'bala', 4: 'vedant', 'day': 'wednesday'}
>>> a_dict
{1: 'bala', 4: 'vedant', 'day': 'wednesday'}
>>>
>>> a_dict["day"]
'wednesday'
>>> a.get("day")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'get'
>>> a_dict.get("day")
'wednesday'
>>> a_dict["date"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'date'
>>> a_dict.get("date")
>>> b = a_dict.get("date")
>>> b
>>> if b == None:
...     print("whatever")
...
whatever
>>> b = a_dict.get("date", "2 march")
>>> a_dict.get("date", "2 march")
'2 march'
>>> a_dict
{1: 'bala', 4: 'vedant', 'day': 'wednesday'}
>>> a_dict.get("date", "3 march")
'3 march'
>>> a_dict = {1: "bala", 4: "vedant", "day": "wednesday"}
>>> a_dict["session"] = 1
>>> a_dict
{1: 'bala', 4: 'vedant', 'day': 'wednesday', 'session': 1}
>>> a_tuple
(1, 2, 3)
>>> len(a_tuple)
3
>>> len(a_dict)
4
>>> a_set = set([1, 2, 3, 4])
>>> a_set
{1, 2, 3, 4}
>>> a_set = set([1, 2, 3, 4, 1, 2,])
>>> a_set
{1, 2, 3, 4}
>>> a_set = set([1, 2, 3, 4, 1, 2, 5,])
>>> a_set
{1, 2, 3, 4, 5}
>>> a_set.add(6)
>>> a_set
{1, 2, 3, 4, 5, 6}
>>> a_set.add(5)
>>> a_set
{1, 2, 3, 4, 5, 6}
>>> a_set.add("bala")
>>> a_set
{1, 2, 3, 4, 5, 6, 'bala'}
>>> a_set.add(a_dict)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
>>> a_set.add(a_list)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> b_set = {4, 5, 6, 1}
>>> type(b_set)
<class 'set'>
>>> a_set.add(b_set)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> a_set.add(a_tuple)
>>> a_set
{1, 2, 3, 4, 5, 6, (1, 2, 3), 'bala'}
>>> b_set = {4, 5, 6, 10, 11, 12, 13, 15}
>>> a_set.union(b_set)
{1, 2, 3, 4, 5, 6, 10, (1, 2, 3), 11, 12, 13, 15, 'bala'}
>>> a_set | b_set
{1, 2, 3, 4, 5, 6, 10, (1, 2, 3), 11, 12, 13, 15, 'bala'}
>>> a_set.intersection(b_set)
{4, 5, 6}
>>> a_set & b_set
{4, 5, 6}
>>> a_set
{1, 2, 3, 4, 5, 6, (1, 2, 3), 'bala'}
>>> c_set = a_set & b_set
>>> c_set
{4, 5, 6}
>>>