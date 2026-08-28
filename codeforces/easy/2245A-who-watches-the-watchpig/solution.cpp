#include <iostream>
#include <string>

using namespace std;

void solve() {
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;
    
    if (n < 2 * k) {
        cout << "-1\n";
        return;
    }
    
    int ans = 0;
    for (int i = 0; i < k; ++i) {
        if (s[i] == 'L') {
            ans++;
        }
    }
    for (int i = n - k; i < n; ++i) {
        if (s[i] == 'R') {
            ans++;
        }
    }
    
    cout << ans << "\n";
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