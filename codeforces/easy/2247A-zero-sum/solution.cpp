#include <iostream>

using namespace std;

void solve() {
    int n;
    cin >> n;
    
    int minus_count = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        if (x == -1) {
            minus_count++;
        }
    }
    
    if (n % 2 != 0) {
        cout << "NO\n";
    } else {
        if (minus_count % 2 == (n / 2) % 2) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
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