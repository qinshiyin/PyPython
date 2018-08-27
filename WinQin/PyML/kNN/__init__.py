# -*- coding:utf-8 -*-
#!/usr/bin/env python

###############################################################################
# kNN: k Nearest Neighbors

# Input:      newInput: vector to compare to existing dataset (1xN)
#             dataSet:  size m data set of known vectors (NxM)
#             labels:   data set labels (1xM vector)
#             k:        number of neighbors to use for comparison

# Output:     the most popular class label
###############################################################################

import numpy as np
import operator as op

#create a dataset which contains 4 samples with 2 classes
def createDataset():
    # create a matrix: each row as a sample
    group = np.array([[1.0,0.9],[1.0,1.0],[0.1,0.2],[0.0,0.1]])
    labels = ['A','A','B','B'] # for samples and 2 classes
    return (group,labels)

# classify using kNN
def kNNClassify(newInput,dataset,lables,k):
    numSamples = dataset.shape[0] #shape[0] stands for the num of row
    ## Step 1: calculate Eucidean distance
    # tile(A, reps): Construct an array by repeating A reps times
    # the following copy numSamples rows for dataSet
    diff = np.tile(newInput,(numSamples,1)) - dataset # subtract element-wise
    squaredDiff = diff ** 2
    squaredDist = np.sum(squaredDiff,axis = 1)
    distance = squaredDist ** 0.5

    ## Step 2: sort the distance
    # argsort() returns the indices that would sort an array in a ascending order
    sortedDistIndices = np.argsort(distance)

    classCount = {}
    for i in range(k):
        ## Step 3: choose the min k distance
        voteLabel = lables[sortedDistIndices[i]]

        ## Step 4: count the times labels occur
        # when the key voteLabel is not in dictionary classCount, get()
        # will return 0
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1

    ## Step 5: the max voted class will return
    maxCount = 0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex


# Test
dataset,labels=createDataset()
testX=np.array([1.2,1.0])
k=3
outputLabel=kNNClassify(testX,dataset,labels,3)
print('Your input is:',testX,'and classified to class:',outputLabel)

testX = np.array([0.1, 0.3])
outputLabel = kNNClassify(testX, dataset, labels, 3)
print("Your input is:", testX, "and classified to class:", outputLabel)























