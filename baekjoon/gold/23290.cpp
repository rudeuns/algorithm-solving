#include <iostream>
#include <vector>
using namespace std;

class Fish {
public:
    int r, c, d;
    Fish() {}
    Fish(int rr, int cc, int dd) {
        r = rr; c = cc; d = dd;
    }
    ~Fish() {}
};

vector<vector<int>> smell(6, vector<int>(6, -1));
vector<Fish> fish;
int dr[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int dc[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int sdr[5] = {0, -1, 0, 1, 0};
int sdc[5] = {0, 0, -1, 0, 1};
int shark[2], fish_num;
string shark_order;

void change_smell(vector<vector<vector<Fish>>>& grid) {
    for(int r = 1; r <= 4; r++) {
        for(int c = 1; c <= 4; c++) {
            if(smell[r][c] > 0) { smell[r][c] -= 1; }
        }
    }

    int sr = shark[0], sc = shark[1];
    for(int i = 0; i < 3; i++) {
        int idx = shark_order[i] - '0';
        sr = sr + sdr[idx];
        sc = sc + sdc[idx];

        if(grid[sr][sc].size() > 0) { 
            smell[sr][sc] = 2; 
            grid[sr][sc].clear();
        }
    }
    shark[0] = sr; shark[1] = sc;

    for(int r = 1; r <= 4; r++) {
        for(int c = 1; c <= 4; c++) {
            for(Fish f : grid[r][c]) {
                fish.push_back(f);
            }
        }
    }
}

void move_shark(vector<vector<vector<Fish>>>& grid, int iter, int sr, int sc, int fnum, string order) {
    if(iter == 3) {
        int d1 = order[0] - '0', d2 = order[1] - '0', d3 = order[2] - '0';
        if(d2 - d3 == 2 || d2 - d3 == -2) {
            fnum -= grid[shark[0] + sdr[d1]][shark[1] + sdc[d1]].size();
        }

        if(fnum > fish_num) {
            fish_num = fnum;
            shark_order = order;
        }
        else if(fnum == fish_num) {
            if(stoi(order) < stoi(shark_order)) {
                shark_order = order;
            }
        }
        return;
    }

    for(int i = 1; i <= 4; i++) {
        int nr = sr + sdr[i];
        int nc = sc + sdc[i];
        if(nr > 0 && nr <= 4 && nc >0 && nc <= 4) {
            move_shark(grid, iter + 1, nr, nc, fnum + grid[nr][nc].size(), order + to_string(i));
        }
    }
}

void move_fish() {
    vector<vector<vector<Fish>>> grid(6, vector<vector<Fish>>(6));
    for(Fish f : fish) {
        for(int i = 0; i <= 8; i++) {
            if(i == 8) {
                grid[f.r][f.c].push_back(Fish(f.r, f.c, f.d));
                break;
            }

            int nd = (f.d + 8 - i) % 8;
            int nr = f.r + dr[nd], nc = f.c + dc[nd];   
            if(smell[nr][nc] == 0 && (nr != shark[0] || nc != shark[1])) {
                grid[nr][nc].push_back(Fish(nr, nc, nd));
                break;
            }
        }
    }

    fish_num = 0;
    shark_order = "444";
    move_shark(grid, 0, shark[0], shark[1], 0, "");
    change_smell(grid);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int M, S; 
    cin >> M >> S;
    while(M--) {
        int r, c, d;
        cin >> r >> c >> d;
        fish.push_back(Fish(r, c, d - 1));
    }
    cin >> shark[0] >> shark[1];

    for(int r = 1; r <= 4; r++) {
        for(int c = 1; c <= 4; c++) {
            smell[r][c] = 0;
        }
    }

    while(S--) {
        move_fish();
    }

    cout << fish.size();
    return 0;
}

/* Simulation | DFS */