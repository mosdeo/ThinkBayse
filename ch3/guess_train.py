import numpy as np
import matplotlib.pyplot as plt
num_in_train = list(range(1, 1001))
prior_rate = [1 for n in num_in_train]
got_num = 60
likelihood = [1/s if got_num <= s else 0 for s in num_in_train]
priori_x_likelihood = np.array(likelihood)*np.array(prior_rate)
probability =  [l/sum(priori_x_likelihood) for l in priori_x_likelihood]
print('Probability:')
avg = 0
# for n, p  in zip(num_in_train, probability):
#     print('N:{:2}, P(N):{:0.3}'.format(n, p))
#     avg += n*p
print("avg:{}".format(avg))

# Visualization
plt.plot(probability)
plt.show()