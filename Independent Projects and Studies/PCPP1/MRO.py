class A:
    var = 4

class B(A):
    var2 = 7

class C(A):
    var = 9

class D(B,A):
    pass

test = D()

print(test.var)
