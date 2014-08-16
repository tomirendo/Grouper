def time_delta(*args,**kwargs):
    
    from datetime import timedelta

    _key_func = kwargs.get("key",lambda x:x)
    _abs = kwargs.get("abs",False)
    
    del kwargs['abs']
    del kwargs['key']

    _delta = timedelta(*args,**kwargs)
    if _abs:
        def _time_delta_relation(a,b):
            return abs(_key_func(b) - _key_func(a)) <= _delta
        return _time_delta_relation
    else :
        def _time_delta_relation(a,b):
            return _key_func(b) - _key_func(a) <= _delta
        return _time_delta_relation
