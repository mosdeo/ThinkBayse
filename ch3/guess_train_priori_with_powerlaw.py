import numpy as np
import matplotlib.pyplot as plt
import math

uppers = [500, 1000, 2000] # 三種上限。證明多次觀測的結果，對上限不敏感
observes = [60 ,30 ,90] # 多次觀測到的數據

def powerlaw(x):
    return math.pow(x, -1)

for uppper in uppers:
    num_in_train = np.array(range(1, uppper+1))
    hypo = np.array(list(map(powerlaw, num_in_train)))

    # 將多次觀測到的數據，分別計算出 likelihood，然後求 dot product
    likelihood = np.ones(shape=(len(num_in_train)))
    for got_num in observes:
        likelihood *= np.array([1/s if got_num <= s else 0 for s in num_in_train]) 

    hypo_x_likelihood = hypo*likelihood
    probability = np.array([l/sum(hypo_x_likelihood) for l in hypo_x_likelihood])
    print("Upper={}, Average of Posteriori(後驗平均值):{}".format(uppper, sum(num_in_train*probability)))
    
    def myPercentile(percentile, pmf_list):
        total = 0;
        for i, p in enumerate(pmf_list):
            total += p
            if total >= percentile:
                return i
        return -1
    percentile_5, percentile_95 = myPercentile(0.05, probability), myPercentile(0.95, probability)
    print("Upper={}, 90% Confidence Interval(置信區間):{}".format(uppper, (percentile_5, percentile_95)))

    # Visualization
    plt.title("Upper = {}".format(uppper))
    plt.xlabel("Num of train")
    plt.ylabel("Probability")
    plt.plot(probability)
    plt.show()