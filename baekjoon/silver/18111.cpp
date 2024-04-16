#include <iostream>
using namespace std;

int num[257];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int R, C, B;
    cin >> R >> C >> B;

    for(int r = 0; r < R; r++) {
        for(int c = 0; c < C; c++) {
            int h;
            cin >> h;
            num[h] += 1;
        }
    }

    int ans_t = -1, ans_h = -1;
    for(int h = 0; h <= 256; h++) { // 목표 height
        int t = 0, b = B;

        for(int cur_h = 256; cur_h >= 0; cur_h--) {
            if(num[cur_h] == 0) { continue; }

            if(cur_h > h) { 
                t += (cur_h - h) * num[cur_h] * 2;
                b += (cur_h - h) * num[cur_h];
            }
            else if(cur_h < h) {
                t += (h - cur_h) * num[cur_h];
                b -= (h - cur_h) * num[cur_h];
                if(b < 0) { break; }
            }
        }
        
        if(b >= 0 && (ans_t == -1 || t <= ans_t)) {
            ans_t = t; ans_h = h;
        }
    }

    cout << ans_t << " " << ans_h;
    return 0;
}

/* Simulation */