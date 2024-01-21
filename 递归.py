# def f1(x):
#     if x> 0:
#       f1(x-1)
#       print(x)
# f1(3)
def hannuo(n,a ,b ,c):
    if n>0:
        i=0
        hannuo(n-1,a,c,b)
        print("移动%s 到 %s"%(a,c))
        hannuo(n-1,b,a,c)
        #print("移动了%d次"%i)
hannuo(3,"A" ,"B" ,"C")
