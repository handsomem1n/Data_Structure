def DFS(graph, s, visited) :
    print(graph[s], end= '')
    visited[s] = True # 방문 여부 확인을 위한 리스트


    for v in range(len(graph)) :
        if graph[s][v] != 0 :
            if visited[s] is not True :
                DFS(graph, v, visited)
