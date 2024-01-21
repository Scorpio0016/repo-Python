# import heapq #python中自带的堆排序模块
# import random #生成随机数函数
# li = list(range(10))#定义一个列表li 长度1-100
# random.shuffle(li)#打乱列表中的顺序
# print(li)#输出列表
# heapq.heapify(li)#建堆 生成一个小根堆 完全二叉数中每一个二叉数中的根为树中最小
# n = len(li)#定义一个函数n n为列表长度
# for i in range(n,0):#for循环 从列表中最后一个元素开始循环
#     print(heapq.heappop(li),end=",")#heappop从列表中t

# nli  = [(-i,li[i]) for i in range(len(li))]
# print(nli,'插入负数后的小根堆')
# heapq.heapify(nli) #以插入的负数做小根堆，越大的数字插入的负数就越小，所以这样就相当于做了大根堆
# # 此时已经按照第一个值变成了小顶堆，即变成了逆序
# max_heap = list()
# while nli:
#     _, s = heapq.heappop(nli) #删除并返回 newl中的最小元素
#     max_heap.append(s)
# print(max_heap,'输出的大根堆')
 
# def sift(li,low,hight):#定义一个sift函数 li指的是列表 low堆的根节点位置 hight是堆最后一个元素的位置
#     i = low#i最开始指向根节点的位置
#     j = 2 * i + 1 #j为指向节点的左孩子
#     tmp = li[low] #定义一个tmp变量 把根结点存起来
#     while j <= hight: #判断j（指向节点的左孩子）的位置是否有数 
#         if j+1 <= hight and li[j+1] < li[j]: #j+i<=hight判断是否有右孩子 and 右孩子的数大于左孩子
#             j = j+1 #j指向节点的左孩子改为指向右孩子
#         elif li[j]<tmp:#判断孩子节点是否大于一开始所存的根节点
#             li[i] = li[j]#把数组中下标为i的数更改为下标为j的数 j为两个孩子节点中最大的数
#             i = j#把下标为i的数的下标更改为j
#             j =2*i+1#把下标为j的数的下标更改为自己的孩子节点
#         else:#数组中下标为j的数小于或等于tmp
#             li[i] = tmp#把tmp存回原来的位置
#             break#跳出
#     else:#判断j（指向节点的左孩子）的位置没有数
#         li[i] = tmp#把tmp存回原来的位置
#  #把调整的根堆进行排序



import random #生成随机数函数
import heapq #python中自带的堆排序模块 *生成的是小根堆*

# def topk(li,k):
#     heap=[]
#     for i in li:
#         if len(heap) < k:
#             heapq.heappush(heap,i)
#         else:
#             heapq.heappushpop(heap,i)
#         return heap
# li = list(range(1000))
# random.shuffle(li)
# print(topk(li,5))















# def topk(li,k):
#     heapq.heapify(li)
#     heap = li[0:k]
#     for i in range (k-2//2,-1,-1):
#         heapq.heapify(heap)
        
#     for i in range(k+1,len(li)-1):
#         if li[i] > heap[0]:
#             heap[0] = li[i]
#             heapq.heapify(heap)
            
#     for i in range(k-1,-1,-1):
#         heap[0],heap[i] = heap[i],heap[0]
#         heapq.heapify(heap)
#         print(heap)
#     return heap

# li = list(range(10))#定义一个列表li 长度1-100
# random.shuffle(li)#打乱列表中的顺序
# #print(topk(li,5))
# topk(li,5)

