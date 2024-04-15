#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int R, C;
    cin >> R >> C;

    vector<vector<vector<int>>> val(R + 1, vector<vector<int>>(C, vector<int>(3, 0)));
    for(int r = 0; r < R; r++) {
        for(int c = 0; c < C; c++) {
            int v;
            cin >> v;
            val[r][c][0] = val[r][c][1] = val[r][c][2] = v;
        }
    }

    for(int r = 0; r < R; r++) {
        for(int c = 0; c < C; c++) {
            if(c == 0) {
                val[r + 1][c][1] += val[r][c][0];
                val[r + 1][c + 1][2] += min(val[r][c][0], val[r][c][1]);
            }
            else if(c == C - 1) {
                val[r + 1][c - 1][0] += min(val[r][c][1], val[r][c][2]);
                val[r + 1][c][1] += val[r][c][2];
            }
            else {
                val[r + 1][c - 1][0] += min(val[r][c][1], val[r][c][2]);
                val[r + 1][c][1] += min(val[r][c][0], val[r][c][2]);
                val[r + 1][c + 1][2] += min(val[r][c][0], val[r][c][1]);
            }
        }
    }

    int answer = val[R][0][1];
    for(int c = 0; c < C; c++) {
        if(c == 0) {
            int m = min(val[R][c][1], val[R][c][0]);
            if(answer > m) { answer = m; }
        }
        else if(c == C - 1) {
            int m = min(val[R][c][1], val[R][c][2]);
            if(answer > m) { answer = m; }
        }
        else {
            int m = min(min(val[R][c][0], val[R][c][1]), val[R][c][2]);
            if(answer > m) { answer = m; }
        }
    }

    cout << answer;
    return 0;
}

/* DP */