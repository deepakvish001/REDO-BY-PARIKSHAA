#pragma GCC optimize("O3,unroll-loops")
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    if (cin >> t) {
        while (t--) {
            long long n, k;
            cin >> n >> k;
            
            long long ans = 0;
            long long p = 1;
            
            while (n >= p) {
                long long cnt = min(k, n / p);
                ans += cnt;
                n -= cnt * p;
                p *= 2;
            }
            
            cout << ans << "\n";
        }
    }
    
    return 0;
}