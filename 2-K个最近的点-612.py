import heapq

'''def s(point,origin):
    return ((point[0]-origin[0])**2+(point[1]-point[1])**2,point[0],point[1])'''

'''import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2] 
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23] 
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]'''

def ksorted(points,origin,k):
    return heapq.nsmallest(k,points,key=lambda point:((point[0]-origin[0])**2+(point[1]-point[1])**2,point[0],point[1]))


points=[(3,4),(4,3),(4,5),(65,0.1)]

print(ksorted(points,(62,3),3))

