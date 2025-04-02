# sanjay
a=int(input())
a=[["1","1","1","1","0"],["1","1","0","1","1"],["1","1","0","0","0"]]

def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                numIslands(grid, i, j)
                count += 1
    return count

print(numIslands(a))