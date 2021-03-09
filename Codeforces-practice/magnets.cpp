#include<iostream>
#include<string>
using namespace std;

int main() {
	int n,count;
	string x,prev;
	
	cin>>n;
	count=1;
	cin>>prev;
	for(int i=0;i<n-1;i++){
		cin>>x;
		if(x!=prev){
			count+=1;
			prev=x;
		}
	}
	cout<<count;
	return 0;
}