#include <iostream>
#include <vector>
using namespace std;

class Shark {
public:
    int r, c, d;
    int dd[5][4];
    bool gone = false;
    Shark() {}
};

int N, M, K;
int dr[5] = {0, -1, 1, 0, 0};
int dc[5] = {0, 0, 0, -1, 1};
int gone_num = 0;

void move_to(vector<vector<pair<int, int>>>& grid, vector<Shark>& sharks) {
    for(int m = 1; m <= M; m++) {
        Shark& S = sharks[m];

        if(!S.gone) {
            bool find_empty = false, find_self = false;
            int sr, sc, sd;

            for(int i = 0; i < 4; i++) {
                int nd = S.dd[S.d][i];
                int nr = S.r + dr[nd];
                int nc = S.c + dc[nd];

                if(nr < 0 || nr >= N || nc < 0 || nc >= N) { continue; }
                else if(grid[nr][nc].second <= 0) {
                    S.r = nr; S.c = nc; S.d = nd;
                    find_empty = true;
                    break;
                }
                else if(!find_self && grid[nr][nc].first == m) {
                    sr = nr; sc = nc; sd = nd;
                    find_self = true;
                }
            }

            if(!find_empty) {
                S.r = sr; S.c = sc; S.d = sd;
            }
        }
    }
}

void reduce_smell(vector<vector<pair<int, int>>>& grid) {
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            grid[r][c].second -= 1;
        }
    }
}

void move(vector<vector<pair<int, int>>>& grid, vector<Shark>& sharks) {
    for(int m = 1; m <= M; m++) {
        Shark& S = sharks[m];

        if(!S.gone) {
            if(grid[S.r][S.c].second < K) {
                grid[S.r][S.c].first = m;
                grid[S.r][S.c].second = K;
            }
            else {
                S.gone = true;
                gone_num += 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> K;

    vector<vector<pair<int, int>>> grid(N, vector<pair<int, int>>(N, {0, 0}));
    vector<Shark> sharks(M + 1, Shark());
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            int m;
            cin >> m;
            if(m > 0) {
                grid[r][c] = {m, K};
                sharks[m].r = r;
                sharks[m].c = c;
            }
        }
    }
    for(int m = 1; m <= M; m++) { 
        cin >> sharks[m].d; 
    }
    for(int m = 1; m <= M; m++) {
        for(int d = 1; d <= 4; d++) {
            for(int i = 0; i < 4; i++) {
                cin >> sharks[m].dd[d][i];
            }
        }
    }

    int T = 1;
    while(T <= 1000) {
        move_to(grid, sharks);
        reduce_smell(grid);
        move(grid, sharks);

        if(gone_num == M - 1) {
            cout << T;
            return 0;
        }
        T += 1;
    }

    cout << -1;
    return 0;
}

/* Simulation */