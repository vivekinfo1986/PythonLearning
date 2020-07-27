Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {"Key1":100, "Key2":200}
>>> d
{'Key1': 100, 'Key2': 200}
>>> d["Key2"] = 300
>>> d
{'Key1': 100, 'Key2': 300}
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d
{'Key1': 100, 'Key2': 300}
>>> d.keys()
dict_keys(['Key1', 'Key2'])
>>> d
{'Key1': 100, 'Key2': 300}
>>> d.values()
dict_values([100, 300])
>>> d
{'Key1': 100, 'Key2': 300}
>>> d.items()
dict_items([('Key1', 100), ('Key2', 300)])
>>> t = (1,2,3)
>>> t
(1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> t
(1, 2, 3)
>>> len(t)
3
>>> t = ("First",2,"Hello",272.474)
>>> t
('First', 2, 'Hello', 272.474)
>>> t[1]
2
>>> t[-1]
272.474
>>> t = ('a','b','c','a')
>>> t
('a', 'b', 'c', 'a')
>>> t.count('a')
2
>>> t.index('c')
2
>>> t = ('a','b','c','a')
>>> t
('a', 'b', 'c', 'a')
>>> t[0] = "New Value"
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t[0] = "New Value"
TypeError: 'tuple' object does not support item assignment
>>> myset = set()
>>> myset
set()
>>> myset.add(1)
>>> myset
{1}
>>> myset.add(2)
>>> myset
{1, 2}
>>> myset.add(2)
>>> myset
{1, 2}
>>> mylist = [1,1,1,1,1,,2,2,2,2,3,3,3,3]
SyntaxError: invalid syntax
>>> mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
>>> mylist
[1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
>>> set(mylist)
{1, 2, 3}
>>> True
True
>>> False
False
>>> true
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 1 ==2
False
>>> 1<2
True
>>> b
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> b = None
>>> b
>>> 