# -*- coding:utf-8 -*-

# 导入包
import numpy as np
import operator as op
import os

# 使用kNN算法进行分类
def kNNClassify(newInput,dataset,labels,k):
    '''
    k近邻分类算法
    输入
        newInput：与已存在数据集比较的向量(1×N)
        dataset:  已知的数据集（训练集）(M×N)
        labels：  数据集类别标签(1×N)
        k：       近邻数目
    输出：      最接近类别的标签
    '''
    numSamples = dataset.shape[0] #shape[0]表示行数
    ## 步骤1：计算欧式距离
    # np.tile(A,reps):构造由A组成的重复的矩阵，相当于Matlab的repmat()函数
    diff = np.tile(newInput,(numSamples,1)) - dataset
    sqrDiff = diff ** 2
    sqrDist = np.sum(sqrDiff,axis=1) # 按行求和
    distance = sqrDist ** 0.5

    ## 步骤2：对距离进行排序
    # np.argsort() 函数返回排序的序列下标
    sortDistIndex = np.argsort(distance)
    classCount = {}
    for i in range(k):
        ## 步骤3：选择最小距离
        voteLabel = labels[sortDistIndex[i]]

        ## 步骤4：统计类别使用的次数
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1

    ## 步骤5：返回最大类别
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return  maxIndex

# 将图像转换为向量
def img2vector(path):
    rows = 32
    cols = 32
    imgVector = np.zeros((1,rows * cols))
    fp = open(path)
    for row in range(rows):
        lineStr = fp.readline()
        for col in range(cols):
            imgVector[0,row*32+col] = int(lineStr[col])

    return imgVector

# 装载数据
def loadDataset():
    ## 步骤1：获取训练数据集
    print('        load training set...')
    datasetPath = r'D:\AgSilver\Documents\Python\WingIDE\PyML\data'
    trainingFileList = os.listdir(datasetPath + r'\trainingDigits')
    numSamples = len(trainingFileList)

    train_x = np.zeros((numSamples,32*32))
    train_y = []
    for i in range(numSamples):
        filename = trainingFileList[i]

        # 获取train_x
        train_x[i,:] = img2vector(datasetPath + '\\trainingDigits\\%s'%filename)

        # 从文件名获取标签
        label = int(filename.split('_')[0])
        train_y.append(label)

    ## 步骤2：获取测试数据集
    print('        load testing set...')
    testingFileList = os.listdir(datasetPath + r'\testDigits')
    numSamples = len(testingFileList)
    test_x = np.zeros((numSamples,32*32))
    test_y = []
    for i in range(numSamples):
        filename = testingFileList[i]

        # 获取test_x
        test_x[i,:]=img2vector(datasetPath+'\\testDigits\\%s'%filename)

        # 从文件名获取标签
        label = int(filename.split('_')[0])
        test_y.append(label)

    return (train_x,train_y,test_x,test_y)

# 测试
def test():
    ## 步骤1：加载数据
    print('Step 1: load data...')
    (train_x,train_y,test_x,test_y) = loadDataset()

    ## 步骤2：训练
    print('Step 2: training...')
    # pass

    ## 步骤3：测试
    print('Step 3: testing...')
    numTestSamples = test_x.shape[0]
    matchCount = 0
    for i in range(numTestSamples):
        predict = kNNClassify(test_x[i],train_x,train_y,3)
        if predict == test_y[i]:
            matchCount +=1
    accuracy = float(matchCount) / numTestSamples

    ##步骤4：显示结果
    print('Step 4: show the result...')
    print('        The classify accuracy is: %.2f%%'%(accuracy*100))


# Test
if __name__ == '__main__':
    test()
















