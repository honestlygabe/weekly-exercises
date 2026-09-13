import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Model definitions
# 1. Define the model function

def decay_model(t, a, b, c):
    return a * np.exp(-b * t) + c

#Array definition
x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y_data = [42, 35, 31, 28, 26, 25, 24, 23.5, 23, 22.8, 22.6, 22.5]
ymin = min(y_data)

#Fitting curve
# 3. Fit the curve to the data
# p0 provides an initial guess for [a, b, c] to help the optimizer converge
initial_guess = [20, 0.5, ymin] 
popt, pcov = curve_fit(decay_model, x_data, y_data, p0=initial_guess)
a_opt, b_opt, c_opt = popt

#predicted_week1 = decay_model(1, a_opt, b_opt, c_opt)

#4 . Standard Errors
std_errors = np.sqrt(np.diag(pcov))

#5. Predicting across all 12 weeks

predicted_weeks = decay_model(np.array(x_data), a_opt, b_opt, c_opt)
print(popt)
print(predicted_weeks)
print(std_errors)

ci_lower = c_opt - 1.96 * std_errors[2]
ci_upper = c_opt + 1.96 * std_errors[2]
print(ci_lower, ci_upper)

plt.figure(figsize=(9, 5))
plt.scatter(x_data, y_data, color='lightsteelblue', label='Observed Values', zorder=5)
plt.plot(x_data, predicted_weeks, color='slategray', label=f'Fit: $y = {a_opt:.1f}e^{{-{b_opt:.2f}x}} + {c_opt:.1f}$', linewidth=2)

plt.title('Feature Adoption Percentage Over Weeks - Decay Curve', fontsize=14)
plt.xlabel('Weeks', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.savefig("week-01-results.png")
plt.show()


