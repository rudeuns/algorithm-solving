#include <iostream>
#include <vector>
using namespace std;
    
int R, C, T, up, down;
int dr[4] = {0, 0, -1, 1};
int dc[4] = {-1, 1, 0, 0};

void spread(vector<vector<int>>& grid) {
    vector<vector<int>> after(R + 2, vector<int>(C + 2, 0));
    after[up][1] = after[down][1] = -1;

    for(int r = 1; r <= R; r++) {
        for(int c = 1; c <= C; c++) {
            if(grid[r][c] > 0) {
                int cnt = 0;
                int v = (int)(grid[r][c] / 5);

                for(int i = 0; i < 4; i++) {
                    if(grid[r + dr[i]][c + dc[i]] != -1) {
                        after[r + dr[i]][c + dc[i]] += v;
                        cnt += 1;
                    }
                }
                after[r][c] += grid[r][c] - v * cnt;
            }
        }
    }

    for(int r = 1; r <= R; r++) {
        for(int c = 1; c <= C; c++) {
            grid[r][c] = after[r][c];
        }
    }
}

void wind(vector<vector<int>>& grid) {
    for(int r = up - 1; r > 1; r--) { 
        grid[r][1] = grid[r - 1][1];
    }
    for(int c = 1; c < C; c++) {
        grid[1][c] = grid[1][c + 1];
    }
    for(int r = 1; r < up; r++) {
        grid[r][C] = grid[r + 1][C];
    }
    for(int c = C; c > 2; c--) {
        grid[up][c] = grid[up][c - 1];
    }
    grid[up][2] = 0;

    for(int r = down + 1; r < R; r++) {
        grid[r][1] = grid[r + 1][1];
    }
    for(int c = 1; c < C; c++) {
        grid[R][c] = grid[R][c + 1];
    }
    for(int r = R; r > down; r--) {
        grid[r][C] = grid[r - 1][C];
    }
    for(int c = C; c > 2; c--) {
        grid[down][c] = grid[down][c - 1];
    }
    grid[down][2] = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> R >> C >> T;

    vector<vector<int>> grid(R + 2, vector<int>(C + 2, -1));
    for(int r = 1; r <= R; r++) {
        for(int c = 1; c <= C; c++) {
            cin >> grid[r][c];
        }
    }
    for(int r = 3; r < R; r++) {
        if(grid[r][1] == -1) {
            up = r; down = r + 1;
            break;
        }
    }

    while(T--) {
        spread(grid);
        wind(grid);
    }

    int answer = 2;
    for(int r = 1; r <= R; r++) {
        for(int c = 1; c <= C; c++) {
            answer += grid[r][c];
        }
    }

    cout << answer;
    return 0;
}

/* Simulation */