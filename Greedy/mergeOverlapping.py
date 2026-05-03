#Merge Overlapping intervals in  the 2D Array

def merge(grid):
    if not grid or not grid[0]:
        return []
    
    grid.sort(key=lambda x:x[0])

    merged = [grid[0]]

    for curr in grid[1:]:
        last = merged[-1]

        if curr[0]<=last[1]:
            last[1] = max(last[1],curr[1])
        else:
            merged.append(curr)
    return merged
    
print(merge([[1,3],[2,6],[8,10],[15,18]]))

#time: O(n log n)
#space: O(n)