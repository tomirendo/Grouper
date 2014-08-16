def difference(difference, attr = None, key = None):
    if attr:
        _key_func = lambda x:getattr(x,attr)
    else :
        if key:
            _key_func = key
        else :
            _key_func = lambda x:x

    def _relation(a,b):
        return _key_func(b) - _key_func(a) < difference
    return _relation

def time_delta(*args,**kwargs):
    
    from datetime import timedelta
    if kwargs.has_key("attr"):
        _key_func = lambda x:getattr(x,kwargs.pop("attr"))
    else :
        _key_func = kwargs.pop("key",lambda x:x)

    _delta = timedelta(*args,**kwargs)

    return difference(_delta,key = _key_func)
