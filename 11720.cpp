#include <iostream>
#include <string>

int main(void){
    int N=0, Sum=0;
    std::cin>>N;
    std::string inputChar;
    std::cin>>inputChar;

    for(int i=0;i<N; i++){
        Sum+=(inputChar[i])-'0';
    }
    std::cout<<Sum<<std::endl;

    return 0;
}