#include <iostream>
#include <string>

using namespace std;

void solve() {
    string s;
    cin >> s;
    
    string s_prime = "";
    bool removed_one = false;
    for (char c : s) {
        if (c == '1' && !removed_one) {
            removed_one = true;
            continue;
        }
        s_prime += c;
    }
    
    string final_s = "";
    bool removed_zero = false;
    for (int i = 0; i < s_prime.length(); ++i) {
        if (!removed_zero && s_prime[i] == '0' && i + 1 < s_prime.length() && s_prime[i+1] == '1') {
            removed_zero = true;
            continue;
        }
        final_s += s_prime[i];
    }
    
    if (!removed_zero) {
        final_s = "";
        for (char c : s_prime) {
            if (c == '0' && !removed_zero) {
                removed_zero = true;
                continue;
            }
            final_s += c;
        }
    }
    
    cout << final_s << "\n";
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