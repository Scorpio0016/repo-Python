#冒泡排序
import random#引入生成随机数函数
def buuble(li):#定义一个buuble函数 li为列表 冒泡排序
    for i in range(len(li)-1):#i为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-1为数组的最后一个元素 
        exchange = False#定义一个exchange变量 用来判断是否进行交换
        for j in range(len(li)-i-1):#j为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-i-1为数组的倒数第二个元素
            if li[j] > li [j+1]:#如果第j个元素大于第j+1个元素
                li[j],li[j+1] = li[j+1],li[j]#交换j和j+1的值
                exchange = True#exchange变量为True
        print(li)#打印数组
        if  not exchange:#如果exchange为False
            return#直接返回
#li = [random.randint(0,100) for i in range(10)]
# li = [9,8,1,2,3,4,5,6,7]
# buuble(li)

#选择排序
def select(li):#定义一个select函数 li为列表 选择排序Low
    li_new = []#定义一个新的li_new列表
    for i in range(len(li)):#i为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-1为数组的最后一个元素
        min_val = min(li)#定义一个min_val变量 用来存储最小值 min(li)为最小值
        li_new.append(min_val)#将最小值添加到li_new列表中 append为添加
        li.remove(min_val)#将最小值从li列表中删除 remove为删除
    return li_new#返回li_new列表
#选择排序升级版
def select_grade(li):#定义一个select_grade函数 li为列表 选择排序High
    for i in range(len(li)-1):#i为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-1为数组的最后一个元素
        min_loc=i#定义一个min_loc变量 用来存储最小值的下标
        for j in range(i+1,len(li)):#j为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-i-1为数组的倒数第二个元素
            if li[j]<li[min_loc]:#如果第j个元素小于第min_loc个元素
                min_loc=j#min_loc变量等于j
        li[i],li[min_loc]=li[min_loc],li[i]#交换i和min_loc的值
        print(li)#打印数组

# li = [1,3,5,7,8,9,4,6,2]
# print(li)
# #print(select(li))
# print(select_grade(li))

#插入排序
def insert (li):#定义一个insert函数 li为列表 插入排序
    for i in range(1,len(li)):#i为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-1为数组的最后一个元素
        tmp = li[i]#定义一个tmp变量 用来存储li[i] li[i]数组中下标为i的数
        j = i - 1#定义一个j变量 j下标=i-1的下标
        while j >= 0 and li[j] > tmp:#j为循环次数 range()为生成一个数组 len(li)为数组的长度 len(li)-i-1为数组的倒数第二个元素 如果li[j]大于tmp
            li[j+1] = li[j]#交换j和j+1的值
            j -= 1#j下标减1
        li[j+1] = tmp #将tmp插入到j+1的位置
        print(li)#打印数组
# li = [1,3,5,7,8,9,4,6,2]
# insert(li)
        
#快速排序
def partition(li,left,right):#定义一个partition函数 li为列表 left为数组的左边界 right为数组的右边界    
    tmp = li[left]#定义一个tmp变量 用来存储li[left]的值 这个值为中间值
    while left < right:#当左边界小于右边界
        while left < right and li[right] >= tmp: #如果左边界小于右边界并且li[right]的值大于等于tmp的值
            right -= 1#右边界下标减1
        li[left] = li[right]#将li[left]的值给为li[right]
        while left < right and li[left] <= tmp:#如果左边界小于右边界并且li[left]的值小于等于tmp的值
            left += 1#左边界下标加1
        li[right] = li[left]#将li[right]的值给为li[left]
    li[left] = tmp#将tmp的值给为li[left] tmp为中间值
    return left#返回left
def quick(li,left,right):#定义一个quick函数 li为列表 left为数组的左边界 right为数组的右边界
    if left < right:#检查左边界是否小于右边界如果不满足这个条件，说明已经处理完了整个数组，不需要再进行排序。 
        mid = partition(li,left,right)#定义一个mid变量 在满足条件的情况下，函数调用 partition 函数，
                                        #将数组 li 进行分区。partition 函数会返回一个索引 mid，表示分区后的中间位置。
        quick(li,left,mid - 1)#接下来，函数对分区后的左侧和右侧递归调用 quick 函数。左侧的调用是 quick(li, left, mid - 1)，对左侧子数组进行排序。
        quick(li,mid + 1,right)#右侧的调用是 quick(li, mid + 1, right)，对右侧子数组进行排序。

# li = [5,7,4,6,3,1,2,9,8]
# quick(li,0,len(li)-1)
# print(li)
        
#堆排序(比较排序*大根堆 把比较符号交换就变成小根堆)
 #调整堆的函数
