# Week 2 - Feature Noise
Purpose: analyze whether a difference in conversion rate between two checkout flow versions in a hypothesized A/B test is statistically real.

## Scenario
 Two versions of a checkout flow ran as an A/B test for two weeks. Daily conversion rate (%) was logged:


```python
version_a = [3.1, 2.9, 3.3, 3.0, 3.2, 2.8, 3.1, 3.4, 2.9, 3.0, 3.2, 3.1, 2.8, 3.3]
version_b = [3.4, 3.2, 3.6, 3.1, 3.5, 3.3, 3.7, 3.2, 3.5, 3.4, 3.3, 3.6, 3.4, 3.5]
```

## Method
Calculate the mean, standard deviation, t_score, and p_value of the a/b results
## Questions:
1) Calculate the mean and standard deviation of the results
2) Run a t-test (scipy.stats.ttest_ind) to check whether the difference between A and B is statistically significant, not just a lucky sample.
3) Interpret the p-value: at a 95% confidence threshold, would you ship version B?

## How to Run
```bash
pip install numpy scipy
python week2.py
```

## Code
```python
import statistics
from scipy.stats import ttest_ind
version_a = [3.1, 2.9, 3.3, 3.0, 3.2, 2.8, 3.1, 3.4, 2.9, 3.0, 3.2, 3.1, 2.8, 3.3]
version_b = [3.4, 3.2, 3.6, 3.1, 3.5, 3.3, 3.7, 3.2, 3.5, 3.4, 3.3, 3.6, 3.4, 3.5]

#Statistical calcs
mean_a = statistics.mean(version_a)
mean_b = statistics.mean(version_b)

print(mean_a,mean_b)

std_a = statistics.stdev(version_a)
std_b = statistics.stdev(version_b)
print(std_a,std_b)


#T_test
tresult = ttest_ind(version_a,version_b)

print(tresult)

## Inference:


From the data provided, a t-score of -4.80 and a p-value of 0.000057, we reject the null hypothesis that there is no real difference between versions A and B. Version B shows a statistically significant higher conversion rate than version A.

Furthermore, the t-score and p-value tell us that the 14-day test per version was a sufficient sample size to detect the conversion rate difference. This, however, does not tell us if the same results would stand under different conditions (e.g. seasonality), or whether the size of the lift is large enough to justify the cost of switching.


Note: Adoption data is synthetic (illustrative), not drawn from real product usage. Results demonstrate the modeling technique rather than an actual product finding.