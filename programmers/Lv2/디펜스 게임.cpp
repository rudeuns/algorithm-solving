#include <iostream>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

int solution(int n, int k, vector<int> enemy) {
    priority_queue<int, vector<int>, greater<int>> pq; // min heap
    int answer = enemy.size();
    int killed = 0;

    for(int i = 0; i < enemy.size(); i++) {
        pq.push(enemy[i]);
        
        if(k <= i) {
            killed += pq.top();
            pq.pop();
        }
        if(n < killed) {
            answer = i;
            break;
        }
    }

    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n = 7, k = 3;
    vector<int> enemy = {4, 2, 4, 5, 3, 3, 1};

    cout << solution(n, k, enemy);

    return 0;
}

/* heap */