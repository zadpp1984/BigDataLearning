# -*- coding: utf-8 -*-
"""
Created on Thu May 25 17:39:35 2017

@author: Chenanyun
"""

#!/usr/bin/env python
#coding:utf-8
import numpy as np
array = np.array([[1,2,3],[4,5,6]])
print(array)
print('维度：',array.ndim) #有几行
print('类型：',array.shape) #(2, 3) 有几行，几列
print('size:',array.size)   #总数大小
a = np.array([2,3,4], dtype=np.int64) #定义类型 int64
print(a.dtype)
a = np.zeros((3,4)) #定义一个三行四列的矩阵，里面的只全部为0
a = np.ones((3,4)) #生成一个三行四列的矩阵，值为1
a = np.empty((3,4)) #生成一个三行四列的矩阵，值接近为0
a = np.arange(1,10,2) #生成一个从1-9 步长为2的矩阵
a = np.arange(10) #生成一个从0-9 的矩阵
a = np.arange(12).reshape(3,4) #生成一个3行4列的数列
a = np.linspace(1,10,20) #生成一个1-10之间的20段线段数列
a = np.linspace(1,10,6).reshape(2,3) #生成一个1-10之间2行3列的6段线段
a = np.array([10,20,30,40])
b = np.arange(4) #生成一个0-3之间四个数的矩阵,即0-3四个数组成的矩阵
print(a,b) #打印两个矩阵
print(a+b) #矩阵相加
print(a-b) #矩阵相减
print(a*b) #矩阵相乘
print(a**b) #矩阵乘方
c = np.sin(a)*10 #对a中每个值取sin, 再乘10, con, tan都是这样的
print(c)
print(b<3) #判断b中每个数据是不是小于3, [ True  True  True False]
a = np.array([[1,2],[3,4]])
b = np.arange(4).reshape(2,2)
print(a,b)

print(a*b) #矩阵a和矩阵b中的每个值相乘, 相乘之后的数值组成的一个矩阵
print(np.dot(a,b)) #矩阵与矩阵相乘,第一个矩阵的列等于第二个矩阵的行
print(a.dot(b)) #跟上面的结果是一样的
a = np.random.random((2,4)) #在0-1之间随机生成一个2行4列的一个矩阵
print(a)
print(np.sum(a)) #矩阵里数值求和
print('###############################')
print(np.sum(a,axis=1)) #矩阵里每行的求和
print(np.sum(a,axis=0)) #矩阵里每列的求和
print(np.min(a)) #矩阵里最小值
print(np.min(a,axis=1)) #矩阵里每行最小值
print(np.min(a,axis=0)) #矩阵里每列最小值
print(np.max(a)) #矩阵里最大值
print(np.max(a,axis=1)) #矩阵里每行最大值
print(np.max(a,axis=0)) #矩阵里每列最大值

A = np.arange(1,13).reshape(3,4) #在1-13这12个数中，分成3行4列
print(A)
print(np.argmin(A)) #求矩阵中最小值的索引 0
print(np.argmax(A)) #求矩阵中最大值的索引 11
print(np.mean(A)) #求矩阵中平均值
print(A.mean()) #求矩阵中平均值
print(np.median(A)) #求矩阵中中位数
print(np.cumsum(A)) #矩阵中数值累加，第一个为第一个的值，第二个为前两个值的和，第三个为前三个的和。。。
print(np.diff(A)) #矩阵中数值累差, 后面减前面一个的差
print(np.nonzero(A)) #找出矩阵中非0的数, 结果输出两个array, 第一个为行，第二个为列
A = np.arange(13,1,-1).reshape(3,4)
print(A)
print(np.sort(A)) #逐行从小到大排序
print(np.transpose(A)) #矩阵行列变换
print(A.T) #矩阵行列变换，上面的简写
print((A.T).dot(A)) #行列变换之后的矩阵再和以前的矩阵相乘
print(np.clip(A,5,10)) #矩阵小于5的等于5, 大于10的等于10, 只保留中间部分
print(np.mean(A,axis=1)) #矩阵中对行计算平均值，axis=0是对列计算平均值

A = np.arange(1,13)
print(A)
print(A[3]) #根据矩阵索引获取值，从0开始的
A = np.arange(1,13).reshape(3,4)
print(A)
print(A[2])    #打印出第二行数据（从0开始数）
print(A[2][3]) #找出矩阵第2行第3列
print(A[2,3]) #找出矩阵第2行第3列
print(A[:,:]) #矩阵所有行所有列
print(A[:,1]) #矩阵第2列所有数
print(A[1,:]) #矩阵第2行所有数
print(A[1,2:]) #矩阵第一行第三个列及其以后的数
for row in A:
    print(row) #迭代每一行
for column in A.T: #想迭代列先行列变换，将列变行，再迭代
    print(column)
print(A.flatten()) #将三行四列的一个矩阵里的值重新放到一个新的矩阵中
for item in A.flat: #A.flat返回一个可迭代对象
    print(item)

A = np.array([1,1,1])
B = np.array([2,2,2])
C = np.vstack((A,B)) #将两个序列上下合并成一个矩阵
# C = np.hstack((A,B)) #将两个序列左右合并，变成一个序列
print(C)
print(A[np.newaxis,:]) #将A加一个维度，从一个序列变成由一行组成的矩阵
print(A[:,np.newaxis]) #将A加一个维度，从一个序列变成由一列组成的矩阵
A = A[np.newaxis,:] #将A, B 分别加一个维度
B = B[np.newaxis,:]
print('A,B:',A,B)
C = np.vstack((A,B)) #将两个矩阵上下合并
C = np.hstack((A,B)) #将两个矩阵左右合并，这里将A、B合并成一个序列
print(C)
C = np.concatenate((A,B,B,A),axis=0) #可以进行多个矩阵合并，可以指定合并维度,axis=1指每个矩阵按行左右合并，0是每个矩阵按列上下合并
print(C)

A = np.arange(12).reshape((3,4))
print(A)
print(np.split(A,2,axis=1)) #将A进行分割，分成两个array，按行等量分割，分成几块得能整除才能分割
print(np.array_split(A,3,axis=1)) #将A进行分割，按行分成三个array，可以进行不等量分割
print(np.vsplit(A,3)) #将A横向平均分割成3块
print(np.hsplit(A,2)) #将A纵向平均分割成2块

a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 8
print(a)
print(d) #都是一样的，一个改变了其他都变
print(b is a) #如果一样就是True
d[1:3] = [11,22]
print(a) #也是一样的，等于是改的同一块内存中的数据
#如果想a改变，其他赋值的不变则需要深拷贝
b = a.copy() #深拷贝，拷贝数据重新放到另外一块内存中
print(a)
b[0] = 66
print(a,b) #b变了，a没变