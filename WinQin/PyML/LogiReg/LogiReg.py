# -*- coding:utf-8 -*-
#!/usr/bin/env python

'''
@ Author: qsy
@ E-mail: qin411858963@163.com
Describe: 

'''

import numpy as np
import matplotlib.pyplot as plt
import time

def sigmoid(x):
    '''
    计算回归系数函数
    :param x: 样本向量
    :return: 回归系数
    '''
    return 1.0/(1+np.exp(-x))

def train(train_x,train_y,opts):
    '''
    训练函数，使用优化算法训练逻辑回归模型
    :param train_x: 一个矩阵，每一行是一个样本
    :param train_y: 一个矩阵，每一行是对应的类别标签
    :param opts: 优化参数，包括迭代次数以及步长变化率
    :return: 权重值
    '''
    # 计数训练时间
    start_time=time.time()

    (rows,cols)=np.shape(train_x)
    alpha=opts['alpha']
    maxIter=opts['maxIter']
    weights=np.ones((cols,1))

    #通过梯度下降优化
    for k in range(maxIter):
        if opts['optimizeType']=='gradDescent': # 梯度下降算法
            output=sigmoid(train_x*weights)
            error=train_y-output
            weights=weights+alpha*train_x.transpose()*error
        elif opts['optimizeType']=='stocGradDescent': # 随机梯度下降算法
            for i in range(rows):
                output=sigmoid(train_x[i,:]*weights)
                error=train_y[i,0]-output
                weights=weights+alpha*train_x[i,:].transpose()*error
        elif opts['optimizeType']=='smoothStocGradDescent': # 平滑随机梯度下降
            # 通过随机选择样本来减小波动
            dataIndex=[i for i in range(rows)]
            for i in range(rows):
                alpha=4.0/(1.0+k+i)+0.01
                randIndex=int(np.random.uniform(0,len(dataIndex)))
                output=sigmoid(train_x[randIndex,:]*weights)
                error=train_y[randIndex,0]-output
                weights=weights+alpha*train_x[randIndex,:].transpose()*error
                del(dataIndex[randIndex])
        else:
            raise NameError('没有支持的优化模型！')

    print('恭喜，训练完成！训练用时 %f 秒。'%(time.time()-start_time))
    return weights

def test(weights,test_x,test_y):
    '''
    测试已训练的逻辑回归模型
    :param weights:
    :param test_x:
    :param test_y:
    :return:
    '''
    (rows,cols)=np.shape(test_x)
    matchCount=0
    for i in range(rows):
        predict=sigmoid(test_x[i,:]*weights)[0,0]>0.5
        if predict==bool(test_y[i,0]):
            matchCount+=1
    accuracy=float(matchCount)/rows
    return accuracy

def show(weights,train_x,train_y):
    '''
    显示回归结果
    :param weights:
    :param train_x:
    :param train_y:
    :return:
    '''
    (rows,cols)=np.shape(train_x)
    if cols!=3:
        print("对不起，只能绘制二维图像!")
        return 1

    # 绘制所有样本
    for i in range(rows):
        if int(train_y[i,0])==0:
            plt.plot(train_x[i,1],train_x[i,2],'or')
        elif int(train_y[i,0])==1:
            plt.plot(train_x[i,1],train_x[i,2],'ob')

    # 绘制分类曲线
    min_x=min(train_x[:,1])[0,0]
    max_x=max(train_x[:,1])[0,0]
    weights=weights.getA()
    y_min_x=float(-weights[0]-weights[1]*min_x)/weights[2]
    y_max_x=float(-weights[0]-weights[1]*max_x)/weights[2]
    plt.plot([min_x,max_x],[y_min_x,y_max_x],'-g')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

def loadData():
    train_x=[]
    train_y=[]
    fp=open(r'D:\AgSilver\Documents\Python\WingIDE\PyML\data\test_LR.txt')
    for line in fp.readlines():
        lineArr=line.strip().split()
        train_x.append([1.0,float(lineArr[0]),float(lineArr[1])])
        train_y.append(float(lineArr[2]))
    return np.mat(train_x),np.mat(train_y).transpose()



# Test
if __name__=='__main__':
    # 第一步：读取数据
    print("第一步：读取数据...")
    (train_x,train_y)=loadData()
    test_x=train_x
    test_y=train_y

    # 第二步：训练
    print("第二步：训练...")
    opts={'alpha':0.001,'maxIter':50,'optimizeType':'smoothStocGradDescent'}
    # stocGradDescent gradDescent smoothStocGradDescent
    optimalWeights=train(train_x,train_y,opts)

    # 第三步：测试
    print("第三步：测试...")
    accuracy=test(optimalWeights,test_x,test_y)

    # 第四步：显示结果
    print('第四步：显示结果...')
    print('分类精度为：%.3f%%'%(accuracy*100))
    show(optimalWeights,train_x,train_y)















