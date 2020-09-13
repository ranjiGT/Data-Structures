class Drive:
    def __init__(self,n,s):
        self.name = n
        self.size = s

doc_list=[Drive('Python_Basics',20),
        Drive('Python_for_Data_Analysis',19),
              Drive('Python_Interview',23),
              Drive('Python_for_Data_Science',25),
              Drive('Python_Advanced',22)]

def storeData():
    import pickle
    f3=open('pick.obj','wb') #Write mode & binary
    for s in doc_list:
        pickle.dump(s,f3) #Dump all list elements from s pointed by f3
    f3.close() #closing the refridgertor

def viewData():
    import pickle
    f2=open('pick.obj','rb') #read mode & binary
    s_list=[]
    while True:
        try:
            s_list+=[pickle.load(f2)]
        except EOFError:
            break
    return s_list

storeData()
viewData()

