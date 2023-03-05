class Fruit():
    def __init__(self,fruit):
        print("Fruit type: ",fruit)
class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print("Apple is sweet")

apple=FruitFlavour()

'''class A:
    a=1
class B(A):
    b=2
class C(B):
    pass
c=C()
print(c.a,c.b)
print(issubclass(A,B))
print(issubclass(B,A))
print(isinstance(c,B))'''