# Inicializiramo zacetno stanje
import random

N = 300
l = 5
results = []
for i in range(1000):
    opinions = [] # source agent je index 0
    sum_memory = [-1] * N

    for i in range(N):
        k = random.randint(0, 1)
        opinions.append(k)


    steps = 0

    while True:
        for ix in range(1,len(opinions)):
            index_list = set(range(len(opinions)))
            index_list.remove(ix)
            sample = set(random.sample(index_list, 2*l))
            sample1 = set(random.sample(sample, l))
            sample2 = sample - sample1

            sum1 = sum([opinions[i] for i in list(sample1)])
            sum2 = sum([opinions[i] for i in list(sample2)])

            if steps != 0:
                if sum1 > sum_memory[ix]:
                    opinions[ix] = 1
                elif sum1 < sum_memory[ix]:
                    opinions[ix] = 0
                
            sum_memory[ix] = sum2

        opinions_sum = sum(opinions)
        #print(opinions)
        #print(opinions[0],opinions_sum)
        steps += 1
        if opinions_sum == 0 or opinions_sum == N:
            break
    print("Finished in " + str(steps) + " steps.")
    results.append(steps)

print(N, sum(results) / len(results))
# 300 17.824