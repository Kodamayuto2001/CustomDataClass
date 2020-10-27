import numpy as np 
from PIL import Image 
import os 
import cv2
import matplotlib.pyplot as plt 

class CustomDataSet:
    def __init__(self):
        pass 

    def setRootDir(self,RootDir):
        self.rootDir = RootDir

    def setSaveDir(self,saveDir):
        self.saveDir = saveDir

    def setLogName(self,logName):
        self.logName = logName
    
    def set2ndDir(self):
        self.list2ndDir = [f for f in os.listdir(self.rootDir) if os.path.isdir(os.path.join(self.rootDir,f))]

    def setLen2ndDir(self):
        self.list3rdDir = [ 
            [] for i in self.list2ndDir
        ]

    def set3rdDir(self):
        for i,d in enumerate(self.list2ndDir):
            self.list3rdDir[i] = [f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f))]


    def set4thDir(self):
        self.list4thDir = [
            [
                [
                    [] for k in self.list3rdDir[0][0]
                ] for j in self.list3rdDir[0]
            ] for i in self.list2ndDir
        ] 
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                self.list4thDir[i][j]  = [f for f in os.listdir(self.rootDir+"/"+d1+"/"+d2) if os.path.isdir(os.path.join(self.rootDir+"/"+d1+"/"+d2,f))]
        # print(self.list4thDir)
        for i,d1 in enumerate(self.list2ndDir):
            for j,d2 in enumerate(self.list3rdDir[i]):
                for k,d3 in enumerate(self.list4thDir[i][j]):
                    self.list4thDir[i][j][k] = self.rootDir+"/"+d1+"/"+d2+"/"+d3
                    print(self.list4thDir[i][j][k])
    
    def loadFile(self):
        pass 

    def saveFile(self):
        pass 

    def logFile(self):
        pass 

    def test1(self):
        print(os.listdir(self.rootDir))
        print([f for f in os.listdir(self.rootDir) if os.path.isdir(os.path.join(self.rootDir,f))])

    def test2(self):
        print(self.list2ndDir)

    def test3(self):
        l3 = []
        print(self.list2ndDir[0])
        # Resources1
        print([f for f in os.listdir(self.list2ndDir[0]) if os.path.isdir(os.path.join(self.list2ndDir[0],f))])
        # ['train']
        for d in self.list2ndDir:
            print(d)
            l3 = [f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f))]
            print(l3)

    def test4(self):
        print(len(self.list2ndDir))
        for i,d in enumerate(self.list2ndDir):
            self.list3rdDir[i] = [f for f in os.listdir(d) if os.path.isdir(os.path.join(d,f))]
        print(self.list3rdDir)
        # [['test', 'train'], ['test', 'train'], ['test', 'train'], ['test', 'train']]

    def test5(self):
        self.list4thDir = [
            [
                [
                    [] for k in self.list3rdDir[0][0]
                ] for j in self.list3rdDir[0]
            ] for i in self.list2ndDir
        ] 
        print(self.list4thDir)

    def test6(self):
        # for i,_ in enumerate(self.list2ndDir):
        #     for j,d2 in enumerate(self.list3rdDir):
        #         self.list4thDir[i][j] = [f for f in os.listdir(d2) if os.path.isdir(os.path.join(d2,f))]
        # print(self.list4thDir)
        # print(self.list4thDir)
        # print(self.list4thDir[0])
        # print(self.list4thDir[0][0])
        # [[[], []], [[], []], [[], []], [[], []]]
        pass 

    def test7(self):
        v = np.zeros((1,len(self.list2ndDir),len(self.list3rdDir[0])),dtype=str)
        print(v)
        print(v[0])
        print(v[0][0])
        print(v[0][0][0])
        v[0][0][0] = "hoge"
        print(v)
        v = np.array(self.list3rdDir)
        print(v)
        v = np.array([self.list3rdDir],dtype="U10")
        print(v)
        v = np.zeros((1,len(self.list2ndDir),len(self.list3rdDir[0])),dtype="U10")
        print(v)
        v[0][0][0] = "hoge"
        print(v)

    def test8(self):
        print(self.list3rdDir)
        print(self.list3rdDir[0])
        print(self.list3rdDir[0][0])
        print(self.list2ndDir)
        print(self.list2ndDir[0])
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[0][0]+"/")
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[0][1]+"/")
        print(self.rootDir+"/"+self.list2ndDir[1]+"/"+self.list3rdDir[0][0]+"/")
        print(self.rootDir+"/"+self.list2ndDir[1]+"/"+self.list3rdDir[0][1]+"/")
        print(self.rootDir+"/"+self.list2ndDir[0]+"/"+self.list3rdDir[1][1]+"/")
        for i,d1 in enumerate(self.list2ndDir):
            print(i)
            print(d1)
            # 0
            # Resources1
            # 1
            # Resources2
            # 2
            # Resources3
            # 3
            # Resources4
        for j,d2 in enumerate(self.list3rdDir):
            print(j)
            print(d2)
            # 0
            # ['test', 'train']
            # 1
            # ['test', 'train']
            # 2
            # ['test', 'train']
            # 3
            # ['test', 'train']
        for k,d3 in enumerate(self.list3rdDir[0]):
            print(d3)
            # test
            # train
        print("-----------------------------------------------------------")
        for i,d1 in enumerate(self.list2ndDir):
            # print(self.rootDir+"/"+d1+"/")
            # ../Project3/Resources1/
            for j,d2 in enumerate(self.list3rdDir[i]):
                
                print(self.rootDir+"/"+d1+"/"+d2)
                self.list4thDir[i][j]  = [f for f in os.listdir(self.rootDir+"/"+d1+"/"+d2) if os.path.isdir(os.path.join(self.rootDir+"/"+d1+"/"+d2,f))]
        print(self.list4thDir)


if __name__ == "__main__":
    CD = CustomDataSet()
    CD.setRootDir(RootDir="../Project3")
    CD.set2ndDir()
    CD.setLen2ndDir()
    CD.set3rdDir()
    CD.set4thDir()
    # CD.test7()
    # CD.test5()
    # CD.test8()