import networkx as nx
import random
import matplotlib.pyplot as plt

# TO NI NIC PAMETNEGA!

N = 50
results = []
#PRAVO MNENJE JE 1!
WEIGHT = 1

# Ustvarimo omrezje povezav
G = nx.gnp_random_graph(N, 0.2)
#G = nx.random_tree(N)
#G = nx.random_powerlaw_tree(N)

for i in range(1):
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
        for ix in range(len(opinions)):
            sum1 = WEIGHT
            for neighbor in G.neighbors(ix):
                sum1+= opinions[neighbor]

            if steps == 0:
                number_of_neighbors = len([n for n in G.neighbors(ix)]) + 1 #broadcaster
                if sum1 / number_of_neighbors >= 0.5: # prvi korak se nastavi mnenje na povprečno mnenje
                    opinions[ix] = 1
                else:
                    opinions[ix] = 0
            else:
                if sum1 > sum_memory[ix]: # sledimo trendom
                    opinions[ix] = 1
                elif sum1 < sum_memory[ix]:
                    opinions[ix] = 0
                
            sum_memory[ix] = sum1

        opinions_sum = sum(opinions)
        print(opinions)
        print(opinions_sum)
        node_colors = []
        for ix_c in range(len(opinions)):
            if opinions[ix_c] == 0:
                node_colors.append("red")
            else:
                node_colors.append("green")
        #nx.draw(G, node_color=node_colors)
        #plt.show()
        steps += 1
        if opinions_sum == 0 or opinions_sum == N:
            break
    print("Finished in " + str(steps) + " steps.")
    results.append(steps)

print(N, sum(results) / len(results))