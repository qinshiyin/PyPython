#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import numpy as np
import matplotlib.pyplot as plt

# 计算欧式距离
def euclideanDistance(vector1,vector2):
    '''
    计算欧式距离
    :param vector1: 向量1
    :param vector2: 向量2
    :return: 欧式距离结果向量
    '''
    return np.sqrt(np.sum(np.power(vector1-vector2,2)))

# 随机初始化
def initCentroids(dataset,k):
    '''
    随机初始化
    :param dataset: 给定的待分类数据集
    :param k: 聚类数目
    :return: 初始化后的类别
    '''
    np.random.seed(int(time.monotonic()))
    (rows,cols)=dataset.shape
    centroids=np.zeros((k,cols))
    for i in range(k):
        index=int(np.random.uniform(0,rows))
        centroids[i,:]=dataset[index,:]
    return centroids

# k均值聚类算法
def kMeans(dataset,k):
    '''
    k均值聚类算法
    :param dataset: 待分类数据集
    :param k: 待分类别
    :return: 分好类别的数据集
    '''
    rows=dataset.shape[0]
    # 第一列存储所属类别
    # 第二列存储其与质心的距离
    clusterAssment=np.mat(np.zeros((rows,2)))

    clusterChanged=True

    ## 第一步：初始化
    centroids=initCentroids(dataset,k)

    while clusterChanged:
        clusterChanged=False
        ## 对每一个样本
        for i in range(rows):
            minDist=100000.0
            minIndex=0
            ## 对每一个质心
            ## 第二步：找出距离最近的质心
            for j in range(k):
                distance=euclideanDistance(centroids[j,:],dataset[i,:])
                if distance<minDist:
                    minDist=distance
                    minIndex=j

            ## 第三步：更新聚类
            if clusterAssment[i,0]!=minIndex:
                clusterChanged=True
                clusterAssment[i,:]=minIndex,minDist**2

        # 第四步：更新质心
        for j in range(k):
            pointInCluster=dataset[np.nonzero(clusterAssment[:,0].A==j)[0]]
            centroids[j,:]=np.mean(pointInCluster,axis=0)

    print('恭喜，聚类完成')
    return (centroids,clusterAssment)

# 显示2D聚类结果
def showCluster(dataset,k,centroids,clusterAssment):
    '''
    显示2D聚类结果
    :param dataset:
    :param k:
    :param centroids:
    :param clusterAssment:
    :return: 无
    '''
    (rows,cols)=dataset.shape
    if cols!=2:
        print('对不起！该函数只能绘制2维图象。')
        return 1

    mark=['or','ob','og','ok','^r','+r','sr','dr','<r','pr']
    if k>len(mark):
        print('对不起！你的k值太大！请联系qsy。')
        return 1
    # 显示所有样本
    for i in range(rows):
        markIndex=int(clusterAssment[i,0])
        plt.plot(dataset[i,0],dataset[i,1],mark[markIndex])

    mark=['Dr','Db','Dg','Dk','^b', '+b', 'sb', 'db', '<b', 'pb']
    # 画质心
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)

    plt.show()

# 测试
if __name__=='__main__':
    ## 第一步：加载数据
    print('第一步：加载数据')
    dataset=[]
    fp=open(r'D:\AgSilver\Documents\Python\WingIDE\PyML\data\test_k_means.txt')
    for line in fp.readlines():
        lineArr=line.strip().split('\t')
        dataset.append([float(lineArr[0]),float(lineArr[1])])

    ## 第二步：聚类
    print('第二步：聚类...')
    dataset=np.mat(dataset)
    k=4
    (centroids,clusterAssment)=kMeans(dataset,k)

    ## 第三步：显示结果
    print('第三步：显示结果...')
    showCluster(dataset,k,centroids,clusterAssment)
