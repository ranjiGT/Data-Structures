'''
class Demo:
    def __init__(self,v):
        self._tu = v
        self.__tum = 20 #hidden 


obj = Demo(10)
print(obj._tu)
#print(obj.__tum)

#We can print hidden variables
print(obj._Demo__tum) #Fully qualified name (FQN)
'''


'''
class SEQ:
    _x = 949 #static member
    __h = 666 #static. hidden

    def __init__(self):
        self.__a = 100 #private Instance Variable

    @staticmethod
    def bar():
        print(obj._SEQ__h)#1 ; FQN
        print(SEQ.__h)#2
        print(obj.__h)#3

obj = SEQ()
obj.bar()

print(obj._x)
print(obj.__dict__) #Name Mangling
'''
