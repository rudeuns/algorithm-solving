#include <iostream>
#include <vector>
using namespace std;

class Sand {
public:
    int dr, dc;
    float p;
    Sand(int _dr, int _dc, float _p) {
        dr = _dr, dc = _dc, p = _p;
    }
};

int N, answer = 0;
int dr[4] = {0, 1, 0, -1};
int dc[4] = {-1, 0, 1, 0};
vector<Sand> flutter[4];

void spread(vector<vector<int>>& grid, int r, int c, int d) {
    int amount = grid[r][c];
    for(Sand sand : flutter[d]) {
        int nr = r + sand.dr;
        int nc = c + sand.dc;
        int a = (int)(amount * sand.p);

        if(nr < 0 || nr >= N || nc < 0 || nc >= N) { answer += a; }
        else { grid[nr][nc] += a; }
        grid[r][c] -= a; 
    }

    int nr = r + dr[d], nc = c + dc[d];
    if(nr < 0 || nr >= N || nc < 0 || nc >= N) { answer += grid[r][c]; }
    else { grid[nr][nc] += grid[r][c]; }
    grid[r][c] = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N;

    vector<vector<int>> grid(N, vector<int>(N));
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            cin >> grid[r][c];
        }
    }

    for(int i = 0; i < 4; i++) {
        int i1 = (i + 1) % 4, i2 = (i + 2) % 4, i3 = (i + 3) % 4;
        flutter[i].push_back(Sand(dr[i1], dc[i1], 0.07));
        flutter[i].push_back(Sand(dr[i3], dc[i3], 0.07));
        flutter[i].push_back(Sand(2 * dr[i1], 2 * dc[i1], 0.02));
        flutter[i].push_back(Sand(2 * dr[i3], 2 * dc[i3], 0.02));
        flutter[i].push_back(Sand(dr[i] + dr[i1], dc[i] + dc[i1], 0.1));
        flutter[i].push_back(Sand(dr[i] + dr[i3], dc[i] + dc[i3], 0.1));
        flutter[i].push_back(Sand(dr[i2] + dr[i1], dc[i2] + dc[i1], 0.01));
        flutter[i].push_back(Sand(dr[i2] + dr[i3], dc[i2] + dc[i3], 0.01));
        flutter[i].push_back(Sand(2 * dr[i], 2 * dc[i], 0.05));
    }

    int cur_r = N >> 1, cur_c = N >> 1, cur_d = 0, iter = 2;
    while(true) {
        for(int i = 0; i < (iter >> 1); i++) {
            cur_r = cur_r + dr[cur_d];
            cur_c = cur_c + dc[cur_d];

            spread(grid, cur_r, cur_c, cur_d);

            if(cur_r == 0 && cur_c == 0) {
                cout << answer;
                return 0;
            }
        }

        cur_d = (cur_d + 1) % 4;
        iter += 1;
    }

    return 0;
}

/* Simulation */