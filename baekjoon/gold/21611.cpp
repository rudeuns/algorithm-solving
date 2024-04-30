#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, center, answer[4];
int dr[5] = {0, -1, 1, 0, 0};
int dc[5] = {0, 0, 0, -1, 1};
vector<pair<int, int>> pos;
queue<pair<int, int>> Q;

void pos_order() {
    for(int s = 1; s <= center; s++) {
        for(int r = 1 - s; r <= s; r++) {
            pos.push_back({center + r, center - s});
        }
        for(int c = 1 - s; c <= s; c++) {
            pos.push_back({center + s, center + c});
        }
        for(int r = s - 1; r >= -s; r--) {
            pos.push_back({center + r, center + s});
        }
        for(int c = s - 1; c >= -s; c--) {
            pos.push_back({center - s, center + c});
        }
    }
}

void push_bead(vector<vector<int>>& grid) {
    int prev = 0, num = 0;
    for(pair<int, int> p : pos) {
        int cur = grid[p.first][p.second];
        if(cur > 0) {
            if(prev == cur) { num += 1; }
            else {
                if(prev > 0) { Q.push({prev, num}); }
                prev = cur;
                num = 1;
            }
        }
    }
    if(prev > 0) { Q.push({prev, num}); }
}

void explosion() {
    bool finish = false;
    while(!finish) {
        queue<pair<int, int>> tmpQ;
        while(!Q.empty()) {
            pair<int, int> bd = Q.front(); Q.pop();
            if(bd.second >= 4) { answer[bd.first] += bd.second; }
            else { tmpQ.push(bd); }
        }

        finish = true;
        int prev = 0, num = 0;
        while(!tmpQ.empty()) {
            pair<int, int> bd = tmpQ.front(); tmpQ.pop();
            if(prev == bd.first) { num += bd.second; }
            else {
                if(num >= 4) { finish = false; }
                if(prev > 0) { Q.push({prev, num}); }
                prev = bd.first;
                num = bd.second;
            }
        }
        if(num >= 4) { finish = false; }
        if(prev > 0) { Q.push({prev, num}); }
    }
}

void change(vector<vector<int>>& grid) {
    int idx = 0;
    while(!Q.empty()) {
        if(idx >= pos.size()) {
            while(!Q.empty()) { Q.pop(); }
            break;
        }

        pair<int, int> bd = Q.front(); Q.pop();
        grid[pos[idx].first][pos[idx].second] = bd.second;
        grid[pos[idx + 1].first][pos[idx + 1].second] = bd.first;
        idx += 2;
    }
    while(idx < pos.size()) {
        grid[pos[idx].first][pos[idx].second] = 0;
        idx += 1;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> N >> M;
    center = N >> 1;

    vector<vector<int>> grid(N, vector<int>(N, 0));
    for(int r = 0; r < N; r++) {
        for(int c = 0; c < N; c++) {
            cin >> grid[r][c];
        }
    }
    pos_order();

    while(M--) {
        int d, s;
        cin >> d >> s;

        for(int i = 1; i <= s; i++) {
            grid[center + dr[d] * i][center + dc[d] * i] = 0;
        }

        push_bead(grid);
        explosion();
        change(grid);
    }

    cout << answer[1] + 2 * answer[2] + 3 * answer[3];
    return 0;
}

/* Simulation */