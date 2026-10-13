
# Week 4 - Is Support Ticket Growth Slowing?
 Purpose: understand how to tell when a linear trend has stopped matching the data, using updated support ticket volume to test whether Week 3's forecast still holds.


## Scenario
Three more weeks of ticket data have come in, and leadership wants to know whether the linear trend from Week 3 is still holding:

```python
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tickets = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275]
```
## Method
Fit a simple linear regression (scipy.stats.linregress returns slope, intercept, and r-value in one call).

## Questions
1) Fit the same linear regression on all 13 weeks. How does the slope compare to Week 3's 9.7 tickets per week?
2) Look at the week-over-week changes. Is growth still steady, or is it leveling off?
3) Check the r-squared. How well does a straight line describe this trend?
4) What does the line forecast for week 14, and what could make that forecast wrong?

## How to Run
```bash
pip install numpy scipy
python week4.py
```
## Code
```python
import numpy as np
from scipy.stats import linregress

# Weekly support ticket volume, weeks 1-13
weeks = np.arange(1, 14)
tickets = np.array([180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275])

# Linear regression and fit statistics
res = linregress(weeks, tickets)
print(f"the slope is {res.slope}")
print(f"the intercept value is {res.intercept}")
print(f"the r-value is {res.rvalue}")
print(f"r-squared is {res.rvalue ** 2}")

# Week-over-week change
t_diff = np.diff(tickets)
print(t_diff)

# Linear forecast for week 14
week14 = res.slope * 14 + res.intercept
print(week14)
```

## Inference:
Week 3's slope of about 9.7 tickets per week fell to about 8.2 once the three new weeks were included, but tickets are still rising. The last five weekly changes (5, 10, 2, 2, 1) show growth leveling off. With an r² of 0.956, the line still fits the 13 weeks well, but it forecasts about 296 tickets for week 14. That is roughly 20 above the ~276 expected if the recent pace of 1-2 tickets a week continues. A high r² describes how well the line fits the past, not how well it forecasts, and staffing to the line risks overstaffing the support team.

Note: Ticket data is synthetic (illustrative), not drawn from real product usage. Results demonstrate the modeling technique rather than an actual product finding.