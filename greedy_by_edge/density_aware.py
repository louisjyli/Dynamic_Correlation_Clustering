__author__ = 'louisjyli'
file_name = 'CollegeMsg.txt'
#file_name = 'email-Eu-core.txt'
file=open(file_name,'r+')
from cost import compute_cost
import time

start_time = time.time()

dict_cluster = {}
cluster_label = 0
m = 0
dens = 0.5

for line in file:
    edge = line.split(' ')
    source_node = edge[0]
    dest_node = edge[1].strip('\n')
    m += 1
    n = len(dict_cluster)
    if n == 0:
        n = 2
    else:
        a = 0
    if source_node not in dict_cluster and dest_node not in dict_cluster and m/(n*(n-1)) >= dens:
        dict_cluster[source_node] = cluster_label
        dict_cluster[dest_node] = cluster_label
        cluster_label += 1
    elif source_node not in dict_cluster and dest_node not in dict_cluster and m/(n*(n-1)) < dens:
        dict_cluster[source_node] = cluster_label
        cluster_label += 1
        dict_cluster[dest_node] = cluster_label
    elif source_node in dict_cluster and dest_node not in dict_cluster and m/(n*(n-1)) >= dens:
        dict_cluster[dest_node] = dict_cluster[source_node]
    elif source_node in dict_cluster and dest_node not in dict_cluster and m/(n*(n-1)) < dens:
        dict_cluster[dest_node] = cluster_label
        cluster_label += 1
    elif source_node not in dict_cluster and dest_node in dict_cluster and m/(n*(n-1)) < dens:
        dict_cluster[source_node] = dict_cluster[dest_node]
    elif source_node not in dict_cluster and dest_node in dict_cluster and m/(n*(n-1)) < dens:
        dict_cluster[source_node] = cluster_label
        cluster_label += 1
    else:
        a = 0

performance = compute_cost(file_name,dict_cluster)
print('(Cost, Agreement, Gain) : ' + str(performance))
print('Number of clusters : ' + str(cluster_label))
print("---Execution Time : %s seconds ---" % (time.time() - start_time))