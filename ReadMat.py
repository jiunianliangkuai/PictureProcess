#coding:UTF-8
'''
Created on 2018.7.24

@author: liangkuai

'''

import os
import scipy.io as scio
import numpy

#获取当前项目的目录
dirPath = os.path.abspath('..')

#获取所有Projects的路径
index = dirPath.rfind('\\')
allProjectPath = dirPath[0:index + 1]

#拼接路径
matlabProjectPath = 'MatlabProjects\demo\ImgData_HE_itera.mat'
destinPath = allProjectPath + matlabProjectPath

#读取文件
data = scio.loadmat(destinPath)

testData = data['All_ImgData_HE_test']
SizeOfTestData = testData.size

i = 0
while i < SizeOfTestData:
    testData2 = testData[0, i]
    rank = testData2.ndim
    SizeOfSpd = testData2.size
    j = 0
    while j < SizeOfSpd:
        testData3 = testData2[0, j]
        print(testData3.shape)
        print('endline')
        j += 1
    i += 1