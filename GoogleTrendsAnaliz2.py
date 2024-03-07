import pandas as pd
import matplotlib.pyplot as pd
from pytrends.request import TrendReq

pytrend = TrendReq() # Nesne oluşturuyoruz.
pytrend.build_payload(kw_list=["python"],timeframe="2015-01-01 2023-09-09", geo = "US")

df_rt = pytrend.related_topics() # kw'de belirttiğimiz python hakkındaki aramalar. Dict ile döndürülür
lst = df_rt["python"]

rising_values = df_rt["python"]["rising"] #Python ile ilgili yükselen arama trendleri
# print(rising_values.head(20))

df_rq = pytrend.related_queries()
# print(df_rq["python"]["rising"].head())
# print(df_rq["python"]["top"].head())

print(pytrend.top_charts(date = "2021",geo = "TR")) # belirttiğimiz tarihte ve ülkede en çok aratılan şeyler