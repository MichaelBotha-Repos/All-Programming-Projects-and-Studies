class Fun:
    cnt = 0
    
    def __init__(self):
        print(Fun.cnt)

    def inc(self):
        Fun.cnt+=1
        print(Fun.cnt)


amy = Fun()
michael = Fun()
charmaine = Fun()
Johan = Fun()


for object in (amy, michael, charmaine, Johan):
    object.inc()    
