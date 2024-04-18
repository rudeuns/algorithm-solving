#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;

    bool find_head = false, find_heart = false;
    int head_r, head_c, heart_r, heart_c;
    vector<string> grid(N);

    for(int r = 0; r < N; r++) {
        cin >> grid[r];
        for(int c = 0; c < N; c++) {
            if(grid[r][c] == '*') {
                if(!find_head) {
                    head_r = r; head_c = c;
                    find_head = true;
                }
                else if(!find_heart && c == head_c) {
                    heart_r = r; heart_c = c;
                    find_heart = true;
                }
            }
        }
    }

    int left_arm = 0, right_arm = 0, waist = 0, left_leg = 0, right_leg = 0;
    for(int c = heart_c - 1; c >= 0; c--) {
        if(grid[heart_r][c] == '_') { break; }
        left_arm += 1;
    }
    for(int c = heart_c + 1; c < N; c++) {
        if(grid[heart_r][c] == '_') { break; }
        right_arm += 1;
    }
    for(int r = heart_r + 1; r < N; r++) {
        if(grid[r][heart_c] == '_') {
            for(int rr = r; rr < N; rr++) {
                if(grid[rr][heart_c - 1] == '_') { break; }
                left_leg += 1;
            }
            for(int rr = r; rr < N; rr++) {
                if(grid[rr][heart_c + 1] == '_') { break; }
                right_leg += 1;
            }
            break;
        }
        waist += 1;
    }

    cout << heart_r + 1 << " " << heart_c + 1 << "\n";
    cout << left_arm << " " << right_arm << " " << waist << " " << left_leg << " " << right_leg;
    return 0;
}

/* Simulation */