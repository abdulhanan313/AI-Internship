class Mera_range:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return mera_range_iterator(self)
        
class mera_range_iterator:
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
            current = self.iterable.start
            self.iterable.start+=1
            
x = Mera_range(1,11)
type(x)