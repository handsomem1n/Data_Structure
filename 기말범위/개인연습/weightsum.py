def weightsum_matrix(vertex_list, adj_matrix) :
    sum = 0
    for i in range(len(vertex_list)) :
        for j in range(len(i+1, vertex_list)) :
            if vertex_list is not None :
                sum = sum + vertex_list[i][j]
    return sum

def display_all_edges(vertex_list, adj_matrix) :
    for i in range(len(vertex_list)) :
        for j in range(i+1, len(vertex_list)) :
            if vertex_list[i][j] is not None and is not 0 :
                print(vertex_list[i], vertex_list[j], vertex_list[i][j], end= '')


def weightsum_list(graph) :
    for i in len(graph) :
        

