def difference(max_difference,min_difference = None, attr = None, key = None):
    if attr:
        _key_func = attrgetter(attr)
    else :
        if key:
            _key_func = key
        else :
            _key_func = lambda x:x
    if min_difference:       
        def _relation(a,b):
            return min_difference <= _key_func(b) - _key_func(a) <= max_difference
    else :
        def _relation(a,b):
            return _key_func(b) - _key_func(a) <= max_difference
    return _relation

def time_delta(*args,**kwargs):
    
    from datetime import timedelta
    if kwargs.has_key("attr"):
        _attr = kwargs.pop("attr")
        _key_func = attrgetter(_attr)
    else :
        _key_func = kwargs.pop("key",lambda x:x)

    _delta = timedelta(*args,**kwargs)

    return difference(_delta,key = _key_func)

def attrgetter(*args,**kwargs):
    import operator
    return operator.attrgetter(*args,**kwargs)

def itemgetter(*args,**kwargs):
    import operator
    return operator.itemgetter(*args,**kwargs)

def methodcaller(*args,**kwargs):
    import operator
    return operator.methodcaller(*args,**kwargs)


def AND(*functions):
    def relation_function(a,b):
        for func in functions:
            if not func(a,b):
                return False
        return True
    return relation_function

def OR(*functions):
    def relation_function(a,b):
        for func in functions:
            if func(a,b):
                return True
        return False
    return relation_function






