#include <iostream>
#include <vector>
using namespace std;

class Fish {
public:
    int r, c, d;
    bool eaten;
    Fish() { eaten = false; }
    Fish(int rr, int cc, int dd) {
        r = rr; c = cc; d = dd;
    }
};

class Shark {
public:
    int r, c, d, eat_num;
    Shark(int rr, int cc, int dd, int ee) {
        r = rr; c = cc; d = dd; eat_num = ee;
    }
};

int dr[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[8] = {0, -1, -1, -1, 0, 1, 1, 1}; 
int answer = 0;

void move_fish(vector<vector<int>>& grid, vector<Fish>& fish) {
    for(int n1 = 1; n1 <= 16; n1++) {
        if(fish[n1].eaten) { continue; }
        
        for(int i = fish[n1].d; i < fish[n1].d + 8; i++) {
            int d = i % 8;
            int r = fish[n1].r + dr[d];
            int c = fish[n1].c + dc[d];
            
            if(r >= 0 && r < 4 && c >= 0 && c < 4 && grid[r][c] >= 0) {
                int n2 = grid[r][c];
                if(n2 > 0) {
                    fish[n2].r = fish[n1].r;
                    fish[n2].c = fish[n1].c;
                }
                grid[fish[n1].r][fish[n1].c] = n2;
                grid[r][c] = n1;
                fish[n1].r = r;
                fish[n1].c = c;
                fish[n1].d = d;
                break;
            }
        }
    }
}

void move_shark(vector<vector<int>> grid, vector<Fish> fish, Shark shark) {
    if(answer < shark.eat_num) { answer = shark.eat_num; }

    move_fish(grid, fish);
    
    for(int i = 1; i <= 3; i++) {
        int r = shark.r + dr[shark.d] * i;
        int c = shark.c + dc[shark.d] * i;
        if(r >= 0 && r < 4 && c >= 0 && c < 4 && grid[r][c] > 0) {
            vector<vector<int>> new_grid = grid;
            vector<Fish> new_fish = fish;
            int n = grid[r][c];
            int d = fish[n].d;

            new_grid[r][c] = -1;
            new_grid[shark.r][shark.c] = 0;
            new_fish[n].eaten = true;
            move_shark(new_grid, new_fish, Shark(r, c, d, shark.eat_num + n));
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<vector<int>> grid(4, vector<int>(4));
    vector<Fish> fish(17, Fish());

    for(int r = 0; r < 4; r++) {
        for(int c = 0; c < 4; c++) {
            int a, b;
            cin >> a >> b;
            grid[r][c] = a;
            fish[a] = Fish(r, c, b - 1);
        }
    }

    int n = grid[0][0];
    int d = fish[n].d;
    fish[n].eaten = true;
    grid[0][0] = -1;
    
    move_shark(grid, fish, Shark(0, 0, d, n));
    
    cout << answer;
    return 0;
}

/* Simulation | DFS */