import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


def stats(array):
    return f"Standard deviation = {np.std(array)} \n Min = {np.min(array)} \n Max = {np.max(array)} \n Mean = {np.mean(array)} \n Median = {np.median(array)} \n 1 SD from mean = {100 * np.sum((array >= np.mean(array) - np.std(array)) & (array <= np.mean(array) + np.std(array)))/len(array)}"


result = np.array([])
outcomes = np.arange(1, 6)
# outcome = {0:"heads", 1: "tail"}

n_tosses = 10
n_experiments = 10

for _ in range(n_experiments):
    result = np.append(result, 1 + np.random.multinomial(n_tosses, [1/6]*6, n_experiments))


print(stats(result))

plt.hist(result, density=True, bins=6)
sb.kdeplot(result, color='red')
plt.show()