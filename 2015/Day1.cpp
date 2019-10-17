#include<iostream>
#include<fstream>

using namespace std;

int main(){
	string line;
	unsigned length,floor=0;
	ifstream fin("Day1.txt");
	while(fin){
		getline(fin,line);
	}
	fin.close();
	length = line.size();
	for(int i=0; i<length; i++){
		if(line[i]=='('){
			floor++;
		}
		else if(line[i]==')'){
			floor--;
		}
	}
	cout<<floor;
	return 0;
}
