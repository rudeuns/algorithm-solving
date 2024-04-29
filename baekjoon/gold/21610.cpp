#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M;
queue<pair<int, int>> Q;
int dr[9] = {0, 0, -1, -1, -1, 0, 1, 1, 1};
int dc[9] = {0, -1, -1, 0, 1, 1, 1, 0, -1};

void rain(vector<vector<int>>& grid, int d, int s) {
    vector<vector<bool>> cloud(N, vector<bool>(N, false));

    while(!Q.empty()) {
        int r = (Q.front().first + (dr[d] + N) * s) % N;
        int c = (Q.front().second + (dc[d] + N) * s) % N;
        Q.pop();

        grid[r][c] += 1;
        cloud[r][c] = true;
    }

    vector<vector<int>> tmp(N, vector<int>(N, 0));
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            if(!cloud[r][c] && grid[r][c] >= 2) {
                Q.push({r, c});
                tmp[r][c] = -2;
            }
            else if(cloud[r][c]) {
                for(int i = 2; i <= 8; i+=2) {
                    int nr = r + dr[i], nc = c + dc[i];
                    if(nr >= 0 && nr < N && nc >= 0 && nc < N && grid[nr][nc] > 0) {
                        tmp[r][c] += 1;
                    }
                }
            }
        }
    }

    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            grid[r][c] += tmp[r][c];
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;

    vector<vector<int>> grid(N, vector<int>(N, 0));
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            cin >> grid[r][c];
        }
    }

    Q.push({N - 1, 0}); 
    Q.push({N - 1, 1}); 
    Q.push({N - 2, 0}); 
    Q.push({N - 2, 1});

    while(M--) {
        int d, s; 
        cin >> d >> s;

        rain(grid, d, s);
    }

    int answer = 0;
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            answer += grid[r][c];
        }
    }

    cout << answer;
    return 0;
}

/* Simulation */