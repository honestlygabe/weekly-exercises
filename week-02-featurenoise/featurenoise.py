# Exercise: Is This Feature Actually Different, or Just Noisy?

# Two versions of a checkout flow ran as an A/B test for two weeks. Daily conversion rate (%) was logged:

# python

# Tasks:

# Compute the mean and standard deviation of each version.
# Run a t-test (scipy.stats.ttest_ind) to check whether the difference between A and B is statistically significant, not just a lucky sample.
# Interpret the p-value: at a 95% confidence threshold, would you ship version B?

#Importing packages
import statistics
import numpy as np
from scipy.stats import ttest_ind
#Recorded daily conversion rates
version_a = [3.1, 2.9, 3.3, 3.0, 3.2, 2.8, 3.1, 3.4, 2.9, 3.0, 3.2, 3.1, 2.8, 3.3]
version_b = [3.4, 3.2, 3.6, 3.1, 3.5, 3.3, 3.7, 3.2, 3.5, 3.4, 3.3, 3.6, 3.4, 3.5]

#Statistical calcs
mean_a = statistics.mean(version_a)
mean_b = statistics.mean(version_b)

print(mean_a,mean_b)

std_a = statistics.stdev(version_a)
std_b = statistics.stdev(version_b)
print(mean_a,mean_b)


#T_test
tresult = ttest_ind(version_a,version_b)

print(tresult)