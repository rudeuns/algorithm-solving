#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<string> orders;
string number;
int len;

void choice(int l, int r, string prev, string order) {
    if(l < 0 && r >= len) {
        orders.insert(order);
        return;
    }

    if(l >= 0) {
        string cur(1, number[l]);
        choice(l - 1, r, cur + prev, order + cur + prev);
    }
    if(r < len) {
        string cur(1, number[r]);
        choice(l, r + 1, prev + cur, order + prev + cur);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> number;
    len = number.length();

    for(int i = 0; i < len; i++) {
        string cur(1, number[i]);
        choice(i - 1, i + 1, cur, cur);
    }

    cout << orders.size();
    return 0;
}

/* backtracking */