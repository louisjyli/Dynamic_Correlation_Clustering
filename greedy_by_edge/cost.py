__author__ = 'louisjyli'

def compute_cost(file_name, dict_cluster):
    edge_set = set()
    graph=open(file_name,'r+')
    TP = 0
    TF = 0
    for a_line in graph:
        an_edge = a_line.split(' ')
        s_node = an_edge[0]
        d_node = an_edge[1].strip('\n')
        edge_set.add(s_node+' '+d_node)
    for node1 in dict_cluster.keys():
        for node2 in dict_cluster.keys():
            if node1 != node2:
                checking_edge = node1 + ' ' + node2
                if checking_edge in edge_set and dict_cluster[node1]==dict_cluster[node2]:
                    TP += 1
                elif checking_edge not in edge_set and dict_cluster[node1]!=dict_cluster[node2]:
                    TF += 1
                else:
                    a = 0
            else:
                a = 0
    number_of_edges = len(dict_cluster)*(len(dict_cluster)-1)
    cost = number_of_edges - TP - TF
    agreement = TP + TF
    gain = agreement - cost
    return cost, agreement, gain