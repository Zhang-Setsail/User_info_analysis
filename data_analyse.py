import csv
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# f = open("/Applications/test1.py/data_work/user_info.csv", "r")
# train = csv.reader(f)
# traindata = []
# traindata.append(next(train))
# # print(traindata)
# # traindata.pop()
# i=0
# print(type(traindata))
# while traindata[len(traindata)-1][0] != "":
#     try:
#         traindata.append(next(train))
#         i = i+1
#         # print(i)
#     except:
#         # print("1")
#         break
# # print(type(traindata))
# # traindata.pop()
# # print(traindata[len(traindata)-1])
# # print(traindata[0])
# traindata.pop(0)
# # print(traindata[0])

# f_login = open("/Applications/test1.py/data_work/login_day.csv", "r")
# login_info = csv.reader(f_login)
# login_info_table = []
# login_info_table.append(next(login_info))
# i=0
# print(type(login_info_table))
# while login_info_table[len(login_info_table)-1][0] != "":
#     try:
#         login_info_table.append(next(login_info))
#         i = i+1
#         print(i)
#     except:
#         print("1")
#         break
# login_info_table.pop(0)


# # print(len(traindata))

# # print(len(login_info_table))

# f_visit = open("/Applications/test1.py/data_work/visit_info.csv", "r")
# visit_info = csv.reader(f_visit)
# visit_info_table = []
# visit_info_table.append(next(visit_info))
# i=0
# print(type(visit_info_table))
# while visit_info_table[len(visit_info_table)-1][0] != "":
#     try:
#         visit_info_table.append(next(visit_info))
#         i = i+1
#         print(i)
#     except:
#         print("1")
#         break
# visit_info_table.pop(0)


# # print(len(traindata))

# # print(len(login_info_table))


# '''
# 价格1
# '''
# for p in traindata:
#     # print(p[2])
#     if float(p[2]) > 10:
#         try:
#             index_pos = traindata.index(p)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(p)
#         except:
#             traindata.remove(p)
#     print(len(traindata))

# '''
# 价格2
# '''
# for p in traindata:
#     # print(p[2])
#     if float(p[2]) > 10:
#         try:
#             index_pos = traindata.index(p)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(p)
#         except:
#             traindata.remove(p)
#     print(len(traindata))

# '''
# 价格3
# '''
# for p in traindata:
#     # print(p[2])
#     if float(p[2]) > 10:
#         try:
#             index_pos = traindata.index(p)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(p)
#         except:
#             traindata.remove(p)
#     print(len(traindata))

# print(len(traindata))
# print("niubi")
# print(len(login_info_table))

# '''
# 年龄1
# '''
# for j in traindata:
#     # print(j[3])
#     if int(j[3]) > 100 or int(j[3]) < 5:
#         try:
#             index_pos = traindata.index(j)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(j)
#         except:
#             traindata.remove(j)
#     print(len(traindata))

# '''
# 年龄2
# '''
# for j in traindata:
#     # print(j[3])
#     if int(j[3]) > 100 or int(j[3]) < 5:
#         try:
#             index_pos = traindata.index(j)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(j)
#         except:
#             traindata.remove(j)
#     print(len(traindata))

# '''
# 年龄3
# '''
# for j in traindata:
#     # print(j[3])
#     if int(j[3]) > 100 or int(j[3]) < 5:
#         try:
#             index_pos = traindata.index(j)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(j)
#         except:
#             traindata.remove(j)
#     print(len(traindata))

# '''
# 城市1
# '''
# for k in traindata:
#     # print(k[4])
#     if k[4] == "" or k[4] == "error":
#         try:
#             index_pos = traindata.index(k)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(k)
#         except:
#             traindata.remove(k)
#     print(len(traindata))


# '''
# 城市2
# '''
# for k in traindata:
#     # print(k[4])
#     if k[4] == "" or k[4] == "error":
#         try:
#             index_pos = traindata.index(k)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(k)
#         except:
#             traindata.remove(k)
#     print(len(traindata))

# '''
# 城市3
# '''
# for k in traindata:
#     # print(k[4])
#     if k[4] == "" or k[4] == "error":
#         try:
#             index_pos = traindata.index(k)
#             login_info_table.pop(index_pos)
#             visit_info_table.pop(index_pos)
#             traindata.remove(k)
#         except:
#             traindata.remove(k)
#     print(len(traindata))

# data_array = np.array(traindata)
# data_csv = pd.DataFrame(data_array)
# data_csv.to_csv('new_data_info_2.csv')

# login_array = np.array(login_info_table)
# login_csv = pd.DataFrame(login_array)
# login_csv.to_csv('new_login_day_info.csv')

# visit_array = np.array(visit_info_table)
# visit_csv = pd.DataFrame(visit_array)
# visit_csv.to_csv('new_visit_info.csv')


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

grouped_user = df.groupby('user_id')

# plt.figure(figsize=(12,4))
# plt.scatter(x = 'order_age', y = 'order_price',data=df)
# plt.xlabel('用户年龄')
# plt.ylabel('用户定购价格')
# plt.show()


plt.figure(figsize=(12, 4))
plt.subplot(121)
ax = grouped_user.order_age.sum().hist(bins=50)
ax.set_xlabel('金额（美元）')
ax.set_ylabel('用户人数')
ax.set_xlim(0, 2000)
ax.set_title('用户消费金额分布图')


# def data_in(id_list):
#     id_number = int(id_list[0])
#     for j in search_info_table:
#         if int(j[1]) == id_number:
#             return True
#     return False

# '''
# id
# '''
# for p in login_info_table:
#     # print(p[2])
#     if data_in(p) == False:
#         login_info_table.remove(p)
#     print(len(login_info_table))


