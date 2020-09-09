'''
class PARENT:
   
    def __init__(self):
        self.a=10
        
    def basefunc(self):
        print("Base Instance Function a =",self.a)

class CHILD(PARENT):
    def __init__(self):
        super().__init__()
        
        
    def f1(self):
        super().basefunc()
        self.basefunc()

obj=CHILD()
obj.f1()
'''
'''
class PARENT:
    x=11
    x=12#static var; returns latest value
    def __init__(self):
        self.a=10

    @staticmethod
    def basefunc():
        print("Base Static Function x =",CHILD.x)

class CHILD(PARENT):
    def __init__(self):
        super().__init__()
        
    @staticmethod   
    def f1():
        CHILD.basefunc()
        #self.basefunc()

obj=CHILD()
obj.f1()
'''


class PERSON:
    def __init__(self,n,a):
        self.name = n
        self.age = a
        
class STUDENT(PERSON):              #HI
    def __init__(self,n,a,r,d):
        self.rollno = r
        self.defaulter = d
        PERSON.__init__(self,n,a)
        
class TEACHER(PERSON):              #HI
    def __init__(self,n,a,c):
        self.course = c
        PERSON.__init__(self,n,a)

class BRIGHTSTUDENT(STUDENT,TEACHER): #MI
    def __init__(self,n,a,r,d,c,p):
        self.points = p
        STUDENT.__init__(self,n,a,r,d)
        TEACHER.__init__(self,n,a,c)



obj=BRIGHTSTUDENT("Rajeev",19,100,"No","Chemistry",7)
print(obj.__dict__)
