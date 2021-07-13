import numpy as np
import matplotlib.pyplot as plt

uppers = [500, 1000, 2000] # 三種上限。證明多次觀測的結果，對上限不敏感
observes = [60 ,30 ,90] # 將多次觀測到的數據

for uppper in uppers:
    num_in_train = list(range(1, uppper+1))
    hypo = [1 for n in num_in_train]

    # 將多次觀測到的數據，分別計算出 likelihood，然後求 dot product
    likelihood = np.ones(shape=(len(num_in_train)))
    for got_num in observes:
        likelihood *= np.array([1/s if got_num <= s else 0 for s in num_in_train]) 

    hypo_x_likelihood = np.array(hypo)*np.array(likelihood)
    probability = [l/sum(hypo_x_likelihood) for l in hypo_x_likelihood]

    # print('Probability:')
    avg = 0
    for n, p  in zip(num_in_train, probability):
        # print('N:{:2}, P(N):{:0.3}'.format(n, p))
        avg += n*p
    print("posteriori avg:{}".format(avg))

    # Visualization
    plt.plot(probability)
    plt.show()