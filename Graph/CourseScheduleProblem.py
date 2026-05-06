#There are numCourses courses labeled from 0 to n-1.
#Given prerequisites, determine if you can finish all courses.

def canFinish(numCourse,pre):

    graph =[[] for _ in range(numCourse)]
    #print(graph)

    for a,b in pre:
        graph[a].append(b)

    visited = [0]*numCourse

    def dfs(course):

        if visited[course] == 1:
            return False
        
        if visited[course] == 2:
            return True
        
        visited[course] = 1

        for p in graph[course]:
            if not dfs(p):
                return False
            
        visited[course] = 2
        return True
    
    for c in range(numCourse):
        if not dfs(c):
            return False
    return True

print(canFinish(2,[[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))
print(canFinish(4,[[1,0],[2,3]]))


