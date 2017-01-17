__author__ = 'louisjyli'
file_name = 'email-Eu-core.txt'
file=open(file_name,'r+')
from cost import compute_cost

dict_cluster = {}
cluster_label = 0

for line in file:
    edge = line.split(' ')
    source_node = edge[0]
    dest_node = edge[1]
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