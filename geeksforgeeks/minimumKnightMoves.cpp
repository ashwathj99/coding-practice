//perform bfs and mark movable cell as visited and increase distance parameter by 1
//when target reached return distance else return 1

#include <iostream>
#include <bits/stdc++.h> 
using namespace std;
struct cell
{ 
    int x, y; 
    int distance; 
    cell() {} 
    cell(int x, int y, int distance): x(x), y(y), distance(distance) { } 
};
bool isInside(int x, int y, int N) 
{ 
    if (x >= 1 && x <= N && y >= 1 && y <= N) 
        return true; 
    return false; 
}
int minKnightSteps( int N, int sx, int sy, int ex, int ey)
{ 
    //positions to which a knight can move
    int moveX[] = { -2, -1, 1, 2, -2, -1, 1, 2 }; 
    int moveY[] = { -1, -2, -2, -1, 1, 2, 2, 1 };
    queue<cell> q;
    q.push(cell(sx, sy, 0));
    cell curr;
    int x, y;
    bool visit[N + 1][N + 1]{};
    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++) 
            visit[i][j] = false;
    visit[sx][sy] = true;
    while (!q.empty())
    { 
        curr = q.front(); 
        q.pop();
        if (curr.x == ex && curr.y == ey) 
            return curr.distance;
        for (int i = 0; i < 8; i++)
        { 
            x = curr.x + moveX[i];
            y = curr.y + moveY[i];
            if (isInside(x, y, N) && !visit[x][y])
            { 
                visit[x][y] = true; 
                q.push(cell(x, y, curr.distance + 1)); 
            } 
        } 
    }
    return 1; //return -1 no solution
} 
int main() {
	int t;  cin>>t;
	while(t--)
	{
	    int n; cin>>n;
	    int sx, sy, ex, ey;
	    cin>>sx>>sy;    //start
	    cin>>ex>>ey;    //end
	    int res = minKnightSteps(n,sx,sy,ex,ey);
	    cout<<res<<endl;
	}
	return 0;
}