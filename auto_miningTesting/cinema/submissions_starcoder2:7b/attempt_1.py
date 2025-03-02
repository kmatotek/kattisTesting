his text has been created for the purpose of learning how to submit code to an online judge. The source code is not graded. Do NOT copy or edit this text, as it may confuse the judge system.
*/

#include <iostream>
using namespace std;
int main() {
  int n,m;
  cin >>n>> m;

  int arr[50];
  
  for(int i= 0 ;i<m;i++){
    	cin >>arr[i];
  }

  int num = 1;


  while(num < m){
	  if(arr[num-1] == n)
		  break;
	  

	  if((n - arr[num]) <= 0){
		  num++;
		  
	  }

	  else{
		  n -= arr[num];
		  num++;
		  
	  }
  }

  cout<<m - num <<endl;