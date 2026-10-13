
#Three more weeks of ticket data have come in, and leadership wants to know whether the linear trend from Week 3 is still holding:

weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tickets = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275]
#Fit a simple linear regression (scipy.stats.linregress returns slope, intercept, and r-value in one call).
#Use the fitted line to forecast weeks 11, 12, 13, and 14.
#Check the r-value (or r-squared). How well does a straight line describe this trend?
#Honesty check: what could make this linear forecast wrong? Think about what usually happens to ticket volume over a longer horizon.

#Import
import numpy as np
from scipy.stats import linregress

# 1. Historical time steps (e.g., Month 1 to Month 10)
weeks = np.arange(1, 14)

# 2. Historical values (e.g., sales or demand)
tickets = np.array([180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275])

#Linear Regression
res = linregress(weeks, tickets)
print(f"the slope is {res.slope}")
print(f"the intercept value is {res.intercept}")
print(f"the r-value is {res.rvalue}")
print(f"r-squared is {res.rvalue ** 2}")

#Ticket difference
t_diff = np.diff(tickets)
print(t_diff)

#Linear forecast gap analysis
week14 = res.slope * 14 + res.intercept
print(week14)
#rvalue value
print(res.rvalue ** 2)
