suits = [2,4,6,10,20]
# prior = [1/len(suits)]*len(suits)
get_num = 6
likelihood = [1/s if get_num <= s else 0 for s in suits]
probability =  [l/sum(likelihood) for l in likelihood]
print('Probability:')
for s, p  in zip(suits, probability):
    print('Suit:{:2}, P(Suit):{:0.3}'.format(s, p))