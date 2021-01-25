
#include <bits/stdc++.h> 
#include<iostream>
using namespace std;

void oddDiv(long long int n){
	for (int i=2;i<=n;i++){
		if (n%i!=0)
		{
			cout<<"YES"<<endl;
			break;
		}else{
			cout<<"NO"<<endl;
			break;
		}
	}
}

int main(){
		int T;
        int m=1;
		cin>>T;
	while (m<=T){
		long long int n;
		cin>>n;
		oddDiv(n);
        m++;
		
	}
	return 0;
}