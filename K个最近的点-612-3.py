def ksorted(points,origin,k):
    return sorted(points,key=lambda point:((point[0]-origin[0])**2+(point[1]-point[1])**2,point[0],point[1]))[:k]

points=[(3,4),(4,3),(4,5),(65,0.1)]

print(ksorted(points,(62,3),3))

'''Output:
[(65, 0.1), (4, 3), (4, 5)]

太优美了！！！
昭昭明月，若水三千
人生苦短，我爱Python
'''

