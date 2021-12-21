from __future__ import print_function
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

# 数据
dta = [-612,
       277,
       377,
       -3266,
       -950,
       2336,
       1459,
       -829,
       1191,
       238,
       -2965,
       -1764,
       -85,
       5312,
       3,
       -1342,
       1733,
       -4106,
       -1461,
       3186,
       -92,
       411,
       -650,
       118,
       -2676,
       -469,
       3051,
       1122,
       -329,
       247,
       866,
       -2548,
       -1414,
       3125,
       371,
       274,
       533,
       -175,
       -2332,
       -1388,
       3060,
       1369,
       676,
       -806,
       522,
       -2199,
       -2511,
       3901,
       -36,
       920,
       -1108,
       2175,
       -2333,
       -1105,
       3029,
       -31,
       2305,
       1302,
       2761,
       -4775,
       -3201,
       7769,
       -1214,
       1817,
       -5271,
       971,
       -2446,
       -3705,
       3329,
       229,
       1952,
       -2434,
       1130,
       -3521,
       -503,
       5004,
       -2211,
       2046,
       521,
       -363,
       -2723,
       -2609,
       4091,
       1314,
       1050,
       -574,
       -585,
       -3632,
       -659,
       ]

dta = pd.Series(dta)
dta.index = pd.Index(sm.tsa.datetools.dates_from_range('2002', '2090'))
dta.plot(figsize=(12, 8))
plt.show()

# plot acf and pacf
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
sm.graphics.tsa.plot_acf(dta.values, lags=40, ax=ax1)  # lags 表示滞后的阶数
ax2 = fig.add_subplot(212)
sm.graphics.tsa.plot_pacf(dta.values, lags=40, ax=ax2)
plt.show()

# 模型1
arma_mod70 = sm.tsa.ARMA(dta, (7, 0)).fit(disp=False)
print(arma_mod70.aic, arma_mod70.bic, arma_mod70.hqic)
# 模型2
arma_mod01 = sm.tsa.ARMA(dta, (0, 1)).fit(disp=False)
print(arma_mod01.aic, arma_mod01.bic, arma_mod01.hqic)
# 模型3
arma_mod71 = sm.tsa.ARMA(dta, (7, 1)).fit(disp=False)
print(arma_mod71.aic, arma_mod71.bic, arma_mod71.hqic)
# 模型4
arma_mod80 = sm.tsa.ARMA(dta, (8, 0)).fit(disp=False)
print(arma_mod80.aic, arma_mod80.bic, arma_mod80.hqic)
# 模型5（只是为了示范，p和q随便取的）
arma_mod32 = sm.tsa.ARMA(dta, (3, 2)).fit(disp=False)
print(arma_mod32.aic, arma_mod32.bic, arma_mod32.hqic)
# 最佳模型可以取aic最小的一个


# 模型检验
# 在指数平滑模型下，观察ARIMA模型的残差是否是平均值为0且方差为常数的正态分布（服从零均值、方差不变的正态分布），
# 同时也要观察连续残差是否（自）相关。

# 对ARMA(7,0)模型所产生的残差做自相关图
resid = arma_mod70.resid
fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=40, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(resid, lags=40, ax=ax2)
plt.show()

# 观察残差是否符合正态分布
# 这里使用QQ图，它用于直观验证一组数据是否来自某个分布，或者验证某两组数据是否来自同一（族）分布。
# 在教学和软件中常用的是检验数据是否来自于正态分布。
resid = arma_mod70.resid  # 残差
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit=True)
plt.show()

# Ljung-Box检验
# 略

# 模型预测
# 模型确定之后，就可以开始进行预测了，我们对未来十年的数据进行预测。

fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2001':].plot(ax=ax)
fig = arma_mod70.plot_predict('2009', '2250', dynamic=True, ax=ax, plot_insample=False, alpha=0.05)
plt.show()
print(arma_mod70.summary())

fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2001':].plot(ax=ax)
fig = arma_mod70.plot_predict('2009', '2250', dynamic=False, ax=ax, plot_insample=False, alpha=0.05)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2001':].plot(ax=ax)
fig = arma_mod32.plot_predict('2091', '2100', dynamic=True, ax=ax, plot_insample=False)
print(arma_mod32.summary())
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2001':].plot(ax=ax)
fig = arma_mod32.plot_predict('2091', '2100', dynamic=False, ax=ax, plot_insample=False)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2001':].plot(ax=ax)
fig = arma_mod32.plot_predict('2002', '2100', dynamic=False, ax=ax, plot_insample=False)
plt.show()
