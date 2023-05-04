import networkx as nx
import random
import matplotlib.pyplot as plt

N = 300
results = []

# Ustvarimo omrezje povezav
G = nx.gnp_random_graph(N, 0.2) ## KONVERGIRA
#G = nx.random_tree(N) ## NE KONVERGIRA
#G = nx.random_powerlaw_tree(N) ## NE KONVERGIRA

for i in range(1000):
    opinions = [] # source agent je index 0
    sum_memory = [-1] * N

    for i in range(N):
        k = random.randint(0, 1)
        opinions.append(k)

    print(opinions)
    node_colors = []
    for ix_c in range(len(opinions)):
        if opinions[ix_c] == 0:
            node_colors.append("red")
        else:
            node_colors.append("green")
    #nx.draw(G, node_color=node_colors)
    #plt.show()
    steps = 0

    while True:
   # for i in range(10):
        for ix in range(1,len(opinions)):
            sum1 = 0
            neighbor_list = [n for n in G.neighbors(ix)]
            number_of_neighbors = len(neighbor_list)

            sample = set(neighbor_list)
            sample1 = set(random.sample(sample, int(number_of_neighbors/2)))
            sample2 = sample - sample1

            sum1 = sum([opinions[i] for i in list(sample1)])
            sum2 = sum([opinions[i] for i in list(sample2)])

            if steps != 0:
                if sum1 > sum_memory[ix]:
                    opinions[ix] = 1
                elif sum1 < sum_memory[ix]:
                    opinions[ix] = 0
                
            sum_memory[ix] = sum1

        opinions_sum = sum(opinions)
        print(opinions)
        print(opinions[0],opinions_sum)
        node_colors = []
        for ix_c in range(len(opinions)):
            if opinions[ix_c] == 0:
                node_colors.append("red")
            else:
                node_colors.append("green")
        #nx.draw(G, node_color=node_colors)
        #plt.show()
        steps += 1
        if opinions_sum == 0 and opinions[0] == 1 or opinions_sum == N and opinions[0] == 0:
            print("CRKNE")
            exit(0)
        if opinions_sum == 0 or opinions_sum == N:
            break
    print("Finished in " + str(steps) + " steps.")
    results.append(steps)

print(N, sum(results) / len(results))
# 50 8.32
# 300 4.453