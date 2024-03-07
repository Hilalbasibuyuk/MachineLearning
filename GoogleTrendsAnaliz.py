import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq # PyTrend kütüphanesi ile çalışıyoruz.

pytrend = TrendReq()

kw_list = ["python", "java", "javascript","visual basic"]
pytrend.build_payload(kw_list,cat=None,timeframe="2010-01-01 2023-09-09", geo = "CN") # cat = Kategori ve burada bir kategoriye sokmadık. timeframe = bakmak istediğimiz zaman aralıkları

df =pytrend.interest_over_time() # nesne datafrime olarak döner

df.to_csv("us_prog_lang_trends.csv") # df'yi excel dosyasına dönüştürüyoruz.

plt.figure(figsize=(8,6))
plt.plot(df.index,df.python,"k*")
plt.plot(df.index,df.java,"r*")
plt.plot(df.index,df.javascript,"b*")
plt.plot(df.index,df["visual basic"],"g*")
plt.legend(["python", "java", "javascript","visual basic"])
plt.show()


