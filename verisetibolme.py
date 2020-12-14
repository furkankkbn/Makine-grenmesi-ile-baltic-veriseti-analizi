import pandas as pd

from sklearn.model_selection import train_test_split
datafile_name = 'veriseti.xlsx'
data = pd.read_excel(datafile_name)
target_attribute = data['Classes']
X_train, X_test, y_train, y_test = train_test_split(data, target_attribute, test_size=0.3)

def Tekrarla():
    datafile_name = 'veriseti.xlsx'
    data = pd.read_excel(datafile_name)
    target_attribute = data['Classes']
    X_train, X_test, y_train, y_test = train_test_split(data, target_attribute, test_size=0.3)

def Kontrol1():
    for index,row in X_train.iterrows():
        if(row['Classes']==1): 
            return True
            break
def Kontrol2():
    for index,row in X_train.iterrows():
        if(row['Classes']==2): 
            return True
            break
def Kontrol3():
    for index,row in X_train.iterrows():
        if(row['Classes']==3): 
            return True
            break
def Kontrol4():
    for index,row in X_train.iterrows():
        if(row['Classes']==4): 
            return True
            break
def Kontrol5():
    for index,row in X_train.iterrows():
        if(row['Classes']==5): 
            return True
            break
def Kontrol6():
    for index,row in X_train.iterrows():
        if(row['Classes']==6): 
            return True
            break
def Kontrol7():
    for index,row in X_train.iterrows():
        if(row['Classes']==7): 
            return True
            break


if(Kontrol1()==True and Kontrol3()==True and Kontrol5()==True):
        print('herşey tamam')
else:
        print('programı yeninden çalışması gerek her parametreden bulunmamakta')
        Tekrarla()
        
print('işlem sonu')