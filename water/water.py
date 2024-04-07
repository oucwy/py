#!usr/bin/env python 
# -*- coding:utf-8 -*- 
""" 
@author: 姚 
@file: 水厂最终稿.py 
@time: 2022/06/17 
@desc: 
"""
import matplotlib.pyplot as plt
import datetime
import time
from keras.models import Sequential
# from keras.layers.core import Dense, Activation, Flatten
from keras.layers import Dense, Activation, Flatten
from xlrd import open_workbook
from pandas import read_excel
import pandas as pd
from sklearn.model_selection import train_test_split,KFold
from sklearn import metrics
from sklearn.metrics import mean_absolute_error  # 均方误差
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False

while True:
    # 对于出水总氮的预测
    a = datetime.datetime.now().strftime('%H:%M')
    # if a == '01:00' or a == '02:00' or a == '03:00' or a == '04:00' or a == '05:00' or a == '06:00' or \
    #    a == '07:00' or a == '08:00' or a == '09:00' or a == '10:00' or a == '11:00' or a == '12:00' or \
    #    a == '13:00' or a == '14:00' or a == '15:00' or a == '16:00' or a == '17:00' or a == '18:00' or \
    #    a == '19:00' or a == '20:46' or a == '21:00' or a == '22:00' or a == '23:00' or a == '24:00' :  #注释一
    if True:
        wb_TN = open_workbook("水厂最终稿TN.xls")    #注释二
        wb_TP = open_workbook("水厂最终稿TP.xls")    #注释三
        #####################################  请勿调整区域 起点1  #####################################
        data_TN = read_excel(wb_TN)
        data_TN_new = data_TN.dropna(axis=0)
        m_TN = data_TN_new.shape[0]
        n_TN = data_TN_new.shape[1]
        x_TN = data_TN_new.iloc[:, :n_TN - 1]
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        x_TN = scaler.fit_transform(x_TN)
        x_TN = pd.DataFrame(x_TN)
        x1_TN = x_TN.iloc[:m_TN - 1, :]
        x2_TN = x_TN.iloc[m_TN - 1:, :]
        y1_TN = data_TN_new.iloc[:m_TN - 1, n_TN - 1]
        X_train_TN, X_test_TN, Y_train_TN, Y_test_TN = train_test_split(x1_TN, y1_TN, test_size=0.05, random_state=0)
        def get_result_TN(y_true, y_pred):
            mse = metrics.mean_squared_error(y_true, y_pred)
            mae = metrics.mean_absolute_error(y_true, y_pred)
            r2 = metrics.r2_score(y_true, y_pred)
            return mse, mae, r2
        def BPNET_TN(input_dim, ouput_dim):
            # 创建序列模型
            model = Sequential()
            model.add(Dense(128, input_dim=input_dim))
            model.add(Activation('relu'))
            model.add(Dense(64))
            model.add(Activation('relu'))
            # 输出
            model.add(Dense(ouput_dim))
            model.add(Activation('relu'))
            model.compile(loss="mse", optimizer="adam", metrics=['mae'])
            return model
        a1_TN = n_TN - 1
        b1_TN = 1
        BP = BPNET_TN(a1_TN, b1_TN)
        result = []
        epochs = 300
        best_bp = 0
        for epoch in range(epochs):
            BP.fit(X_train_TN, Y_train_TN, epochs=1,verbose = 0)  # 95%数据训练模型
            Y_pre_TN = BP.predict(X_test_TN)  # 5%数据测试模型
            test_mse_TN, test_mae_TN, test_r2_TN = get_result_TN(Y_test_TN, Y_pre_TN)

            # 记录最好状态的权重值
            if test_r2_TN > best_bp:
                BP.save_weights('./BP_weights.pkl')
                best_bp = test_r2_TN
            result.append([test_mse_TN, test_mae_TN, test_r2_TN])
        Y_now_TN = BP.predict(x2_TN)
        Y_pre_TN = pd.DataFrame(Y_pre_TN)
        Y_test_TN = pd.DataFrame(Y_test_TN)
        pre_mae_TN = mean_absolute_error(Y_test_TN, Y_pre_TN)
        JG1_TN = pd.DataFrame(Y_now_TN)
        JG3_TN = Y_now_TN - pre_mae_TN  # 结果下限
        JG4_TN = Y_now_TN + pre_mae_TN  # 结果上限
        JG3_TN,JG4_TN  = pd.DataFrame(JG3_TN),pd.DataFrame(JG4_TN)
        JG_time_TN = datetime.datetime.now().strftime('%H:%M:%S')
        print(JG_time_TN)
        OUT1_TN = pd.concat([JG1_TN, JG3_TN, JG4_TN], axis=0)
        OUT1_TN = OUT1_TN.reset_index(drop=True)
        OUT2_TN = OUT1_TN.transpose()
        new_col_TN = ['总氮预测结果','总氮预测下限','总氮预测上限']
        OUT2_TN.columns = new_col_TN
        #####################################  请勿调整区域 终点1  #####################################
        writer = pd.ExcelWriter("结果1.xls")    #注释四
        OUT2_TN.to_excel(writer, 'page_1')
        writer.save()



        #####################################  请勿调整区域 起点2  #####################################
        data_TP = read_excel(wb_TP)
        data_TP_new = data_TP.dropna(axis=0)
        m_TP = data_TP_new.shape[0]
        n_TP = data_TP_new.shape[1]
        x_TP = data_TP_new.iloc[:, :n_TP - 1]

        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler()
        x_TP = scaler.fit_transform(x_TP)
        x_TP = pd.DataFrame(x_TP)
        x1_TP = x_TP.iloc[:m_TP - 1, :]
        x2_TP = x_TP.iloc[m_TP - 1:, :]
        y1_TP = data_TP_new.iloc[:m_TP - 1, n_TP - 1]
        X_train_TP, X_test_TP, Y_train_TP, Y_test_TP = train_test_split(x1_TP, y1_TP, test_size=0.05, random_state=0)
        def get_result_TP(y_true, y_pred):
            mse = metrics.mean_squared_error(y_true, y_pred)
            mae = metrics.mean_absolute_error(y_true, y_pred)
            r2 = metrics.r2_score(y_true, y_pred)
            return mse, mae, r2
        def BPNET_TP(input_dim, ouput_dim):
            # 创建序列模型
            model = Sequential()
            model.add(Dense(128, input_dim=input_dim))
            model.add(Activation('relu'))
            model.add(Dense(64))
            model.add(Activation('relu'))
            # 输出
            model.add(Dense(ouput_dim))
            model.add(Activation('relu'))
            model.compile(loss="mse", optimizer="adam", metrics=['mae'])
            return model

        a1_TP = n_TP - 1
        b1_TP = 1
        BP = BPNET_TP(a1_TP, b1_TP)
        result = []
        epochs = 300
        best_bp = 0
        for epoch in range(epochs):
            BP.fit(X_train_TP, Y_train_TP, epochs=1, verbose=0)  # 95%数据训练模型
            Y_pre_TP = BP.predict(X_test_TP)  # 5%数据测试模型
            test_mse_TP, test_mae_TP, test_r2_TP = get_result_TP(Y_test_TP, Y_pre_TP)

            # 记录最好状态的权重值
            if test_r2_TP > best_bp:
                BP.save_weights('./BP_weights.pkl')
                best_bp = test_r2_TP
            result.append([test_mse_TP, test_mae_TP, test_r2_TP])
        Y_now_TP = BP.predict(x2_TP)
        Y_pre_TP = pd.DataFrame(Y_pre_TP)
        Y_test_TP = pd.DataFrame(Y_test_TP)
        pre_mae_TP = mean_absolute_error(Y_test_TP, Y_pre_TP)
        JG1_TP = pd.DataFrame(Y_now_TP)
        JG3_TP = Y_now_TP - pre_mae_TP  # 结果下限
        JG4_TP = Y_now_TP + pre_mae_TP  # 结果上限
        JG3_TP, JG4_TP = pd.DataFrame(JG3_TP), pd.DataFrame(JG4_TP)
        JG_time_TP = datetime.datetime.now().strftime('%H:%M:%S')
        print(JG_time_TP)
        OUT1_TP = pd.concat([JG1_TP, JG3_TP, JG4_TP], axis=0)
        OUT1_TP = OUT1_TP.reset_index(drop=True)
        OUT2_TP = OUT1_TP.transpose()
        new_col_TP = ['总磷预测结果', '总磷预测下限', '总磷预测上限']
        OUT2_TP.columns = new_col_TP
        #####################################  请勿调整区域 终点2  #####################################
        writer = pd.ExcelWriter("c:/Users/姚/Desktop/结果2.xls")  #注释五
        OUT2_TP.to_excel(writer, 'page_1')  # 写在第一页
        writer.save()

        #####################################  请勿调整区域 起点3  #####################################
        writer = pd.ExcelWriter("c:/Users/姚/Desktop/空白文档.xls")
        OUT2_TP.to_excel(writer, 'page_1')  # 写在第一页
        writer.save()
        #####################################  请勿调整区域 终点3  #####################################

        time.sleep(120)

    else:
        continue