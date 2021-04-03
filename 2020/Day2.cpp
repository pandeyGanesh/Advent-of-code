#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

class Solution{
    private:
        vector<int> start;
        vector<int> end;
        vector<char> character;
        vector<string> password;
    public:
        Solution(string file){
            ifstream fin;
            fin.open(file);
            string line;

            int temp;
            string number;
            while(fin){
                if(getline(fin,line)){
                    number = line.substr(0, line.find("-"));
                    start.push_back( stoi(number) );
                    
                    number = line.substr(line.find("-")+1, line.find(" "));
                    end.push_back( stoi(number) );

                    character.push_back( line.at( line.find(" ")+1 ) );

                    password.push_back( line.substr( line.find(":")+2 ) );
                }
            }
        }

        void print(){
            int length = password.size();
            for(int i=0; i<length; ++i){
                cout<<start[i]<<"\t"<<end[i]<<"\t";
                cout<<character[i]<<"\t"<<password[i]<<"\n";
            }
            cout<<endl;
        }

        void star1(){
            int validPassword = 0;
            int length = password.size();
            for(int i=0; i<length; ++i){
                int characterCount = 0;
                int passwordLength = password[i].size();
                for(int j=0; j<passwordLength; ++j){
                    if( password[i].at(j) == character[i] ){
                        ++characterCount;
                    }
                }

                if( characterCount>=start[i] && characterCount<=end[i]){
                    ++validPassword;
                }
            }
            cout<<validPassword<<endl;
        }

        void star2(){
            int validPassword = 0;
            int length = password.size();
            for(int i=0; i<length; ++i){
                if( (password[i].at(start[i]-1) == character[i] && password[i].at(end[i]-1) != character[i]) || 
                    (password[i].at(start[i]-1) != character[i] && password[i].at(end[i]-1) == character[i]) ){
                    ++validPassword;
                }
            }
            cout<<validPassword<<endl;
        }
};

int main(){
    Solution obj("inputs/Day2.txt");
    //obj.print();
    //obj.star1();
    obj.star2();
    return 0;
}