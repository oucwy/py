'''
  The p-value tells us the probability of obtaining a result as extreme as the one we got, 
  given that the null hypothesis is true.
'''

from scipy.stats import mannwhitneyu

group_a = [1, 3, 5, 7, 9]
group_b = [2, 4, 6, 8, 10]
group_c = [1, 2, 3, 4, 5]
group_d = [6, 7, 8, 9, 10]

statistic, p_value = mannwhitneyu(group_a, group_b)
print("Statistic:", statistic)
print("p-value:", p_value)

statistic1, p_value1 = mannwhitneyu(group_c, group_d)
print("Statistic:", statistic1)
print("p-value:", p_value1)

