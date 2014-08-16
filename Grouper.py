class groupby(object):
    def __init__(self, iterable, key=None,relation = None,compare_to_first = False,as_iterable = True):
        self.it = iter(iterable)
        self.as_iterable = as_iterable
        if relation is None:
            if key is None:
                key = lambda x: x
            self.keyfunc = key
            self.relation_function = None
            self.tgtkey = self.currkey = self.currvalue = object()
        else :
            self.relation_function = relation
            self.prevvalue = None
            self.curvalue = next(self.it)
            self.it_ended = False
            self.cmp_to_first = compare_to_first
            
    def __iter__(self):
        return self
    
    def next(self):
        if self.relation_function is None:
            while self.currkey == self.tgtkey:
                self.currvalue = next(self.it)    # Exit on StopIteration
                self.currkey = self.keyfunc(self.currvalue)
            self.tgtkey = self.currkey
            if self.as_iterable:
                return (self.currkey, self._grouper(self.tgtkey))
            else :
                return (self.currkey, list(self._grouper(self.tgtkey)))
        else :
            if not self.it_ended:
                if self.as_iterable:
                    return self._relation_grouper()
                else :
                    return list(self._relation_grouper())
            else :
                raise StopIteration()
        
    def _grouper(self, tgtkey):
        while self.currkey == tgtkey:
            yield self.currvalue
            self.currvalue = next(self.it)    # Exit on StopIteration
            self.currkey = self.keyfunc(self.currvalue)

    def _relation_grouper(self):
        yield self.curvalue
        self.prevvalue = self.curvalue
        self.currvalue = next(self.it)
        while self.relation_function(self.prevvalue,self.curvalue):
            yield self.curvalue
            if self.cmp_to_first is False:
                self.prevvalue = self.curvalue
            try :
                self.curvalue = next(self.it)
            except StopIteration:
                self.it_ended = True
                raise StopIteration()
        
        