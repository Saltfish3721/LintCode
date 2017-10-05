#题目
##描述
给定一些 points 和一个 origin，从 points 中找到 k 个离 origin 最近的点。按照距离由小到大返回。如果两个点有相同距离，则按照x值来排序；若x值也相同，就再按照y值排序。
##样例
给出 points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
返回 [[1,1],[2,5],[4,4]]

#思路
1. 得到点-距离对应的dict

2. 对距离进行升序排序（重点）

3. 取出前k个距离

#一些方法
1. [对dict按key或者value排序@Stack Overflow](https://stackoverflow.com/questions/613183/how-to-sort-a-dictionary-by-value)

2. 在for循环中，如何获得当前元素的索引值？

```
points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
l=points.index([4,6])
print(l)
```
输出

```
0
```

#代码

（距离相同的情况待定）

```
import operator

class Solution:

    def kClosest(self,points, origin, k):

        # 得到点-距离的dict
        p_d_dict = {}
        for point in points:
            distance_square =(point[0] - origin[0])**2+(point[1] - origin[1])**2
            p_d_dict[points.index(point)]=distance_square 
                                        #老版本：p_d_dict[points.index(point)]=distance_square
            
        # 对dict排序
        sorted_dict = sorted(p_d_dict.items(), key=operator.itemgetter(1))#这是一个list，元素是tuple:(key，value)

        k_list=[]

        for x in range(0,k):
            k_list.append(points[sorted_dict[x][0]])

        return k_list

solution=Solution()#原来这种情况下要创建类的实例啊

points = [[4,6],[4,7],[-4,4],[4,-4],[1,1]]
origin = [0, 0]
k = 3

result=solution.kClosest(points,origin,k)

print(result)

'''
Output:

[[1, 1], [-4, 4], [4, -4]]
'''
```