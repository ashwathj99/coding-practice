def containsCycle(grid) -> bool:
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    found = False
    def gofind(x, y, px, py):
        visited[x][y] = True
        nonlocal found
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<rows and 0<=ny<cols and grid[nx][ny] == grid[x][y] and not(nx==px and ny==py):
                if visited[nx][ny]:
                    found = True
                    break
                else:
                    gofind(nx, ny, x, y)
    for x in range(rows):
        for y in range(cols):
            if not visited[x][y] and not found :
                gofind(x,y,-1,-1)
                if found:
                    return True
    return False
    