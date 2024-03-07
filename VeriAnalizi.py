import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer # Eksik olan veriler için kullanacağız
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

veriler = pd.read_csv("EksikVeriler.csv")
print(veriler)

imputer = SimpleImputer(missing_values=np.nan,strategy="mean") # Mean kullanarak ortalamayı alıp boş olan yerlere ortalamayı yazdırırız ve bir şey değişmemiş olur.
Yas = veriler.iloc[:,1:4].values
imputer = imputer.fit(Yas[:,1:4]) # İmputer nesnesini eğiterek eksik değerlerin yerine ortalama değeri eklemek için fit yöntemini kullanıyoruz
Yas[:,1:4] = imputer.transform(Yas[:,1:4]) # Eksik değerleri doldurmak için transform yöntemini kullanıyoruz
print(Yas)

# Ülkeleri 0-1'lere dönüştürmek. Sayısal değer olması açısından
ulke = veriler.iloc[:,0:1].values
le = preprocessing.LabelEncoder() # LabelEncoder kullanıldığında, her kategoriye bir sayı atanır.

ulke[:,0]= le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder() # OneHotEncoder, her farklı ülke için ayrı bir sütun oluşturur ve her sütun sadece bir ülkeyi temsil eder.
ulke = ohe.fit_transform(ulke).toarray() #Sonucu numpy dizisine dönüştürür
print(ulke)

# Yeni verilerin dataFrame'e dönüştürülmesi
sonuc = pd.DataFrame(data=ulke, index = range(22), columns= ["fr","tr","us"])
sonuc2 = pd.DataFrame(data = Yas, index=range(22), columns= ["boy", "kilo" ,"yas"])

cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data=cinsiyet,index=range(22),columns= ["cinsiyet"])

s = pd.concat([sonuc,sonuc2],axis=1)
s2 = pd.concat([s,sonuc3],axis=1)
print(s2)

# Verileri test ve train olarak bölüyoruz
x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=15)

# Verileri aynı dünyaya sokmak için küçültürüz
sc = StandardScaler()
X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