def sift(li,low,hight):#定义一个sift函数 li指的是列表 low堆的根节点位置 hight是堆最后一个元素的位置
    i = low#i最开始指向根节点的位置
    j = 2 * i + 1 #j为指向节点的左孩子
    tmp = li[low] #定义一个tmp变量 把根结点存起来
    while j <= hight: #判断j（指向节点的左孩子）的位置是否有数 
        if j+1 <= hight and li[j+1] > li[j]: #j+i<=hight判断是否有右孩子 and 右孩子的数大于左孩子
            j = j+1 #j指向节点的左孩子改为指向右孩子
        elif li[j]>tmp:#判断孩子节点是否大于一开始所存的根节点
            li[i] = li[j]#把数组中下标为i的数更改为下标为j的数 j为两个孩子节点中最大的数
            i = j#把下标为i的数的下标更改为j
            j =2*i+1#把下标为j的数的下标更改为自己的孩子节点
        else:#数组中下标为j的数小于或等于tmp
            li[i] = tmp#把tmp存回原来的位置
            break#跳出
    else:#判断j（指向节点的左孩子）的位置没有数
        li[i] = tmp#把tmp存回原来的位置
 #把调整的根堆进行排序
def heap(li):#定义一个heap函数 li指的是列表
    n = len(li)-1#定义一个变量n n为列表长度减1 为最后一个数的下标
    for i in range(n-1//2,-1,-1):#for循环 i (从最后一个叶子节点的根节点到-1，-1不循环)
        sift(li,i,n)#把完全二叉树上的小树进行调整 i为sift函数中的low n为sift函数中的hight
    for i in range(n,-1,-1):#for循环 i (从最后一个叶子节点到-1，-1不循环)
        li[0],li[i] = li[i],li[0]#交换最后一个叶子节点和根结点的数
        sift(li,0,i-1)#把完全二叉树上的小树进行调整 根节点为sift函数中的low i-1节点为sift函数中的hight
# li = [5,7,4,6,3,1,2,9,8]
# heap(li)
# print(li)
    
#用py自带的堆排序模块（小根堆）
# import heapq #python中自带的堆排序模块
# import random #生成随机数函数
# li = list(range(100))#定义一个列表li 长度1-100
# random.shuffle(li)#打乱列表中的顺序
# print(li)#输出列表
# heapq.heapify(li)#建堆 生成一个小根堆 完全二叉数中每一个二叉数中的根为树中最小
# n = len(li)#定义一个函数n n为列表长度
# for i in range(n):#for循环 从列表中最后一个元素开始循环
#     print(heapq.heappop(li))#heappop从列表中弹出一个元素

#用py自带的堆排序（小根堆）实现topk切片问题
# import heapq #python中自带的堆排序模块
# import random #生成随机数函数 
# def topk(nums,k):
#     heap = []
#     for num in nums:
#         if len(heap) < k:
#             heapq.heappush(heap, num)
#         else:
#             heapq.heappushpop(heap, num)
#     return heap
# nums = list(range(1000))
# random.shuffle(nums)
# print(topk(nums,5))

#heapq模块（小根堆）：使用方法
#heapq.heapify(list)：将列表转换为最小堆。
#heapq.heappush(heap, item)：将元素添加到堆中。
#heapq.heappop(heap)：弹出并返回堆中的最小元素。
#heapq.heappushpop(heap, item)：将元素添加到堆中，并返回堆中的最小元素。
#heapq.heapreplace(heap, item)：弹出并返回堆中的最小元素，然后将元素添加到堆中。
        
#归并排序
def merge(li,low,mid,hight):#定义一个merge函数 li指的是列表 low是列表中第一个元素下标 mid是列表中中间的元素下标 hight是列表中最后一个元素下标
    i = low#定义一个变量i i为low的下标
    j = mid + 1#定义一个变量j j为mid+1的下标
    ltmp = []#定义一个空列表
    while i <= mid and j<=hight:#判断列表的左右是否有元素
        if li[i]<li[j]:#判断第i个的数是否小于第j个的数
            ltmp.append(li[i])#把第i个的数放入ltmp
            i+=1#i下标加1
        else:#第i个的数大于或等于第j个的数
            ltmp.append(li[j])#把第j个的数放入ltmp
            j+=1#j下标加1
    while i <= mid:#判断列表的左边是否有元素
        ltmp.append(li[i])#把剩下的元素放入ltmp
        i+=1#i下标加1
    while j <= hight:#判断列表的右边是否有元素
        ltmp.append(li[j])#把剩下的元素放入ltmp
        j+=1#j下标加1
    li[low:hight+1] = ltmp#把ltmp列表中的元素放入原来的li列表中
def merge_sort(li,low,hight):#定义一个merge_sort函数 li指的是列表 low是列表中第一个元素下标 hight是列表中最后一个元素下标
    if low < hight:#判断列表是否为空
        mid = (low+hight)//2#找到中间的元素
        merge_sort(li,low,mid)#递归调用 排序左边
        merge_sort(li,mid+1,hight)#递归调用 排序右边
        merge(li,low,mid,hight)#调用merge函数
# li = [5,7,4,6,3,1,2,9,8]
# merge_sort(li,0,len(li)-1)
# print(li)

