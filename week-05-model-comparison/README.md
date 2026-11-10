# Week 5 - Which Model Should Leadership Trust for Staffing?
Purpose: understand how to compare a linear model and a saturating curve on the same data, and how to judge a forecast when the fitted ceiling is uncertain.

## Scenario
A product ops team has tracked weekly support ticket volume for 13 weeks since a major feature launch. The Week 4 line forecast about 296 tickets for week 14, but the last few weeks added only 1-2 tickets a week. Support leadership is setting staffing levels and asks whether a straight line is still the right tool:

```python
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
tickets = [180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275]
```

## Method
Fit a saturating curve (`c - a * exp(-b * t)`) with `scipy.optimize.curve_fit` and a straight line with `linregress`. Compare them by root mean squared error, forecast week 14 with each, and check how tightly the curve's ceiling is estimated.

## Questions
1) Fit a saturating curve to the 13 weeks. What are `a`, `b`, and the ceiling `c`?
2) Which model has the smaller root mean squared error, the line or the curve?
3) What does each model forecast for week 14, and which is closer to the ~276 the recent trend suggests?
4) How tightly is the ceiling estimated, and how much should you trust it?
5) What could make the curve wrong too, and what data would you want before staffing to one model?

## How to Run
```bash
pip install numpy scipy
python week5.py
```

## Code
```python
import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit

# Weekly support ticket volume, weeks 1-13
weeks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
tickets = np.array([180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275])

# Saturating curve: tickets level off at the ceiling c
def saturating_func(x, a, b, c):
    return c - a * np.exp(-b * x)

popt, pcov = curve_fit(saturating_func, weeks, tickets, p0=[95, 0.2, 275])
a_opt, b_opt, c_opt = popt
print(f"a = {a_opt:.2f}, b = {b_opt:.4f}, c = {c_opt:.2f}")

# Uncertainty on the fitted parameters and an approximate 95% range for the ceiling
std_errors = np.sqrt(np.diag(pcov))
print(std_errors)
ci_lower = c_opt - 1.96 * std_errors[2]
ci_upper = c_opt + 1.96 * std_errors[2]
print(ci_lower, ci_upper)

# Straight-line fit for comparison
res = linregress(weeks, tickets)
line_pred = res.slope * weeks + res.intercept
curve_pred = saturating_func(weeks, a_opt, b_opt, c_opt)

# Root mean squared error for each model
line_rmse = np.sqrt(np.mean((tickets - line_pred) ** 2))
curve_rmse = np.sqrt(np.mean((tickets - curve_pred) ** 2))
print(line_rmse, curve_rmse)

# Week 14 forecasts
print(res.slope * 14 + res.intercept)
print(saturating_func(14, a_opt, b_opt, c_opt))
```

## Inference
The curve fits the 13 weeks better than the line (root mean squared error of about 4.35 tickets versus 6.54), and its week 14 forecast of about 284 is closer than the line's 296 to the ~276 expected if the recent pace of 1-2 tickets a week continues. The line assumes linear growth, the same increase every week, which the recent weeks don't support. The curve assumes growth slows and levels off at a ceiling (`c`), estimated at about 330, but tickets haven't finished leveling off, so the data can't pin it down. The approximate 95% range for the ceiling is about 277 to 384.

A better fit to 13 weeks doesn't prove the curve is right, because both models were only checked on weeks they were fit to and the curve has an extra parameter. I would give leadership a range for week 14 (about 276 to 296) instead of one number, and I would want several more weeks of data to see whether weekly growth stays at 1-2 tickets before choosing a model.

Note: Ticket data is synthetic (illustrative), not drawn from real product usage. Results demonstrate the modeling technique rather than an actual product finding.
