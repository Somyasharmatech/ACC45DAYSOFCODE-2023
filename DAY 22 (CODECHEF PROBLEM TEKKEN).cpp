//DAY 22 (CODECHEF PROBLEM TEKKEN)
#include <iostream>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--){
        int a,b,c;
        cin>>a>>b>>c;
        int x=max(b-c,c-b);
        if(a>x)cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        
    }
    
	return 0;
}