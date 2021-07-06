import numpy as np
bag = [
    {"brown":0.3, "yellow":0.2, "red":0.2, "green":0.1, "orang":0.1, "yellow-brown":0.1},
    {"blue":0.24, "green":0.2, "orang":0.16, "yellow":0.14, "red":0.13, "brown":0.13}
]
priori = [1/2, 1/2]
print("sum of bag0 = {}".format(sum(bag[0].values())))
print("sum of bag1 = {}".format(sum(bag[1].values())))

picked_eachs = [
    ["yellow", "green"],
    ["green", "yellow"],
    ["blue", "green"],
    ["green", "blue"],
]

for picked_each in picked_eachs:
    # Case 1
    pick1_bag1 = bag[0][picked_each[0]] if (picked_each[0] in bag[0]) else 0
    pick2_bag2 = bag[1][picked_each[1]] if (picked_each[1] in bag[1]) else 0

    # Case 2
    pick2_bag1 = bag[0][picked_each[1]] if (picked_each[1] in bag[0]) else 0
    pick1_bag2 = bag[1][picked_each[0]] if (picked_each[0] in bag[1]) else 0

    likelihood = [pick1_bag1*pick2_bag2, pick2_bag1*pick1_bag2]
    priori_x_likelihood = np.array(priori)*np.array(likelihood)

    print('Case {} Probability:'.format(picked_each))
    for p in priori_x_likelihood:
        print("P={}".format(p/sum(priori_x_likelihood)))
    print("---------------")