#include <iostream>
#include <string>

using namespace std;

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    
    int even_idx_valid1 = 1, even_idx_valid2 = 1;
    for (int i = 0; i < n; i += 2) {
        int expected1 = (i / 2) % 2;
        int expected2 = 1 - expected1;
        if (s[i] != '?') {
            int val = s[i] - '0';
            if (val != expected1) even_idx_valid1 = 0;
            if (val != expected2) even_idx_valid2 = 0;
        }
    }
    
    int odd_idx_valid1 = 1, odd_idx_valid2 = 1;
    for (int i = 1; i < n; i += 2) {
        int expected1 = (i / 2) % 2;
        int expected2 = 1 - expected1;
        if (s[i] != '?') {
            int val = s[i] - '0';
            if (val != expected1) odd_idx_valid1 = 0;
            if (val != expected2) odd_idx_valid2 = 0;
        }
    }
    
    long long ans = (even_idx_valid1 + even_idx_valid2) * (odd_idx_valid1 + odd_idx_valid2);
    
    cout << ans % 998244353 << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    
    return 0;
}