#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

class Solution{
    private:
        vector<string> field;
    public:
        Solution(string file){
            ifstream fin;
            fin.open(file);
            string line;
            while(fin){
                if(getline(fin,line)){
                    field.push_back(line);
                }
            }
        }

        void print(){
            int length = field.size();
            for(int i=0; i<length; ++i){
                cout<<field[i]<<"\n";
            }
            cout<<endl;
        }

        void star1(){
            int currentPos = 0;
            int currentRow = 0;
            int totalRows = field.size();
            int fieldWidth = field[0].size();
            int tree = 0;

            ++currentRow;
            while(currentRow < totalRows){
                currentPos = (currentPos+3)%fieldWidth;
                if( field[currentRow][currentPos] == '#' ){
                    ++tree;
                }
                ++currentRow;
            }
            cout<<tree<<endl;
        }

        
        void star2(){
            vector<int> right = {1,3,5,7,1};
            vector<int> down = {1,1,1,1,2};

            long long answer = 1;
            for(int i=0; i<right.size(); ++i){
                int currentPos = 0;
                int currentRow = 0;
                int totalRows = field.size();
                int fieldWidth = field[0].size();
                int tree = 0;

                currentRow += down[i];
                while(currentRow < totalRows){
                    currentPos = (currentPos+right[i])%fieldWidth;
                    if( field[currentRow][currentPos] == '#' ){
                        ++tree;
                    }
                    currentRow += down[i];
                }
                answer *= tree;
            }
            cout<<answer<<endl;
        }
};

int main(){
    Solution obj("inputs/Day3.txt");
    //obj.print();
    //obj.star1();
    obj.star2();
    return 0;
}