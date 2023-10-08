// DAY 21 CODECHEF PROBLEM INTERMEDIATE MARKET
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--){
	   int x;
	   cin>>x;
	   int arr[3];
	   for(int i=0;i<3;i++){
	       cin>>arr[i];
	   }
	  sort(arr, arr+3);
	 cout<<(arr[0]*(x-1))+ arr[1]<<endl;
	}
	return 0;
}