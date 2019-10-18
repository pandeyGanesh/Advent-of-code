#include<iostream>
#include<fstream>

using namespace std;

int main(){
	string line;
	unsigned length;
	int i, floor=0;
	ifstream fin("Day1.txt");
	while(fin){
		getline(fin,line);
	}
	fin.close();
	length = line.size();
	for(i=1; i<=length; i++){
		if(line[i-1]=='('){
			floor++;
		}
		else if(line[i-1]==')'){
			floor--;
		}
		if(floor==-1)
			break;
	}
	cout<<i;
	return 0;
}
