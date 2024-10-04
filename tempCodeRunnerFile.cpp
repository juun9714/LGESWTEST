#include <iostream>
#include <cstring>

int main(void){
    int N=0, Sum=0;
    std::cin>>N;

    char * inputChar=new char(N+1);
    std::cin>>inputChar;

    for(int i=0;i<strlen(inputChar); i++){
        Sum+=(inputChar[i])-'0';
    }
    std::cout<<Sum<<std::endl;

    return 0;
}