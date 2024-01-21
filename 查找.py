#顺序查找 !!!任何数组都可以使用顺序查找
def linear(li,val):#li为列表,val为要查找的值
    for ind,v in enumerate(li):#ind为数组下标,v为值,enumerate为枚举,li为枚举的列表
        if v == val:#v为值，val为要查找的值
            return ind#返回数组的下标
    else:#当for循环完毕后，没有找到需要的值，返回None
        return None

#二分查找 !!!必须是有序的数组才可以使用二分查找
def binary(li,val):#li为列表,val为要查找的值
    left = 0#定义左边界
    right =  len(li)-1#定义右边界 len(li)为数组的长度 len(li)-1为数组的最后一个元素
    while left <= right:#当左边界小于等于右边界 候选区有值
        mid = (left + right)//2#定义中间值
        if li[mid] == val:#li为列表名 mid为顺序表里中间值的下标 val为要查找的值 如果中间值等于要查找的值
            return print("有你想要查找的值 值为%s"%li[mid])
        elif li[mid] > val:#如果中间值大于要查找的值 要查找的值在mid左边
            right = mid - 1#改变右边界 右边界等于中间值减1
        elif  li[mid] < val:#如果中间值小于要查找的值 要查找的值在mid右边
            left = mid + 1#改变左边界 左边界等于中间值加1
    else:#都没有找到
        return print("没有你想要查找的值")
    
li = (1,2,4,4,5,6,7,8,9)
print(binary(li,3))
print(linear(li,5))