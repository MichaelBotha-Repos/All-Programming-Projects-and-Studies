class A:
    def __init__(self):
        self.vara = 1

class B:
    def __init__(self):
        self.varb = 2

class C(A, B):
    def   __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.varc = 3

test = C()
print(test.vara, test.varb, test.varc)