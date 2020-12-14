from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,QDesktopWidget, QWidget,QTableWidget,QTableView,QTableWidgetItem,QHeaderView,QGraphicsScene,QGraphicsPixmapItem,QFileDialog
from Design import Ui_MainWindow

import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from xlrd import open_workbook
from openpyxl.reader.excel import load_workbook
from shutil import copyfile
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from skimage import data, img_as_float,io
from skimage.measure import compare_ssim
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from math import sqrt
from math import *

class MainWindow(QWidget,Ui_MainWindow):

    veriseti_file_path = ""
    select_classes_index=0
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)   
          
        self.model = QtGui.QStandardItemModel(self)
        self.model_x_train = QtGui.QStandardItemModel(self)
        self.btnyukle.clicked.connect(self.veriyukle)
        self.btnyukle_2.clicked.connect(self.veriyukle2)
        self.btnveribol.clicked.connect(self.veribol)
        self.btnveribol_2.clicked.connect(self.hesapla)   

      
    dataset = []
    X,Y=[],[]
    def veriyukle(self):
        file,_ = QFileDialog.getOpenFileName(self, 'Open file', './',"CSV files (*.csv)")
        #copyfile(file, "./"+self.dataset_file_path)
        self.dataset_file_path = file
        print(self.dataset_file_path)
        #self.dataset = pd.read_csv(self.dataset_file_path, engine='python')  
        #self.read_CSV(self.dataset_file_path)
        self.dataset = pd.read_csv(self.dataset_file_path, engine='python')
        self.dataset = self.dataset.values
        
        
        #print(len(self.dataset))
        self.verigoster.clear()
        self.verigoster.setColumnCount(len(self.dataset[0]))
        self.verigoster.setRowCount(len(self.dataset))
        for i,row in enumerate(self.dataset):
           for j,cell in enumerate(row):
               self.verigoster.setItem(i,j, QTableWidgetItem(str(cell)))
        self.verigoster.horizontalHeader().setStretchLastSection(True)
        self.verigoster.resizeColumnsToContents()
    
       
    def read_CSV(self,file):
        with open(file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                lines=[]
                for value in row:
                    lines.append(str(round(float(value),3)))
                    
                self.dataset.append(lines)
        csvFile.close()
    def read_CSV2017(self,file):
        with open(file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                lines=[]
                for value in row:
                    lines.append(str(round(float(value),3)))
                    
                self.datasetcekilen2017.append(lines)
        csvFile.close()
    
    def read_CSVay2016(self,file):
        with open(file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                lines=[]
                for value in row:
                    lines.append(str(round(float(value),3)))
                    
                self.datasetcekilen2016.append(lines)
        csvFile.close()    
    
    def read_CSV2015(self,file):
        with open(file, 'r') as csvFile:
            reader = csv.reader(csvFile)
            for row in reader:
                lines=[]
                for value in row:
                    lines.append(str(round(float(value),3)))
                    
                self.datasetcekilen2015.append(lines)
        csvFile.close()    
    
    gecicideger2=0
    datasetcekilen2017=[]
    datasetcekilen2016=[]
    datasetcekilen2015=[]

    dataset2 = []
    datasetyenigelen = []
    datasetyil = []
    datasetgecici = []

    datasetay = [] 
    datasettoplam=[]
    yenidataset=[]
    rmsedataset=[]
    rmsedataset2=[]

    X2,Y2=[],[]    
    
    def veriyukle2(self):
        toplam=0.0
        sabitdegeryil=''
        sabitdegeryil2=''
        sabitdegeray=''
        sabitdegeray2=''
        gecicidegeryil=''
        gecicidegeryil2=''
        gecicidegeray=''
        gecicidegeray2=''
        sayac=0
        sonuc=0.0
        for i in range(len(self.dataset)):
            gecicidegeray2=gecicidegeray
            gecicidegeryil2=gecicidegeryil
            if sabitdegeryil==sabitdegeryil2:                
                deger=self.dataset[i,0]
                sabitdegeryil=deger[0]+deger[1]+deger[2]+deger[3]
            if sabitdegeray==sabitdegeray2: 
                deger=self.dataset[i,0]                                         
                sabitdegeray=deger[5]+deger[6] 
                
            deger3=self.dataset[i,0]
            gecicidegeryil=deger3[0]+deger3[1]+deger3[2]+deger3[3]
            gecicidegeray=deger3[5]+deger3[6]
                                
            if sabitdegeryil==gecicidegeryil:                                
                if sabitdegeray==gecicidegeray:                    
                    deger2=self.dataset[i,1]
                    toplam=toplam+float(deger2) 
                    sayac=sayac+1
                else:
                    sonuc=toplam/sayac
                    self.datasettoplam.append(sonuc)
                    self.datasetay.append(gecicidegeray2)
                    self.datasetyil.append(gecicidegeryil2)
                    sabitdegeray=''
                    sabitdegeray=gecicidegeray
                    toplam=0.0
                    sayac=0                    
            else:
                
                sonuc=toplam/sayac
                self.datasettoplam.append(sonuc)
                self.datasetay.append(gecicidegeray2)
                self.datasetyil.append(gecicidegeryil2)
                sabitdegeray=''
                sabitdegeray=gecicidegeray
                toplam=0.0
                sayac=0                    
                sabitdegeryil=''
                sabitdegeryil=gecicidegeryil
               
        self.datasettoplam.append(toplam)       
        self.datasetay.append(gecicidegeray)
        self.datasetyil.append(gecicidegeryil)  
        
        for j in range(len(self.datasetyil)):
            degersay=self.datasetyil[j]+","+self.datasetay[j]+","+str(self.datasettoplam[j])
            self.yenidataset.append(degersay)
                                        
        saveFile=open('yeniveriseti.csv','w')
        saveFile.write("yil,ay,ort \n")
        for j in range(len(self.yenidataset)):
            text=self.yenidataset[j]
            saveFile.write(text+"\n")
        saveFile.close()            
        
        self.dataset2 = pd.read_csv("./yeniveriseti.csv", engine='python')
        self.datasetyenigelen = self.dataset2.values    
        
        self.yenidataset=[]
        for j in range(len(self.datasetyenigelen)):
            if (str(self.datasetyenigelen[j,0])=="2017.0"):
                degersay=str(self.datasetyenigelen[j,0])+","+str(self.datasetyenigelen[j,1])+","+str(self.datasetyenigelen[j,2])
                self.yenidataset.append(degersay)        

        saveFile=open('2017veriseti.csv','w')
        saveFile.write("yil,ay,ort \n")
        for j in range(len(self.yenidataset)):
            text=self.yenidataset[j]
            saveFile.write(text+"\n")
        saveFile.close()         

        self.datasetgecici=[]                 
        self.datasetgecici = pd.read_csv("./2017veriseti.csv", engine='python')
        self.dataset2017 = self.datasetgecici.values
        
        #print(len(self.dataset)) 2017 verileriiiii
        self.verigoster_5.clear()
        self.verigoster_5.setColumnCount(len(self.dataset2017[0]))
        self.verigoster_5.setRowCount(len(self.dataset2017))
        for i,row in enumerate(self.dataset2017):
           for j,cell in enumerate(row):
               self.verigoster_5.setItem(i,j, QTableWidgetItem(str(cell)))
        self.verigoster_5.horizontalHeader().setStretchLastSection(True)
        self.verigoster_5.resizeColumnsToContents()        
#2016--------------------2016------------------------------2016--------------------------------
        self.yenidataset=[]
        for j in range(len(self.datasetyenigelen)):
            if (str(self.datasetyenigelen[j,0])=="2016.0"):
                degersay=str(self.datasetyenigelen[j,0])+","+str(self.datasetyenigelen[j,1])+","+str(self.datasetyenigelen[j,2])
                self.yenidataset.append(degersay)        

        saveFile=('2016veriseti.csv','w')
        saveFile.write("yil,ay,ort \n")
        for j in range(len(self.yenidataset)):
            text=self.yenidataset[j]
            saveFile.write(text+"\n")
        saveFile.close()         

        self.datasetgecici=[]                 
        self.datasetgecici = pd.read_csv("./2016veriseti.csv", engine='python')
        self.dataset2016 = self.datasetgecici.values
        
        #print(len(self.dataset)) 2016 verileriiiii
        self.verigoster_4.clear()
        self.verigoster_4.setColumnCount(len(self.dataset2016[0]))
        self.verigoster_4.setRowCount(len(self.dataset2016))
        for i,row in enumerate(self.dataset2016):
           for j,cell in enumerate(row):
               self.verigoster_4.setItem(i,j, QTableWidgetItem(str(cell)))
        self.verigoster_4.horizontalHeader().setStretchLastSection(True)
        self.verigoster_4.resizeColumnsToContents()        
#-----------------------------------2015---------2015------------------------------------------------------        
        self.yenidataset=[]
        for j in range(len(self.datasetyenigelen)):
            if (str(self.datasetyenigelen[j,0])=="2015.0"):
                degersay=str(self.datasetyenigelen[j,0])+","+str(self.datasetyenigelen[j,1])+","+str(self.datasetyenigelen[j,2])
                self.yenidataset.append(degersay)        

        saveFile=open('2015veriseti.csv','w')
        saveFile.write("yil,ay,ort \n")
        for j in range(len(self.yenidataset)):
            text=self.yenidataset[j]
            saveFile.write(text+"\n")open
        saveFile.close()         

        self.datasetgecici=[]                 
        self.datasetgecici = pd.read_csv("./2015veriseti.csv", engine='python')
        self.dataset2015 = self.datasetgecici.values
        
        #print(len(self.dataset)) 2016 verileriiiii
        self.verigoster_3.clear()
        self.verigoster_3.setColumnCount(len(self.dataset2015[0]))
        self.verigoster_3.setRowCount(len(self.dataset2015))
        for i,row in enumerate(self.dataset2015):
           for j,cell in enumerate(row):
               self.verigoster_3.setItem(i,j, QTableWidgetItem(str(cell)))
        self.verigoster_3.horizontalHeader().setStretchLastSection(True)
        self.verigoster_3.resizeColumnsToContents()         

        
        
        #print(len(self.dataset))
        self.verigoster_2.clear()
        self.verigoster_2.setColumnCount(len(self.datasetyenigelen[0]))
        self.verigoster_2.setRowCount(len(self.datasetyenigelen))
        for i,row in enumerate(self.datasetyenigelen):
           for j,cell in enumerate(row):
               self.verigoster_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.verigoster_2.horizontalHeader().setStretchLastSection(True)
        self.verigoster_2.resizeColumnsToContents()
        



    X_train=[]
    X_test=[]
    y_train=[]
    y_test=[]
    def veribol(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0   
#----------------------------2015 bölme işlemi--------------------------------------------------------------#
        veriler = pd.read_csv('2015veriseti.csv')     
        x = veriler.iloc[:,1:2]
        y = veriler.iloc[:,2:]
        X = x.values
        Y = y.values 
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X,Y, test_size=0.5, random_state=42)
        #print(len(self.dataset))
        self.list_x_train.clear()
        self.list_x_train.setColumnCount(len(self.X_train[0]))
        self.list_x_train.setRowCount(len(self.X_train))
        for i,row in enumerate(self.X_train):
           for j,cell in enumerate(row):
               self.list_x_train.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_train.horizontalHeader().setStretchLastSection(True)
        self.list_x_train.resizeColumnsToContents()

        #print(len(self.dataset))
        self.list_y_train.clear()
        self.list_y_train.setColumnCount(len(self.y_train[0]))
        self.list_y_train.setRowCount(len(self.y_train))
        for i,row in enumerate(self.y_train):
           for j,cell in enumerate(row):
               self.list_y_train.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_train.horizontalHeader().setStretchLastSection(True)
        self.list_y_train.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_x_test.clear()
        self.list_x_test.setColumnCount(len(self.X_test[0]))
        self.list_x_test.setRowCount(len(self.X_test))
        for i,row in enumerate(self.X_test):
           for j,cell in enumerate(row):
               self.list_x_test.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_test.horizontalHeader().setStretchLastSection(True)
        self.list_x_test.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_y_test.clear()
        self.list_y_test.setColumnCount(len(self.y_test[0]))
        self.list_y_test.setRowCount(len(self.y_test))
        for i,row in enumerate(self.y_test):
           for j,cell in enumerate(row):
               self.list_y_test.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_test.horizontalHeader().setStretchLastSection(True)
        self.list_y_test.resizeColumnsToContents()
        
#---------------------2016 verileri bölme---------------------
        veriler = pd.read_csv('2016veriseti.csv')     
        x = veriler.iloc[:,1:2]
        y = veriler.iloc[:,2:]
        X = x.values
        Y = y.values 
        self.X_trainx, self.X_testx, self.y_trainx, self.y_testx = train_test_split(X,Y, test_size=0.5, random_state=42)
        #print(len(self.dataset))
        self.list_x_train_2.clear()
        self.list_x_train_2.setColumnCount(len(self.X_trainx[0]))
        self.list_x_train_2.setRowCount(len(self.X_trainx))
        for i,row in enumerate(self.X_trainx):
           for j,cell in enumerate(row):
               self.list_x_train_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_train_2.horizontalHeader().setStretchLastSection(True)
        self.list_x_train_2.resizeColumnsToContents()

        #print(len(self.dataset))
        self.list_y_train_2.clear()
        self.list_y_train_2.setColumnCount(len(self.y_trainx[0]))
        self.list_y_train_2.setRowCount(len(self.y_trainx))
        for i,row in enumerate(self.y_trainx):
           for j,cell in enumerate(row):
               self.list_y_train_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_train_2.horizontalHeader().setStretchLastSection(True)
        self.list_y_train_2.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_x_test_2.clear()
        self.list_x_test_2.setColumnCount(len(self.X_testx[0]))
        self.list_x_test_2.setRowCount(len(self.X_testx))
        for i,row in enumerate(self.X_testx):
           for j,cell in enumerate(row):
               self.list_x_test_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_test_2.horizontalHeader().setStretchLastSection(True)
        self.list_x_test_2.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_y_test_2.clear()
        self.list_y_test_2.setColumnCount(len(self.y_testx[0]))
        self.list_y_test_2.setRowCount(len(self.y_testx))
        for i,row in enumerate(self.y_testx):
           for j,cell in enumerate(row):
               self.list_y_test_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_test_2.horizontalHeader().setStretchLastSection(True)
        self.list_y_test_2.resizeColumnsToContents()           

#---------------------2017 verileri bölme---------------------
        veriler = pd.read_csv('2017veriseti.csv')     
        x = veriler.iloc[:,1:2]
        y = veriler.iloc[:,2:]
        X = x.values
        Y = y.values 
        self.X_trainy, self.X_testy, self.y_trainy, self.y_testy = train_test_split(X,Y, test_size=0.5, random_state=42)
        #print(len(self.dataset))
        self.list_x_train_3.clear()
        self.list_x_train_3.setColumnCount(len(self.X_trainy[0]))
        self.list_x_train_3.setRowCount(len(self.X_trainy))
        for i,row in enumerate(self.X_trainy):
           for j,cell in enumerate(row):
               self.list_x_train_2.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_train_2.horizontalHeader().setStretchLastSection(True)
        self.list_x_train_2.resizeColumnsToContents()

        #print(len(self.dataset))
        self.list_y_train_3.clear()
        self.list_y_train_3.setColumnCount(len(self.y_trainy[0]))
        self.list_y_train_3.setRowCount(len(self.y_trainy))
        for i,row in enumerate(self.y_trainy):
           for j,cell in enumerate(row):
               self.list_y_train_3.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_train_3.horizontalHeader().setStretchLastSection(True)
        self.list_y_train_3.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_x_test_3.clear()
        self.list_x_test_3.setColumnCount(len(self.X_testy[0]))
        self.list_x_test_3.setRowCount(len(self.X_testy))
        for i,row in enumerate(self.X_testy):
           for j,cell in enumerate(row):
               self.list_x_test_3.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_x_test_3.horizontalHeader().setStretchLastSection(True)
        self.list_x_test_3.resizeColumnsToContents()
        
        #print(len(self.dataset))
        self.list_y_test_3.clear()
        self.list_y_test_3.setColumnCount(len(self.y_testy[0]))
        self.list_y_test_3.setRowCount(len(self.y_testy))
        for i,row in enumerate(self.y_testy):
           for j,cell in enumerate(row):
               self.list_y_test_3.setItem(i,j, QTableWidgetItem(str(cell)))
        self.list_y_test_3.horizontalHeader().setStretchLastSection(True)
        self.list_y_test_3.resizeColumnsToContents()        

        veriler = pd.read_csv('2015veriseti.csv')     
        x = veriler.iloc[:,1:2]
        y = veriler.iloc[:,2:]
        X = x.values
        Y = y.values   
        veriler2 = pd.read_csv('2016veriseti.csv')     
        x1 = veriler2.iloc[:,1:2]
        y1 = veriler2.iloc[:,2:]
        X1 = x1.values
        Y1 = y1.values 
        veriler3 = pd.read_csv('2017veriseti.csv')     
        x2 = veriler3.iloc[:,1:2]
        y2 = veriler3.iloc[:,2:]
        X2 = x2.values
        Y2 = y2.values        
        self.X_trainz, self.X_testz, self.y_trainz, self.y_testz = train_test_split(Y,Y1 ,test_size=0.5, random_state=42)
        self.X_trainw, self.X_testw, self.y_trainw, self.y_testw = train_test_split(Y1,Y2 ,test_size=0.5, random_state=42)
        self.X_trainp, self.X_testp, self.y_trainp, self.y_testp = train_test_split(Y,Y2 ,test_size=0.5, random_state=42)

    def maehesapla3(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_testw):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainw):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainw):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testw):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_18.setText(str(sonuc3))

    def maehesapla2(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_testw):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainw):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainw):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testw):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_15.setText(str(sonuc3))

    def maehesapla1(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_testz):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainz):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainz):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testz):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_9.setText(str(sonuc3))

    def maehesapla2017(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_testy):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainy):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainy):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_test):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_2.setText(str(sonuc3))
    def maehesapla2016(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_testx):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainx):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainx):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_test):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_6.setText(str(sonuc3))
    def maehesapla2015(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #mae formulü
        #xlerin toplamı
        for i,row in enumerate(self.X_test):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_train):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_train):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_test):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
       
        #bölme işlemi
        bolmedataset=[]
        for i,row in enumerate(yofdataset):
            ydegeri=float(xofdataset[i])/float(yofdataset[i])
            bolmedataset.append(ydegeri)  
        xtoplam=0.0
        for i,row in enumerate(bolmedataset):
            xtoplam=xtoplam+float(row)
 
        sonuc3=xtoplam/12
        self.lblr2sonuc_12.setText(str(sonuc3))

    def rmsehesapla3(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_testp):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainp):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testp):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainp):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_testp):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainp):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainp):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testp):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_13.setText(str(sonuc2))

    def rmsehesapla2(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_testw):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainw):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testw):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainw):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_testw):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainw):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainw):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testw):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_16.setText(str(sonuc2))

    def rmsehesapla1(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_testz):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainz):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testz):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainz):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_testz):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainz):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainz):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testz):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_10.setText(str(sonuc2))


    def rmsehesapla2017(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_test):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_train):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testy):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainy):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_testy):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainy):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainy):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testy):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_3.setText(str(sonuc2))

        
    def rmsehesapla2016(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_testx):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainx):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testx):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainx):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_testx):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainx):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_trainx):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_testx):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_7.setText(str(sonuc2))
        
    def rmsehesapla2015(self):
        xort=0
        yort=0
        xofort=0
        yofort=0
        xtoplam=0
        ytoplam=0
        xxtoplam=0
        yytoplam=0        
        xsayac=0
        ysayac=0
        ydegeri=0
        xdegeri=0 
        xoftoplam=0
        yoftoplam=0
        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0
        for i,row in enumerate(self.X_test):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_train):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac
        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_test):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_train):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1       
        
        #yoflerin ortlaması
        yofort=yoftoplam/ysayac        
        #xoflerin ortalaması        
        xofort=xoftoplam/xsayac
        
        #x*y işlemi
        xydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=xofdataset[i]*yofdataset[i]
            xydataset.append(sonuc)           
        #xy toplamı
        for i,row in enumerate(xydataset):
            xytoplam=xytoplam+row
                     
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc                
        
        ###RMSE FORMULU İŞLEMLERİ
        #xlerin toplamı
        for i,row in enumerate(self.X_test):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_train):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        #x ve y lerin ortalamaları
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac  
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_train):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_test):
            ydegeri=row - yort
            yofdataset.append(ydegeri)         
        
        #xlerin kareleri işlemi
        xsayac=0
        xxdataset=[]
        for i,row in enumerate(xofdataset):
            sonuc=row*row
            xxdataset.append(sonuc)
            xxtoplam=xxtoplam+sonuc
        
        
        #ylerin kareleri işlemi
        ysayac=0
        yydataset=[]
        for i,row in enumerate(yofdataset):
            sonuc=row*row
            yydataset.append(sonuc)
            yytoplam=yytoplam+sonuc         
        #cıkarma işlemi
        xtahmindataset=[]
        for i in range(len(xxdataset)):
            sonuc= int(xxdataset[i])-int(yydataset[i])
            xtahmindataset.append(sonuc)          
            xtahmintoplam=xtahmintoplam+sonuc        
        a=float(xtahmintoplam)

        number_iters=1500
        for i in range(number_iters):
            xtahmintoplam=0.5 *(float(xtahmintoplam)+float(a)/float(xtahmintoplam))
        xtahmintoplam=xtahmintoplam/10000
        sonuc2=abs(xtahmintoplam)
        self.lblr2sonuc_4.setText(str(sonuc2))
  
    def r2hesapla3(self):

        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_testp):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainp):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testp):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainp):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_testp):
            sonuc=self.X_testz[i]-self.y_trainp[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc_17.setText(str(sonuc))


    def r2hesapla2(self):

        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_testw):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainw):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testw):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainw):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_testw):
            sonuc=self.X_testz[i]-self.y_trainw[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc_14.setText(str(sonuc))        
    def r2hesapla1(self):

        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_testz):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainz):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testz):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainz):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_testz):
            sonuc=self.X_testz[i]-self.y_trainz[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc_8.setText(str(sonuc))
        
    def r2hesapla2015(self):
        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_test):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_train):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_test):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_train):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_test):
            sonuc=self.X_test[i]-self.y_train[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc_11.setText(str(sonuc))
  
    def r2hesapla2016(self):
        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_testx):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainx):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testx):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainx):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_testx):
            sonuc=self.X_test[i]-self.y_trainx[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc_5.setText(str(sonuc))    

    def r2hesapla2017(self):
        xtoplam=0
        ytoplam=0
        xsayac=0
        ysayac=0        
        xort=0
        yort=0
        xoftoplam=0
        yoftoplam=0                
        xofort=0
        yofort=0
        oukttopplam=0

        xxtoplam=0
        yytoplam=0        

        ydegeri=0
        xdegeri=0 

        xytoplam=0
        b2=0
        b1=0
        xtahmintoplam=0
        ytahmintoplam=0 
        #xlerin toplamı
        for i,row in enumerate(self.X_testy):
            xtoplam=xtoplam+row
            xsayac=xsayac+1
        #ylerin toplamı 
        for i,row in enumerate(self.y_trainy):
            ytoplam=ytoplam+row
            ysayac=ysayac+1
        yort=ytoplam/ysayac
        xort=xtoplam/xsayac        
        # x değişkeninin ortalmadan farkı
        xofdataset=[]
        for i,row in enumerate(self.X_testy):
            xdegeri=row - xort
            xofdataset.append(xdegeri)        
        
        #y değişkeninin ortalamadan farkı
        yofdataset=[]
        for i,row in enumerate(self.y_trainy):
            ydegeri=row - yort
            yofdataset.append(ydegeri)           
        #xoflerin toplamı
        xsayac=0
        for i,row in enumerate(xofdataset):
            xoftoplam=xoftoplam+row
            xsayac=xsayac+1
            
        ysayac=0
        #yoflerin toplamı 
        for i,row in enumerate(yofdataset):
            yoftoplam=yoftoplam+row
            ysayac=ysayac+1  
        ouktdataset=[]
        oukttopplam=0
        for i,row in enumerate(yofdataset):
            sonuc=int(xofdataset[i])-int(yofdataset[i])
            
            ouktdataset.append(sonuc) 
            oukttopplam=oukttopplam+sonuc 
        sonuc=int(oukttopplam)*int(oukttopplam)
        toplam=0.0   
        for i,row in enumerate(self.X_testy):
            sonuc=self.X_test[i]-self.y_trainy[i]
            toplam=toplam+sonuc
        akt=int(toplam)*int(toplam)
        sonuc=sonuc/akt
        sonuc=1-sonuc
        self.lblr2sonuc.setText(str(sonuc))        
        
    def hesapla(self):
        self.r2hesapla2017()
        self.r2hesapla2016()
        self.r2hesapla2015()
        self.r2hesapla1()
        self.r2hesapla2()
        self.r2hesapla3()
        self.rmsehesapla2015()        
        self.rmsehesapla2016() 
        self.rmsehesapla2017()
        self.rmsehesapla1() 
        self.rmsehesapla2() 
        self.rmsehesapla3()         
        self.maehesapla2015()
        self.maehesapla2016() 
        self.maehesapla2017()         
        self.maehesapla1()
        self.maehesapla2() 
        self.maehesapla3()