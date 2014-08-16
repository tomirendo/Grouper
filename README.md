Grouper
=======

A python library for grouping objects together.


You can use Grouper.groupby just like itertools.groupby:
```python
list([key,list(group)] for key,group in Grouper.groupby("abbbccd"))
#[['a', ['a']], ['b', ['b', 'b', 'b']], ['c', ['c', 'c']], ['d', ['d']]]
```
'as_iterable = True' returns each group as a list
```python
ls = "aaabcdddef"
print list(Grouper.groupby(ls,as_iterable=False))
#[('a', ['a', 'a', 'a']), ('b', ['b']), ('c', ['c']), 
#                ('d', ['d', 'd', 'd']), ('e', ['e']), ('f', ['f'])]
```

The "relation" keyword allows comparing consecutive values
```python
Grouper.groupby(ls,relation=lambda x,y:ord(y) - ord(x) <3,as_iterable=False)
#[['a', 'a', 'a', 'b', 'c', 'd', 'd', 'd', 'e', 'f', 'g'], ['j', 'k', 'l', 'm']]
```

A cleaner way to find a relation is using Grouper.difference
```python
Grouper.groupby(ls,as_iterable= False, relation=Grouper.difference(3,key = ord))
#[['a', 'a', 'a', 'b', 'c', 'd', 'd', 'd', 'e', 'f', 'g'], ['j', 'k', 'l', 'm']]
```

The "compare_to_first" keyword collect groups by their relation to the first object in the group 
```python
Grouper.groupby(ls,as_iterable= False, 
                relation=Grouper.difference(3,key = ord),compare_to_first= True)
#[['a', 'a', 'a', 'b', 'c'], ['d', 'd', 'd', 'e', 'f'], ['g'], ['j', 'k', 'l'], ['m']]
```

Grouper is great in creating groups of close dates.
You can use the Grouper.time_delta function to group dates together
```python
#Create a list of random dates
list_of_dates = sorted(datetime.datetime.now() + \
            datetime.timedelta(minutes = random.randint(1,200000)) for i in range(10))

list(Grouper.groupby(list_of_dates,
                    as_iterable=False,relation=Grouper.time_delta(days = 7)))
#[[datetime.datetime(2014, 8, 28, 7, 42, 6, 903210)],
# [datetime.datetime(2014, 9, 13, 14, 31, 6, 903233),
#  datetime.datetime(2014, 9, 16, 0, 23, 6, 903246)],
# [datetime.datetime(2014, 10, 6, 20, 0, 6, 903220),
#  datetime.datetime(2014, 10, 7, 0, 9, 6, 903252),
#  datetime.datetime(2014, 10, 8, 14, 10, 6, 903238)],
# [datetime.datetime(2014, 11, 26, 5, 16, 6, 903263)],
# [datetime.datetime(2014, 12, 6, 8, 51, 6, 903189),
#  datetime.datetime(2014, 12, 7, 10, 10, 6, 903257),
#  datetime.datetime(2014, 12, 12, 13, 21, 6, 903227)]]
```
