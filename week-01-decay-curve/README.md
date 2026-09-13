# Week 1 - Decay Curve
Purpose: understand how decay curves are mathematically modeled and utilize dummy data to model the output.

## Scenario
The team shipped a new feature 90 days ago. Daily active usage (as % of users who tried it at least once) was logged weekly:

```python
weeks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
adoption_pct = [42, 35, 31, 28, 26, 25, 24, 23.5, 23, 22.8, 22.6, 22.5]
```

## Method
Fit a simple model to model the decay curve
## Questions:
1) Estimate the "steady-state" adoption rate the feature is converging to
2) is this feature a hit, a dud, or a niche tool — and what threshold would you use to decide?

## How to Run
```bash
pip install numpy scipy matplotlib
python week1.py
```

## Code
```python
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Model definitions
def decay_model(t, a, b, c):
    return a * np.exp(-b * t) + c

# Array alignment
x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_data = [42, 35, 31, 28, 26, 25, 24, 23.5, 23, 22.8, 22.6, 22.5]
ymin = min(y_data)

# Fitting the curve to the data
initial_guess = [20, 0.5, ymin]
popt, pcov = curve_fit(decay_model, x_data, y_data, p0=initial_guess)
a_opt, b_opt, c_opt = popt

# Standard errors
std_errors = np.sqrt(np.diag(pcov))

# Predicting across all 12 weeks
predicted_weeks = decay_model(np.array(x_data), a_opt, b_opt, c_opt)
print(popt)
print(predicted_weeks)
print(std_errors)

plt.figure(figsize=(9, 5))
plt.scatter(x_data, y_data, color='lightsteelblue', label='Observed Values', zorder=5)
plt.plot(x_data, predicted_weeks, color='slategray',
         label=f'Fit: $y = {a_opt:.1f}e^{{-{b_opt:.2f}x}} + {c_opt:.1f}$', linewidth=2)
plt.title('Feature Adoption Percentage Over Weeks - Decay Curve', fontsize=14)
plt.xlabel('Weeks', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.savefig("week-01 Results")
plt.show()
```

## Inference:


"From the model and data provided, it appears that the feature adoption rate has gone from approximately 42% to 22.35%, with a standard error of ±0.0755 This is within the margin of error from the observed data of 22.5%.

Whether 22% represents a 'successful' outcome depends on context this dataset doesn't provide (e.g., the feature's cost to build/maintain, comparable adoption rates for similar features, or the original success bar set for the launch). Absent that context, the data supports only a narrower claim: adoption did not fail to find a stable base, though whether that base is large enough to justify continued investment is a separate business question."

Note: Adoption data is synthetic (illustrative), not drawn from real product usage. Results demonstrate the modeling technique rather than an actual product finding.