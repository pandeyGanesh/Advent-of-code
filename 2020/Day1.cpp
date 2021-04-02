#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution{
    private:
        vector<int> entries;
    public:
        Solution(string file){
            ifstream fin;
            fin.open(file);
            int entry;
            while(fin){
                if(fin>>entry){
                    entries.push_back(entry);
                }
            }
        }

        void sortElements(){
            sort(entries.begin(), entries.end());
        }

        void printVector(){
            int length = entries.size();
            for(int i=0; i<length; ++i){
                cout<<entries[i]<<"\t";
                if(i%15==0){
                    cout<<"\n";
                }
            }
            cout<<endl;
        }

        void star1(){
            int begin = 0;
            int end = entries.size()-1;
            long sum;
            while(begin<end){
                sum = entries[begin] + entries[end];
                if(sum==2020){
                    cout<<entries[begin]*entries[end]<<endl;
                    break;
                }
                else if(sum<2020){
                    ++begin;
                }
                else if(sum>2020){
                    --end;
                }
            }
        }

        int star2(){
            // Uses 2 pointer approach
            for(int first=0; first<entries.size(); ++first){
                int limit = 2020 - entries[first];
                int begin = first+1;
                int end = entries.size()-1;
                long sum;
                while(begin<end){
                    sum = entries[begin] + entries[end];
                    if(sum==limit){
                        cout<<entries[begin]*entries[end]*entries[first]<<endl;
                        return 0;
                    }
                    else if(sum<limit){
                        ++begin;
                    }
                    else if(sum>limit){
                        --end;
                    }
                }
            }
            cout<<"Returning -1\n";
            return -1;
        }
};

int main(){
    Solution obj("inputs/Day1.txt");
    obj.sortElements();
    //obj.printVector();
    //obj.star1();
    obj.star2();
    return 0;
}