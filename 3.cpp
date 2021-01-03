#include <iostream>
using namespace std;

void swap(unsigned long long int *x,unsigned long long int *y)
{
  unsigned long long int z;
  z=*x;
  *x=*y;
  *y=z;
}

int main()
{
    int t;
    cin>>t;
    
    for(int i=0;i<t;i++)
    {
        unsigned long long int n,m;
        cin>>n>>m;
        unsigned long long int a[n];
        unsigned long long int b[m];
        unsigned long long int sum1=0;
        unsigned long long int sum2=0;
        for(int i=0;i<n;i++)
        {
            cin>>a[i];
            sum1 = sum1+a[i];
        }
        for(int j=0;j<m;j++)
        {
            cin>>b[j];
            sum2 = sum2+b[j];
        }
        for(int i=0;i<n-1;i++)
        {
           for(int j=i+1;j<n;j++)
           {
             if(a[j]<a[i])
             { swap(&a[j],&a[i]);}
           }
        }
        for(int i=0;i<m-1;i++)
        {
           for(int j=i+1;j<m;j++)
           {
             if(b[j]<b[i])
             { swap(&b[j],&b[i]); }
           }
        }
        
        if(sum1 > sum2)
        cout<<0<<endl;
        else
        {
            int swapp=0;
            for(int i=0 ; sum1<=sum2 ; i++)
            {
                unsigned long long int min_a = a[i];
                unsigned long long int max_b = b[m-1-i];
                
                if(min_a < max_b)
                {
                    swap(&min_a,&max_b);
                    sum1 = sum1 - max_b + min_a ;
                    sum2 = sum2 - min_a + max_b ;
                    swapp++;
                }
                else
                {
                    swapp = -1;
                    break;
                }
            }
            cout<<swapp<<endl;
        }
        
    }

return 0;
}  



