# Week 3 - Support Ticket Volume
Purpose: understand how linear regression is used to forecast support ticket volume, and how to judge the limits of a forecast built on a short, strongly fitting trend.

## Scenario
A product ops team tracked weekly support ticket volume for 10 weeks after a major feature launch. Leadership wants a forecast for weeks 11-14 to help staff the support team:

```python
week_history = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t_history = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270]
```

## Method
Fit a linear regression to weekly support ticket volume, forecast weeks 11 - 14 from the fitted line, and evaluate the fit using r².

## Questions
1) Fit a simple linear regression (`scipy.stats.linregress`) to the 10 weeks of ticket data. What are the slope and intercept?
2) Use the fitted line to forecast ticket volume for weeks 11-14.
3) Check the r-value (and r²). How well does a straight line describe this trend?
4) What could make this linear forecast wrong, and what would that mean for staffing the support team?

## How to Run
```bash
pip install numpy scipy
python week3.py
```

## Code
```python
import numpy as np
from scipy.stats import linregress

# Weekly support ticket volume after launch
week_history = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t_history = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270]

# Linear regression and fit statistics
res = linregress(week_history, t_history)
print(f"the slope is {res.slope}")
print(f"the intercept value is {res.intercept}")
print(f"the r-value is {res.rvalue}")
print(f"r-squared is {res.rvalue ** 2}")

# Forecast weeks 11 - 14
w_future = np.array([11, 12, 13, 14])
t_forecast = res.slope * w_future + res.intercept
print("Forecasted values:", t_forecast)
```

## Inference:

With an r² of 0.98, the linear model, using time as its only predictor, explains about 98% of the variability in the 10 weeks of ticket data. The forecast rises from 281 tickets in week 11 to about 310 in week 14, roughly 10 additional tickets per week. A strong fit to the first 10 weeks doesn’t guarantee the trend continues, because the model assumes constant growth. Post-launch volume often levels off, so these forecasts likely run high, which creates the risk of overstaffing the support team. The model also omits factors such as seasonality, marketing pushes, or bug fixes that could affect ticket volume.

Note: Ticket data is