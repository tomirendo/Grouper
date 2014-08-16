Grouper
=======

A python library for grouping objects together.

```python
import Grouper,datetime,random

#### You can use Grouper.groupby just like itertools.groupby:
print list([key,list(group)] for key,group in Grouper.groupby("abbbccd"))

ls = "aaabcdddef"
print list(Grouper.groupby(ls,as_iterable=False))#as_iterable = True returns each group as a list

#the "relation" keyword allows comparing consecutive values
print list(Grouper.groupby(ls,relation=lambda x,y:ord(y) - ord(x) <3,as_iterable=False))

#A cleaner way to find a relation is using Grouper.difference
print list(Grouper.groupby(ls,as_iterable= False, relation=Grouper.difference(3,key = ord))) 

#The "compare_to_first" keyword collect groups by their relation to the first object in the group 
print list(Grouper.groupby(ls,as_iterable= False, relation=Grouper.difference(3,key = ord),compare_to_first= True)) 

list_of_dates = sorted(datetime.datetime.now() + datetime.timedelta(minutes = random.randint(1,200000)) for i in range(10))

list(Grouper.groupby(list_of_dates,as_iterable=False,relation=Grouper.time_delta(days = 7)))
```