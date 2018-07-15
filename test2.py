#coding:utf-8
'''
L=[('b',2),('a',1),('c',3),('d',4)]
print sorted(L, cmp=lambda x,y:cmp(-x[1],-y[1]))   # 利用cmp函数 cmp(-x[1],-y[1]) :表示反序　cmp(x[1],y[1])　：表示正序
L2=[(1,2),(3,1),(4,3),(2,4)]
print L2.sort(cmp=lambda x, y: x[0] - y[0] or y[1] - x[1])#第一个为顺序，第二个代表倒序
'''

numbers=[5,2,9,7]
numbers.sort(lambda a,b:-b+a)
print(numbers)
