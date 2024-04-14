#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Shark {
public:
    int r, c, t;
    Shark(int rr, int cc, int tt) {
        r = rr; c = cc; t = tt;
    }
    bool operator<(const Shark& other) const {
        if(t == other.t) {
            if(r == other.r) { 
                return c > other.c; 
            }
            return r > other.r;
        }
        return t > other.t;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    vector<vector<int>> grid(N, vector<int>(N));
    int sr, sc, st = 0, sz = 2, cnt = 0;

    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            cin >> grid[r][c];
            if(grid[r][c] == 9) {
                grid[r][c] = 0;
                sr = r; sc = c;
            }
        }
    }
    
    int dr[4] = {-1, 0, 0, 1};
    int dc[4] = {0, -1, 1, 0};
    bool stop = false;

    while(!stop) {
        priority_queue<Shark> pq;
        vector<vector<bool>> visited(N, vector<bool>(N, false));

        pq.push(Shark(sr, sc, st));
        visited[sr][sc] = true;

        stop = true;
        while(!pq.empty()) {
            Shark shk = pq.top(); pq.pop();

            if(grid[shk.r][shk.c] > 0 && grid[shk.r][shk.c] < sz) {
                if(sz == ++cnt) { sz += 1; cnt = 0; }
                grid[shk.r][shk.c] = 0;
                sr = shk.r; sc = shk.c; st = shk.t;
                stop = false;
                break;
            }

            for(int i = 0; i < 4; i++) {
                int nr = shk.r + dr[i], nc = shk.c + dc[i];

                if(nr < 0 || nr >= N || nc < 0 || nc >= N) { continue; }
                else if(visited[nr][nc] || grid[nr][nc] > sz) { continue; }
                else { 
                    pq.push(Shark(nr, nc, shk.t + 1)); 
                    visited[nr][nc] = true;
                }
            }
        }
    }

    cout << st;
    return 0;
}

/* Simulation | BFS | Min Heap */