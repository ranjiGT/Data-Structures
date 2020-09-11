#Demonstrating manual Garbage Collection

import gc

i = 0 
  
def refcycle(): 
    x = { } 
    x[i] = x 
    print(x) 
  

collected = gc.collect()
print( "Garbage collector: collected %d objects." % (collected)) 
#***************************************************************** 
print( "Creating cycles...")
for i in range(20): 
    refcycle() 
  
collected = gc.collect() 
  
print( "Garbage collector: collected %d objects." % (collected))



