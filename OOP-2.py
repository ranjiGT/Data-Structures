"""INSTANCE MEMORY"""


class PARENT:
    def __init__(self):
        self.a = 10
        self.b = 20

    def bar(self):
        self.c = 30
        print(self.c)


class CHILD(PARENT):
    def __init__(self):
        super().__init__()

    def foo(self):
        print(self.b)


obj = CHILD()
obj.foo()
obj.bar()
#obj.d=40

print(obj.__dict__)


"""STATIC MEMORY"""

'''class PARENT:
    x = 11

    def __init__(self):
        self.a = 10


class CHILD(PARENT):
    def __init__(self):
        super().__init__()

    @staticmethod
    def foo():
        print(CHILD.x)


CHILD.foo()'''
