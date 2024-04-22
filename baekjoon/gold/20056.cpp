#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Fireball {
public:
    int r, c, m, s, d;
    Fireball() {}
    Fireball(int rr, int cc, int mm, int ss, int dd) {
        r = rr; c = cc; m = mm; s = ss; d = dd;
    }
};

class Info {
public:
    int n, m, s;
    vector<int> d;
    Info() { n = m = s = 0; }
    void update(int mm, int ss, int dd) {
        m += mm;
        s += ss;
        d.push_back(dd);
        n += 1;
    }
};

int N, M, K;
queue<Fireball> Q;
int dr[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[8] = {0, 1, 1, 1, 0, -1, -1, -1};

void move() {
    vector<vector<Info>> grid(N, vector<Info>(N, Info()));

    while(!Q.empty()) {
        Fireball fb = Q.front(); Q.pop();
        int nr = (fb.r + (N + dr[fb.d]) * fb.s) % N;
        int nc = (fb.c + (N + dc[fb.d]) * fb.s) % N;
        grid[nr][nc].update(fb.m, fb.s, fb.d);
    }

    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            Info info = grid[r][c];

            if(info.n == 1) {
                Q.push(Fireball(r, c, info.m, info.s, info.d[0]));
            }
            else if(info.n > 1) {
                int new_m = (int)(info.m / 5);
                if(new_m == 0) { continue; }

                int new_s = (int)(info.s / info.n);
                bool odd = false, even = false;
                for(int i = 0; i < info.d.size(); i++) {
                    if(info.d[i] % 2 == 0) { even = true; }
                    else { odd = true; }
                }

                if(odd && even) {
                    for(int d = 1; d < 8; d += 2) {
                        Q.push(Fireball(r, c, new_m, new_s, d));
                    }
                }
                else {
                    for(int d = 0; d < 8; d += 2) {
                        Q.push(Fireball(r, c, new_m, new_s, d));
                    }
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M >> K;

    while(M--) {
        int r, c, m, s, d;
        cin >> r >> c >> m >> s >> d;
        Q.push(Fireball(r - 1, c - 1, m, s, d));
    }

    int answer = 0;
    while(K--) { move(); }
    while(!Q.empty()) {
        answer += Q.front().m;
        Q.pop();
    }

    cout << answer;
    return 0;
}

/* Simulation */