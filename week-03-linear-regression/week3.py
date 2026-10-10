#Exercise: Forecasting Next Quarter’s Support Ticket Volume

#Your product ops team has tracked weekly support ticket volume for 10 weeks since a major feature launch

week_history = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t_history = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270]
#Fit a simple linear regression (scipy.stats.linregress returns slope, intercept, and r-value in one call).
#Use the fitted line to forecast weeks 11, 12, 13, and 14.
#Check the r-value (or r-squared). How well does a straight line describe this trend?
#Honesty check: what could make this linear forecast wrong? Think about what usually happens to ticket volume over a longer horizon.

#Import
import numpy as np
from scipy.stats import linregress

# 1. Historical time steps (e.g., Month 1 to Month 10)
week_history = np.arange(1, 11)

# 2. Historical values (e.g., sales or demand)
t_history = np.array([180, 195, 210, 205, 225, 235, 240, 255, 260, 270])

#Linear Regression
res = linregress(week_history, t_history)
print(f"the slope is {res.slope}")
print(f"the intercept value is {res.intercept}")
print(f"the r-value is {res.rvalue}")
print(f"the r-value is {res.rvalue}")
print(f"r-squared is {res.rvalue ** 2}")

# using values to predict weeks 11 - 14
w_future = np.array([11, 12, 13, 14])

t_forecast = res.slope * w_future + res.intercept

print("Forecasted values:", t_forecast)