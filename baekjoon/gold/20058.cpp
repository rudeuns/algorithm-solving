#include <iostream>
#include <vector>
using namespace std;

int N, answer = 0, max_sz = 0;
int dr[4] = {0, 0, -1, 1};
int dc[4] = {-1, 1, 0, 0};

void fire_storm(vector<vector<int>>& grid, int lv) {
    vector<vector<int>> tmp(N + 2, vector<int>(N + 2, 0));
    int step = 1 << lv;
    
    for(int i = 0; i < N; i += step) {
        for(int j = 0; j < N; j += step) {
            for(int r = 1, rc = step; r <= step; r++, rc--) {
                for(int c = 1; c <= step; c++) {
                    tmp[c + i][rc + j] = grid[r + i][c + j];
                }
            }
        }
    }
    
    for(int r = 1; r <= N; r++) {
        for(int c = 1; c <= N; c++) {
            int zero_num = 0;
            for(int i = 0; i < 4; i++) {
                if(tmp[r + dr[i]][c + dc[i]] <= 0) { zero_num += 1; }
                if(zero_num > 1) { break; }
            }

            if(zero_num > 1) { grid[r][c] = tmp[r][c] - 1; }
            else { grid[r][c] = tmp[r][c]; }
        }
    }
}

int dfs(vector<vector<int>>& grid, int r, int c) {
    answer += grid[r][c];
    grid[r][c] = 0;

    int connect = 0;
    for(int i = 0; i < 4; i++) {
        if(grid[r + dr[i]][c + dc[i]] > 0) {
            connect += dfs(grid, r + dr[i], c + dc[i]);
        }
    }

    return 1 + connect;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n, Q; cin >> n >> Q;
    N = 1 << n;

    vector<vector<int>> grid(N + 2, vector<int>(N + 2, 0));
    for(int r = 1; r <= N; r++) {
        for(int c = 1; c <= N; c++) {
            cin >> grid[r][c];
        }
    }

    while(Q--) {
        int lv; cin >> lv;
        fire_storm(grid, lv);
    }

    for(int r = 1; r <= N; r++) {
        for(int c = 1; c <= N; c++) {
            if(grid[r][c] > 0) {
                int sz = dfs(grid, r, c);
                if(max_sz == 0 || sz > max_sz) { max_sz = sz; }
            }
        }
    }

    cout << answer << "\n" << max_sz;
    return 0;
}

/* Simulation | DFS */