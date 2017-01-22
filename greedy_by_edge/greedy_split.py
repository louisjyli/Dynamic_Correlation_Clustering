__author__ = 'louisjyli'
file_name = 'er_1000_0.8.txt'
file=open(file_name,'r+')
from cost import compute_cost
import time

start_time = time.time()

dict_cluster = {}
cluster_label = 0

for line in file:
    edge = line.split(' ')
    source_node = edge[0]
    dest_node = edge[1].strip('\n')
    if source_node not in dict_cluster and dest_node not in dict_cluster:
        dict_cluster[source_node] = cluster_label
        dict_cluster[dest_node] = cluster_label
        cluster_label += 1
    elif source_node in dict_cluster and dest_node not in dict_cluster:
        dict_cluster[dest_node] = cluster_label
        cluster_label += 1
    elif source_node not in dict_cluster and dest_node in dict_cluster:
        dict_cluster[source_node] = cluster_label
        cluster_label += 1
    else:
        a = 0

performance = compute_cost(file_name,dict_cluster)
print('(Cost, Agreement, Gain) : ' + str(performance))
print('Number of clusters : ' + str(cluster_label))
print("---Execution Time : %s seconds ---" % (time.time() - start_time))