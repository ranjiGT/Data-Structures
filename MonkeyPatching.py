class Stub:
    def __init__(self,x):
        self.a = x

    def response(self):
        print('Success!')

    def addtocart(self):
        self.response()

    def checkout(self):
        self.response()


obj = Stub('url/token')

obj.addtocart()
obj.checkout()


'''
def patch_resp(self):
    print('$uCCe$$!')

Stub.response = patch_resp #Patched

#print("Just before Monkey Patching")

obj.addtocart()
obj.checkout()
'''
