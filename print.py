import csv
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


columns = ['number', 'user_id', 'order_dt', 'order_price', 'order_age', 'city', 'product', 'phone', 'APP']
# 将 order_dt 转化为日期数据类型格式
df = pd.read_table(r'/Applications/test1.py/new_data_info_2.csv',names = columns,sep = ',')
# print(df.info())
print('-'*30)
# print(df.isnull().sum())
print('-'*30)
print(df.describe())
print('-'*30)
# print(df.head())
print('-'*30)
# print(df.tail())
print('-'*30)

columns_login = ['number', 'user_id', 'login_day', 'login_diff_time', 'distance_day', 'login_time', 'launch_time', 'Chinese_subscribe_num', 'math_subscribe_num', 'add_friend', 'add_group', 'camp_num', 'learn_num', 'finish_num', 'study_num', 'coupon', 'course_order_num']
# 将 order_dt 转化为日期数据类型格式
df_login = pd.read_table(r'/Applications/test1.py/new_login_day_info.csv',names = columns_login,sep = ',')
# print(df_login.info())
print('-'*30)
# print(df_login.isnull().sum())
print('-'*30)
print(df_login.describe())
print('-'*30)
# print(df_login.head())
print('-'*30)
# print(df_login.tail())
print('-'*30)


plt.figure(figsize=(12,4))
plt.scatter(x = 'order_age', y = 'order_price',data=df)
plt.xlabel('用户年龄')
plt.ylabel('用户定购价格')
plt.show()