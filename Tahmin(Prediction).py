import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

veriler = pd.read_csv("AylaraGoreSatisVerileri.csv")
print(veriler)

aylar = veriler["Aylar"]

satislar = veriler["Satislar"]

satislar2 = veriler.iloc[:,:1].values

x_train,x_test,y_train,y_test = train_test_split(aylar,satislar,test_size=0.33,random_state=0)

sc = StandardScaler()

X_test = sc.fit_transform(x_test)
X_train = sc.fit_transform(x_train)

Y_test =sc.fit_transform(y_test)
Y_train = sc.fit_transform(y_train)

# Model inşası (linear regression)
lr = LinearRegression()
lr.fit(X_train,Y_train)

tahmin = lr.predict(X_test)

x_train = x_train.sort_index()
y_train = y_train.sort_index()

plt.plot(x_train,y_train)
plt.plot(x_test,lr.predict(x_test))

plt.title("Aylara göre Satış")
plt.xlabel("Aylar")
plt.ylabel("Satışlar")

