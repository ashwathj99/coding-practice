def detonate(grid, r, c):   # returns a list of lists
    grid = [['O' if x=='.' else '.' for x in row] for row in grid]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
                if cell == '.':
                    if i>0: grid[i-1][j] = '.'
                    if j>0: grid[i][j-1] = '.'
                    if j<c-1 and grid[i][j+1] != '.' : grid[i][j+1] = '1'
                    if i<r-1 and grid[i+1][j] != '.' : grid[i+1][j] = '1'
                if cell == '1':
                            grid[i][j] = '.'
    return grid

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    if n == 1: return grid
    #pattern
    elif n % 2 == 0: return ['O'*c]*r
    elif n % 4 == 3: return [''.join(row) for row in detonate(grid, r, c)]
    elif n % 4 == 1: return [''.join(row) for row in detonate(detonate(grid, r, c), r, c)]
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print(result)
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
