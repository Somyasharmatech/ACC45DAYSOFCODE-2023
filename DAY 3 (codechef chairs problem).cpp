//DAY 3 CHAIRS PROBLEM
#include <bits/stdc++.h>
using namespace std;

void solve()
{
    int X,Y;
    cin>>X>>Y;
    cout<<max(0,X-Y)<<endl;
}

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int t;
    cin>>t;
    
    while(t--)
    {
        solve();
    }
}
