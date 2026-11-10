#Import
import numpy as np
from scipy.stats import linregress
from scipy.optimize import curve_fit

weeks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
tickets = np.array([180, 195, 210, 205, 225, 235, 240, 255, 260, 270, 272, 274, 275])

#1. Fit a saturating curve with scipy.optimize.curve_fit, using the model c - a * np.exp(-b * t).

def saturating_func(x, a, b, c):
  return c - a * np.exp(-b * x)

#Initial variable tests and data assignment
x_data = weeks
y_data = tickets

initial_guess = [95, 0.2, 275] 

popt, pcov = curve_fit(saturating_func, x_data, y_data, p0=initial_guess)
a_opt, b_opt, c_opt = popt

print(popt)
#standard errors
std_errors = np.sqrt(np.diag(pcov))

print(std_errors)


#2.Fit the straight line again with linregress, then compute the residuals (actual minus predicted) for both models. 
#Regression

#Linear Regression, curve predicitons
res = linregress(weeks, tickets)
line_pred = res.slope * np.array(weeks) + res.intercept

curve_pred = saturating_func(np.array(weeks), a_opt, b_opt, c_opt)

#Residual checks
line_resid = tickets - line_pred
curve_resid = tickets - curve_pred
print(np.sqrt(np.mean(line_resid ** 2)))
print(np.sqrt(np.mean(curve_resid ** 2)))

#3.Forecast week 14 with each model and compare both to the roughly 276 the recent trend suggests.

res_pred =res.slope * 14 + res.intercept
sat_pred = saturating_func(14, a_opt, b_opt, c_opt)
print(res_pred)
print(sat_pred)

#4.Print popt and the standard errors from pcov, as you did in Week 1.
#95% confidence interval


ci_lower = c_opt - 1.96 * std_errors[2]
ci_upper = c_opt + 1.96 * std_errors[2]

print(ci_lower,ci_upper)

#5. Honesty check: a better fit to 13 weeks doesn’t prove the curve is right. What could make the curve wrong too? Think about what each model assumes about the future, and what data you’d want before telling leadership to staff to one of them.