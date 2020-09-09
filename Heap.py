from heapq import heappop, heappush, heapify 
   
oranges = [] 
heapify(oranges) 

heappush(oranges, -1 * 10) 
heappush(oranges, -1 * 30) 
heappush(oranges, -1 * 20) 
heappush(oranges, -1 * 160) 

print("Topmost element of heap : ",(-1 * oranges[0])) 
  
print("The heap elements : ") 
for i in oranges: 
    print(-1 * i, end = ' ') 
print("\n") 
  
top = heappop(oranges) 
  
print("The heap elements : ") 
for i in oranges: 
    print(-1 * i, end = ' ') 
