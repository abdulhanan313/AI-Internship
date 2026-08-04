def meraForLoop(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break
        
a = [1,2,3]
b= range(1,11)
c= (1,2,3)
d = {1,2,3}
e = {0:1,1:2}

meraForLoop(a)
meraForLoop(b)
meraForLoop(c)
meraForLoop(d)
meraForLoop(e)
        
 
 