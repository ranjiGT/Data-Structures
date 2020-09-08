#Stack design using LIST
'''

l = [eval(x) for x in input("Enter elements onto stack: ").split(",")] 


print('Initial stack') 
print(l) 


print('Elements poped from stack:') 
print(l.pop()) 
print(l.pop()) 
print(l.pop()) 

print('Stack after elements are poped:') 
print(l) 

'''
#Stack design using DEQUE 

'''
from collections import deque 

stack = deque([eval(x) for x in input("Enter elements onto stack: ").split(",")]) 

print('Initial stack:') 
print(stack) 


print('Elements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print('Stack after elements are poped:') 
print(stack) 
'''


# Stack design using LIFOQUEUE

from queue import LifoQueue 

lifostack = LifoQueue(maxsize = 5) 
 
print(lifostack.qsize()) 

lifostack.put('sugar') 
lifostack.put('lemon drops') 
lifostack.put('water') 

print("Full: ", lifostack.full()) 
print("Size: ", lifostack.qsize()) 

print('Elements poped from the stack') 
print(lifostack.get()) 
print(lifostack.get()) 
print(lifostack.get()) 

print("Empty: ", lifostack.empty()) 


