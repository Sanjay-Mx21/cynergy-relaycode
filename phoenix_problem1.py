# sanjay
a=[["1","1","1","1","0"],["1","1","0","1","1"],["1","1","0","0","0"]]
b = [['1','1','1','0','0'],['1','1','0','0','0'],['0','0','0','1','1'],['0','0','1','1','1']]

def helper(grid,i,j):
    try:
        if grid[i][j]=='1':
            grid[i][j]='0'
        if grid[i+1][j]=='1':
            helper(grid,i+1,j)
        
        if grid[i][j+1]=='1':
            helper(grid,i,j+1)


        if grid[i-1][j]=='1':
            helper(grid,i+1,j)
        if grid[i][j-1]=='1':
            helper(grid,i,j+1)
    except IndexError:
        pass

def numIslands(grid,i,j,count):
    
    try:
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    grid[i][j]='0'
                    for line in grid:
                        print(line)
                    print()
                    if grid[i+1][j]=='1':
                        helper(grid,i+1,j)
                    if grid[i][j+1]=='1':
                        helper(grid,i,j+1)
                    if grid[i-1][j]=='1':
                        helper(grid,i+1,j)
                    if grid[i][j-1]=='1':
                        helper(grid,i,j+1)
                                
                
    except IndexError:
        pass
    return count
for i in b:
    print(i)
print(numIslands(b,0,0,0))